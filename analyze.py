import mmap
import glob
import typing

import yaml
from yaml import scanner, parser, composer, constructor, resolver, _yaml

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
properties_key_qty = 0
properties_adjacent_to_type = {}
properties_not_adjacent_to_type = 0


class CustomConstructor(constructor.SafeConstructor):
    def construct_mapping(self, node, deep=False):
        res = super().construct_mapping(node, deep=deep)
        if 'properties' in res:
            global properties_key_qty
            properties_key_qty += 1
            global properties_adjacent_to_type, properties_not_adjacent_to_type
            if 'type' in res:
                type_str = str(res['type'])
                if type_str not in properties_adjacent_to_type:
                    properties_adjacent_to_type[type_str] = 0
                properties_adjacent_to_type[type_str] += 1
            else:
                properties_not_adjacent_to_type += 1

        return res


class CustomLoader(
    _yaml.CParser,
    CustomConstructor,
    resolver.Resolver):
    # custom class so metrics can be gathered on opeanpi document info

    def __init__(self, stream):
        _yaml.CParser.__init__(self, stream)
        CustomConstructor.__init__(self)
        resolver.Resolver.__init__(self)


def yaml_loading_works(document_path: str) -> bool:
    try:
        with open(document_path, 'r') as file:
            yaml.load(file, Loader=CustomLoader)
            return True
    except Exception as exc:
        print (f"Yaml error in file={document_path} error={exc}")
        return False

def filter_documents(document_paths: typing.List[str]) -> typing.List[str]:
    filtered_paths: typing.List[str] = []
    for i, document_path in enumerate(document_paths):
        if i % 50 is 0 or i == len(document_paths) - 1:
            print(f"Examining document {i} in filter_documents")
        is_v3_spec = file_contains_3x_spec_version(document_path)
        # print(f"path={document_path} v3={is_v3_spec}")
        if is_v3_spec:
            if yaml_loading_works(document_path):
                filtered_paths.append(document_path)
    return filtered_paths


if __name__ == '__main__':
    document_paths = find_document_paths()
    print(f"qty_found_documents={len(document_paths)}")
    filtered_document_paths = filter_documents(document_paths)
    print(f"qty_filtered_document_paths={len(filtered_document_paths)}")
    print(f"properties_key_qty={properties_key_qty}")
    print(f"properties_adjacent_to_type={properties_adjacent_to_type}")
    print(f"properties_not_adjacent_to_type={properties_not_adjacent_to_type}")