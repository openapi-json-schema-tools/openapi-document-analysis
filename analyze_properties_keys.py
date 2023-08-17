from extracted_key_data_v3specs import properties_key_to_qty as properties_key_to_qty_module
from language_info import python, mapping_key_language_info

from analyzer import report


def write_python_report(language_info: mapping_key_language_info.MappingKeyLanguagInfo):
    general_info = report.TableInfo(
        title='Key Information',
        table_headers=('Metric', 'Qty'),
        table_data=tuple({
            'qty_keys': language_info.unique_keys,
            'case_insensitieve_collisions_qty': len(language_info.case_insensitieve_collisions),
            'invalid_identifiers_qty': len(language_info.invalid_identifiers),
        }.items())
    )
    case_insensitieve_collisions_info = report.TableInfo(
        title='Reserved Word Identifiers Info',
        table_headers=('Original Key', 'Reserved Word'),
        table_data=tuple(language_info.case_insensitieve_collisions.items())
    )
    invalid_identifiers_info = report.TableInfo(
        title='Invalid Identifiers Info',
        table_headers=('Original Key', 'Fixed Identifier'),
        table_data=tuple(language_info.invalid_identifiers.items())
    )

    this_report = report.ReportInfo(
        title='Properties Key Info',
        description='Checks if mapping property keys are reserved words or would ave invalid getter names',
        table_infos={
            'general_info': general_info,
            'case_insensitieve_collisions_info': case_insensitieve_collisions_info,
            'invalid_identifiers_info': invalid_identifiers_info,
        }
    )
    with open('reports/properties_keys_python_report.md', 'wt') as stream:
        this_report.write(stream)

if __name__ == '__main__':
    properties_key_to_qty = properties_key_to_qty_module.data
    qty_key_usages = 0

    language_info = mapping_key_language_info.MappingKeyLanguagInfo(
        unique_keys=len(properties_key_to_qty)
    )
    for key, usage_qty in properties_key_to_qty.items():
        qty_key_usages += usage_qty

        getter_method = python.get_getter_method(key, language_info)        
        python.check_identifier(getter_method)

    print(language_info)
    write_python_report(language_info)
