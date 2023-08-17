# Json Schema keyword=properties Usage Info

Counts number of properties keyword usages. Analyzes keyword=type info adjacent to properties. documents: 3.0.0-3.1.0 yaml specs only

## General Metrics
| Metric                              | Qty    |
| ----------------------------------- | ------ |
| properties_key_qty                  | 191278 |
| properties_adjacent_to_type_qty     | 183722 |
| properties_not_adjacent_to_type_qty | 7556   |
| openapi_documents_qty               | 1857   |
## Properties Adjacent to Type Metrics
| Type                                                                                                                                                                                         | Qty    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| object                                                                                                                                                                                       | 182100 |
| {'description': 'Indication of the type of message.\nSee [the general documentation for more information](./#section/Response/Messages)', 'example': 'BrokenBusinessRule', 'type': 'string'} | 814    |
| {'description': 'Indication of the type of message.\nSee [the general documentation for more information](./#section/Response/Messages)', 'example': 'Warning', 'type': 'string'}            | 501    |
| Feature                                                                                                                                                                                      | 83     |
| ['object', 'null']                                                                                                                                                                           | 55     |
| array                                                                                                                                                                                        | 44     |
| Warning                                                                                                                                                                                      | 24     |
| string                                                                                                                                                                                       | 18     |
| {'description': 'Required. Entity type from a schema e.g. `Address`.', 'type': 'string'}                                                                                                     | 9      |
| {'type': 'string'}                                                                                                                                                                           | 7      |
| {'description': 'Log type.\n', 'enum': ['event', 'page', 'start_session', 'error', 'push_installation', 'start_service', 'custom_properties'], 'type': 'string'}                             | 6      |
| blob                                                                                                                                                                                         | 6      |
| {'$ref': '#/components/schemas/ArtifactType', 'description': ''}                                                                                                                             | 5      |
| name                                                                                                                                                                                         | 4      |
| {'description': 'Log type.\n', 'enum': ['event', 'page', 'start_session', 'error', 'start_service', 'custom_properties'], 'type': 'string'}                                                  | 3      |
| AVRO                                                                                                                                                                                         | 3      |
| {'enum': ['Feature'], 'type': 'string'}                                                                                                                                                      | 3      |
| {'description': 'Output only. The type of the resource, for example `compute.v1.instance`, or `cloudfunctions.v1beta1.function`.', 'type': 'string'}                                         | 3      |
| SpecActivity                                                                                                                                                                                 | 3      |
| {'allOf': [{'$ref': '#/components/schemas/Name'}, {'description': 'The type of the composite model. For alarm composite models, this type is <code>AWS/ALARM</code>.'}]}                     | 3      |
| PROTOBUF                                                                                                                                                                                     | 2      |
| {'nullable': True, 'type': 'string'}                                                                                                                                                         | 2      |
| PullRequestActivity                                                                                                                                                                          | 2      |
| CustomActivity                                                                                                                                                                               | 2      |
| DiscordMessageSentActivity                                                                                                                                                                   | 2      |
| {'$ref': '#/components/schemas/PushOption/definitions/pushOptionType'}                                                                                                                       | 2      |
| String                                                                                                                                                                                       | 2      |
| {'description': 'The custom object definition type. Can only be `object` currently.', 'enum': ['object'], 'type': 'string'}                                                                  | 1      |
| {'$ref': '#/components/schemas/NodeType'}                                                                                                                                                    | 1      |
| {'default': 'Feature', 'type': 'string'}                                                                                                                                                     | 1      |
| {'description': 'Not used by Apigee.', 'enum': ['TYPE_UNSPECIFIED', 'TYPE_TRIAL', 'TYPE_PAID', 'TYPE_INTERNAL'], 'type': 'string'}                                                           | 1      |
| {'description': 'The value type for this schema. A list of values can be found here: http://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1', 'type': 'string'}                     | 1      |
| {'description': 'Top level category describing the type of facility.', 'enum': ['Feature'], 'example': 'Feature', 'type': 'string'}                                                          | 1      |
| {'$ref': '#/components/schemas/BeezUP.Common.ParameterType'}                                                                                                                                 | 1      |
| IssueActivity                                                                                                                                                                                | 1      |
| GithubActivity                                                                                                                                                                               | 1      |
| {'description': 'type of primitive', 'type': 'string'}                                                                                                                                       | 1      |
| {'description': 'Schema type.', 'example': 'object', 'type': 'string'}                                                                                                                       | 1      |
| {'allOf': [{'$ref': '#/components/schemas/ProxyConfigurationType'}, {'description': 'The proxy type. The only supported value is <code>APPMESH</code>.'}]}                                   | 1      |
| {'description': 'The type of ID', 'enum': ['GUID', 'ROUTING_COLLECTION', 'LOGISTIC_COLLECTION', 'LABELLED_COLLECTION'], 'readOnly': True, 'type': 'string'}                                  | 1      |
| {'enum': ['Feature'], 'example': 'Feature', 'type': 'string'}                                                                                                                                | 1      |
