import typing

def get_md_table_colun_lengths(
    table_headers: typing.Tuple[str, ...],
    table_data: typing.Tuple[
        typing.Tuple[typing.Any, ...],
        ...
    ]
) -> typing.Tuple[int, ...]:
    column_sizes = []
    for table_header in table_headers:
        column_sizes.append(len(table_header) + 2)
    for table_row in table_data:
        for i, val in enumerate(table_row):
            val_length = len(str(val)) + 2
            if val_length > column_sizes[i]:
                column_sizes[i] = val_length
    return tuple(column_sizes)

def display_markdown_table(
    table_headers: typing.Tuple[str, ...],
    table_data: typing.Tuple[
        typing.Tuple[typing.Any, ...],
        ...
    ],
    table_column_lengths: typing.Tuple[int, ...]
):
    row: typing.List[str] = ['', '']
    for i, table_header in enumerate(table_headers):
        row.insert(-1, ' '+table_header.ljust(table_column_lengths[i]-1))
    print('|'.join(row))
    row = ['', '']
    for i in table_column_lengths:
        dashes = '-'*(i-2)
        row.insert(-1, dashes.center(i))
    print('|'.join(row))
    for table_row in table_data:
        row = ['', '']
        for i, val in enumerate(table_row):
            row.insert(-1, ' '+str(val).ljust(table_column_lengths[i]-1))
        print('|'.join(row))

def print_markdown_table(
    table_headers: typing.Tuple[str, ...],
    table_data: typing.Tuple[
        typing.Tuple[typing.Any, ...],
        ...
    ],
):
    table_column_lengths = get_md_table_colun_lengths(
        table_headers=table_headers,
        table_data=table_data
    )
    display_markdown_table(
        table_headers,
        table_data,
        table_column_lengths
    )
