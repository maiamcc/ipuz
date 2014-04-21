import json

from exceptions import IPUZException


IPUZ_MANDATORY_FIELDS = (
    "version",
    "kind",
)


def read(data):
    if data.endswith(')'):
        data = data[data.index('(') + 1:-1]
    try:
        json_data = json.loads(data)
    except ValueError:
        raise IPUZException("No valid JSON could be found")

    for field in IPUZ_MANDATORY_FIELDS:
        if field not in json_data:
            raise IPUZException("Mandatory field {} is missing".format(field))

    return json_data


def write(data, json_only=False):
    json_string = json.dumps(data)
    if json_only:
        return json_string
    return ''.join(['ipuz(', json_string, ')'])
