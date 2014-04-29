from datetime import datetime
import re

import six

from ipuz.exceptions import IPUZException


def validate_bool(field_name, field_data):
    if type(field_data) is not bool:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_int(field_name, field_data):
    # type instead of isinstance as bool inherits from int
    if type(field_data) is not int:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_non_negative_int(field_name, field_data):
    if type(field_data) is not int or field_data < 0:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_string(field_name, field_data):
    if not isinstance(field_data, six.string_types):
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_dict_of_strings(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for key, value in field_data.items():
        validate_string(field_name, key)
        validate_string(field_name, value)


def validate_list_of_strings(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        validate_string(field_name, field_data)


def validate_version(field_name, field_data):
    groups = re.match("http://ipuz.org/v([1-9]\d*)", field_data)
    if not groups:
        raise IPUZException("Invalid version value found")
    version_number = int(groups.group(1))
    if version_number > 1:
        raise IPUZException("Unsupported version value found")


def validate_kind(field_name, field_data):
    if type(field_data) is not list or not field_data:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not isinstance(element, six.string_types) or not element:
            raise IPUZException("Invalid {} value found".format(field_name))


def validate_date(field_name, field_data):
    try:
        datetime.strptime(field_data, '%m/%d/%Y')
    except ValueError:
        raise IPUZException("Invalid date format: {}".format(field_data))


def validate_empty(field_name, field_data):
    if type(field_data) is not int and not isinstance(field_data, six.string_types):
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_styles(field_name, field_data):
    from ipuz.structures import validate_stylespec
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for _, stylespec in field_data.items():
        validate_stylespec(stylespec)


IPUZ_FIELD_VALIDATORS = {
    "version": validate_version,
    "kind": validate_kind,
    "copyright": validate_string,
    "publisher": validate_string,
    "publication": validate_string,
    "url": validate_string,
    "uniqueid": validate_string,
    "title": validate_string,
    "intro": validate_string,
    "explanation": validate_string,
    "annotation": validate_string,
    "author": validate_string,
    "editor": validate_string,
    "date": validate_string,
    "notes": validate_string,
    "difficulty": validate_string,
    "origin": validate_string,
    "block": validate_string,
    "empty": validate_empty,
    "date": validate_date,
    "styles": validate_styles,
    "checksum": validate_list_of_strings,
    "volatile": validate_dict_of_strings,
}
