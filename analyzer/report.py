import dataclasses
import io
import typing

from . import markdown


@dataclasses.dataclass
class TableInfo:
    title: str
    table_headers: typing.Tuple[str, ...]
    table_data: typing.Tuple[typing.Tuple[typing.Any, ...], ...]



@dataclasses.dataclass
class ReportInfo:
    title: str
    description: str
    table_infos: typing.Optional[typing.Dict[str, TableInfo]] = None

    def write(self, stream: io.TextIOWrapper):
        stream.write(f"# {self.title}\n")
        stream.write("\n")
        stream.write(self.description+'\n')
        stream.write("\n")
        if self.table_infos:
            for _table_key, table_info in self.table_infos.items():
                stream.write(f"## {table_info.title}\n")
                markdown.render_table(
                    table_info.table_headers,
                    table_info.table_data,
                    stream
                )

