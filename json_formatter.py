#!/usr/bin/python3

def json_formatter(input) -> str:
    if input is None:
        return 'null'
    elif isinstance(input, list):
        return '[' + ','.join(list(map(json_formatter, input))) + ']'
    elif isinstance(input, dict):
        # same thing as list, but format the key value pairs
        return '{' + ','.join(list(map(key_value_formatter, input.items()))) + '}'
    elif isinstance(input, str):
        return '\'' + input + '\''
    else:
        return str(input)

def key_value_formatter(item) -> str:
    # the key should always be a string. the value can be anything
    return json_formatter(item[0]) + ": " + json_formatter(item[1])

print(json_formatter([None, 123, ["a", "b"], {"c":"d"}, {'asdf': {'foo': 'bar'}}]))
