import typing

from analyzer import report, loader

def write_properties_report(filtered_document_paths: typing.List[str], metrics_data: loader.MetricsData):
    properties_info = report.TableInfo(
        title='General Metrics',
        table_headers=('Metric', 'Qty'),
        table_data=tuple({
            'openapi_documents_qty': len(filtered_document_paths),
            'properties_key_qty': metrics_data.properties_key_qty,
            'properties_adjacent_to_type_qty': len(metrics_data.properties_adjacent_to_type),
            'properties_not_adjacent_to_type_qty': metrics_data.properties_not_adjacent_to_type_qty,
        }.items())
    )
    properties_adjacent_info = report.TableInfo(
        title='Properties Adjacent to Type Metrics',
        table_headers=('Type', 'Qty'),
        table_data=tuple(metrics_data.properties_adjacent_to_type.items())
    )
    properties_report = report.ReportInfo(
        title='Json Schema keyword=properties Usage Info',
        description='Counts number of properties keyword usages. Analyzes keyword=type info adjacent to properties. documents: 3.0.0-3.1.0 yaml specs only',
        table_infos={
            'properties_info': properties_info,
            'properties_adjacent_info': properties_adjacent_info
        }
    )
    with open('reports/properties_report.md', 'wt') as stream:
        properties_report.write(stream)

def write_required_report(filtered_document_paths: typing.List[str], metrics_data: loader.MetricsData):
    required_info = report.TableInfo(
        title='General Metrics',
        table_headers=('Metric', 'Qty'),
        table_data=tuple({
            'openapi_documents_qty': len(filtered_document_paths),
            'required_usage_qty': metrics_data.required_usage_qty,
            'properties_adjacent_to_type_qty': len(metrics_data.required_adjacent_to_type),
            'properties_not_adjacent_to_type_qty': metrics_data.required_not_adjacent_to_type_qty,
        }.items())
    )
    required_adjacent_info = report.TableInfo(
        title='Required Adjacent to Type Metrics',
        table_headers=('Type', 'Qty'),
        table_data=tuple(metrics_data.required_adjacent_to_type.items())
    )
    required_key_info = report.TableInfo(
        title='Required Key to Qty',
        table_headers=('Required Key', 'Qty'),
        table_data=tuple(metrics_data.required_key_to_qty.items())
    )
    required_report = report.ReportInfo(
        title='Json Schema keyword=required Usage Info',
        description='Counts number of required keyword usages. Analyzes keyword=type info adjacent to required. documents: 3.0.0-3.1.0 yaml specs only',
        table_infos={
            'required_info': required_info,
            'required_adjacent_info': required_adjacent_info,
            'required_key_info': required_key_info
        }
    )
    with open('reports/required_report.md', 'wt') as stream:
        required_report.write(stream)

if __name__ == '__main__':
    document_paths = loader.find_document_paths()
    print(f"qty_found_documents={len(document_paths)}")
    metrics_data = loader.MetricsData()
    filtered_document_paths = loader.filter_and_analyze_documents(document_paths, metrics_data)
    print(f"qty_filtered_document_paths={len(filtered_document_paths)}")
    print(f"properties_key_qty={metrics_data.properties_key_qty}")
    print(f"properties_adjacent_to_type={metrics_data.properties_adjacent_to_type}")
    print(f"properties_not_adjacent_to_type_qty={metrics_data.properties_not_adjacent_to_type_qty}")
    print(f"required_usage_qty={metrics_data.required_usage_qty}")
    print(f"required_adjacent_to_type={metrics_data.required_adjacent_to_type}")
    print(f"required_not_adjacent_to_type_qty={metrics_data.required_not_adjacent_to_type_qty}")
    print(f"required_key_to_qty={metrics_data.required_key_to_qty}")

    write_properties_report(filtered_document_paths, metrics_data)
    write_required_report(filtered_document_paths, metrics_data)


