from analyzer import report, loader


if __name__ == '__main__':
    document_paths = loader.find_document_paths()
    print(f"qty_found_documents={len(document_paths)}")
    metrics_data = loader.MetricsData()
    filtered_document_paths = loader.filter_and_analyze_documents(document_paths, metrics_data)
    print(f"qty_filtered_document_paths={len(filtered_document_paths)}")
    print(f"properties_key_qty={metrics_data.properties_key_qty}")
    print(f"properties_adjacent_to_type={metrics_data.properties_adjacent_to_type}")
    print(f"properties_not_adjacent_to_type_qty={metrics_data.properties_not_adjacent_to_type_qty}")
    general_metrics = report.TableInfo(
        title='General Metrics',
        table_headers=('Metric', 'Qty'),
        table_data=tuple({
            'openapi_documents_qty': len(filtered_document_paths),
            'properties_key_qty': metrics_data.properties_key_qty,
            'properties_adjacent_to_type_qty': len(metrics_data.properties_adjacent_to_type),
            'properties_not_adjacent_to_type_qty': metrics_data.properties_not_adjacent_to_type_qty,
        }.items())
    )
    properties_adjacent_metrics = report.TableInfo(
        title='Properties Adjacent to Type Metrics',
        table_headers=('Type', 'Qty'),
        table_data=tuple(metrics_data.properties_adjacent_to_type.items())
    )
    properties_report_info = report.ReportInfo(
        title='Json Schema keyword=properties Usage Info',
        description='Counts number of properties keyword usages. Analyzes keyword=type info adjacent to properties. documents: 3.0.0-3.1.0 yaml specs only',
        table_infos={
            'general_metrics': general_metrics,
            'properties_adjacent_metrics': properties_adjacent_metrics
        }
    )
    with open('reports/properties_report.md', 'wt') as stream:
        properties_report_info.write(stream)
