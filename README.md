# openapi-document-analysis
A repo to analye usage of some keywords in openapi documents

## openapi documents
documents are from https://github.com/APIs-guru/openapi-directory

## env setup
```
python3 -m venv venv
source venv/bin/activate
pip install pyyaml
```

## usage
- `python analyze.py`
    - Outputs md reports and .py files containing required keys and properties keys and qty of usages
    - After this is run, the below analyzers can be run on the generated .py files containing key info
- `python analyze_required_keys.py`
- `python analyze_properties_keys.py`

## Reports
- [properties usage](reports/properties_report.md)
- [required usage](reports/required_report.md)
- [required keys python usage](reports/required_keys_python_report.md)
- [properties keys python usage](reports/properties_keys_python_report.md)