import dataclasses
import glob
import mmap
import typing

import yaml
from yaml import constructor, resolver, _yaml, nodes

def find_document_paths() -> typing.List[str]:
    # note there are no json files
    return glob.glob('./openapi-directory/**/*.yaml', recursive=True)


def file_contains_3x_spec_version(document_path: str) -> bool:
    with open(document_path) as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(b'openapi: 3.0.0') != -1:
            return True
        if s.find(b'openapi: 3.0.1') != -1:
            return True
        if s.find(b'openapi: 3.0.2') != -1:
            return True
        if s.find(b'openapi: 3.0.3') != -1:
            return True
        if s.find(b'openapi: 3.1.0') != -1:
            return True
    return False


# needed to fix https://github.com/yaml/pyyaml/pull/635
yaml.constructor.SafeConstructor.add_constructor(
    'tag:yaml.org,2002:value',
    yaml.constructor.SafeConstructor.construct_yaml_str
)

@dataclasses.dataclass
class MetricsData:
    properties_key_qty: int = 0
    properties_not_adjacent_to_type_qty: int = 0
    properties_adjacent_to_type: typing.Dict[str, int] = dataclasses.field(default_factory=lambda: {})
    required_usage_qty: int = 0
    required_not_adjacent_to_type_qty: int = 0
    required_adjacent_to_type: typing.Dict[str, int] = dataclasses.field(default_factory=lambda: {})
    required_key_to_qty: typing.Dict[str, int] = dataclasses.field(default_factory=lambda: {})



class CustomConstructor(constructor.Constructor):
    def __init__(self, metrics_data: MetricsData) -> None:
        super().__init__()
        self.metrics_data = metrics_data

    def construct_mapping(self, node, deep=False):
        res = super().construct_mapping(node, deep=deep)
        if 'properties' in res:
            self.metrics_data.properties_key_qty += 1
            if 'type' in res:
                type_str = str(res['type'])
                if type_str not in self.metrics_data.properties_adjacent_to_type:
                    self.metrics_data.properties_adjacent_to_type[type_str] = 0
                self.metrics_data.properties_adjacent_to_type[type_str] += 1
            else:
                self.metrics_data.properties_not_adjacent_to_type_qty += 1
        if 'required' in res:
            required_keys = res['required']
            if type(required_keys) is list:
                self.metrics_data.required_usage_qty += 1
                for required_key in required_keys:
                    if required_key not in self.metrics_data.required_key_to_qty:
                        self.metrics_data.required_key_to_qty[required_key] = 0
                    self.metrics_data.required_key_to_qty[required_key] += 1
                if 'type' in res:
                    type_str = str(res['type'])
                    if type_str not in self.metrics_data.required_adjacent_to_type:
                        self.metrics_data.required_adjacent_to_type[type_str] = 0
                    self.metrics_data.required_adjacent_to_type[type_str] += 1
                else:
                    self.metrics_data.required_not_adjacent_to_type_qty += 1                

        return res

    def construct_yaml_seq(self, node):
        # this is needed to load required list at construction time and to not use a generator that is
        # fired later to finish processing
        data = []
        data.extend(self.construct_sequence(node))
        return data


CustomConstructor.add_constructor(
        'tag:yaml.org,2002:seq',
        CustomConstructor.construct_yaml_seq)


class CustomLoader(
    _yaml.CParser,
    CustomConstructor,
    resolver.Resolver):
    # custom class so metrics can be gathered on opeanpi document info

    def __init__(self, stream, metrics_data: MetricsData):
        _yaml.CParser.__init__(self, stream)
        CustomConstructor.__init__(self, metrics_data)
        resolver.Resolver.__init__(self)


def yaml_loading_works(document_path: str, metrics_data: MetricsData) -> bool:
    try:
        with open(document_path, 'r') as file:

            loader = CustomLoader(file, metrics_data)
            try:
                _loaded_data = loader.get_single_data()
            finally:
                loader.dispose()
            return True
    except Exception as exc:
        print (f"Yaml error in file={document_path} error={exc}")
        return False

def filter_and_analyze_documents(document_paths: typing.List[str], metrics_data: MetricsData) -> typing.List[str]:
    filtered_paths: typing.List[str] = []
    for i, document_path in enumerate(document_paths):
        if i % 50 is 0 or i == len(document_paths) - 1:
            print(f"Examining document {i} in filter_and_analyze_documents")
        is_v3_spec = file_contains_3x_spec_version(document_path)
        # print(f"path={document_path} v3={is_v3_spec}")
        if is_v3_spec:
            if yaml_loading_works(document_path, metrics_data):
                filtered_paths.append(document_path)
    return filtered_paths