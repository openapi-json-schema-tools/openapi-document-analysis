from . import mapping_key_language_info

reserved_words = {
    "property",  # decorator
    "and", "del", "from", "not", "while", "as", "elif", "global", "or", "with", # python reserved words
    "assert", "else", "if", "pass", "yield", "break", "except", "import",
    "print", "class", "exec", "in", "raise", "continue", "finally", "is",
    "return", "def", "for", "lambda", "try", "self", "nonlocal", "None", "True",
    "False", "async", "await",
    "float", "int", "str", "bool", "dict", "immutabledict", "list", "tuple"  # types
}

def get_getter_method(key: str, language_info: mapping_key_language_info.MappingKeyLanguagInfo):
    if isinstance(key, bool):
        used_key = str(key)
    else:
        used_key = key
    if used_key.lower() in reserved_words:
        print(used_key)
        language_info.case_insensitieve_collisions[used_key] = used_key.lower()

    updated_key = "get_" + used_key.lower()
    if updated_key.isidentifier():
        return updated_key

    final_key = ''
    for char in updated_key:
        if char.isidentifier():
            final_key += char
            continue
        # not valid identifier
        if char.isdigit():
            final_key += char
            continue
        final_key += '_'
    language_info.invalid_identifiers[used_key] = final_key
    print(f"{used_key} -> {final_key}")
    return final_key


def check_identifier(identifier: str):
    if not identifier.isidentifier():
        raise ValueError('{!r} is not a valid parameter name'.format(identifier))


"""
Note: the get_ prefx + lower case fixes these colisions

Reserved words that are used:
('self', 609)
('list', 34)
('from', 629)
('Self', 4)
('class', 8)
('continue', 3)
('yield', 2)
('break', 2)
('int', 1)
('From', 11)
('in', 2)
('return', 1)
('global', 2)
('Property', 2)
('property', 4)
('Lambda', 1)
('List', 2)
--------
Python Reserved Work Collision?
17 out of 21,431 required keys
- can be fixed with get_ prefix

Invalid method name in python?
293 out of 21,431 -> 1.3%
"""