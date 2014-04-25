from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_clue,
    validate_crosswordvalue,
    validate_direction,
    validate_enumeration,
    validate_groupspec,
    validate_labeledcell,
)
from ipuz.validators import (
    validate_bool,
    validate_dict_of_strings,
)


def validate_dimensions(field_name, field_data):
    for key in ["width", "height"]:
        if key not in field_data:
            raise IPUZException(
                "Mandatory field {} of dimensions is missing".format(key)
            )
        if field_data[key] < 1:
            raise IPUZException(
                "Field {} of dimensions is less than one".format(key)
            )


def validate_puzzle(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_labeledcell(element):
                raise IPUZException("Invalid LabeledCell in {} element found".format(field_name))


def validate_crosswordvalues(field_name, field_data):
    if type(field_data) is not list or any(type(e) is not list for e in field_data):
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        for element in line:
            if not validate_crosswordvalue(element):
                raise IPUZException("Invalid CrosswordValue in {} element found".format(field_name))


def validate_zones(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_groupspec(element):
            raise IPUZException("Invalid GroupSpec in {} element found".format(field_name))


def validate_clueplacement(field_name, field_data):
    if field_data not in [None, "before", "after", "blocks"]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_answer(field_name, field_data):
    if type(field_data) not in [str, unicode] or field_data == "":
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_answers(field_name, field_data):
    if type(field_data) is not list or not field_data:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        try:
            validate_answer(field_name, element)
        except IPUZException:
            raise IPUZException("Invalid {} value found".format(field_name))


def validate_clues(field_name, field_data):
    if type(field_data) is not dict:
        raise IPUZException("Invalid {} value found".format(field_name))
    for direction, clues in field_data.items():
        if not validate_direction(direction) or type(clues) is not list or not clues:
            raise IPUZException("Invalid {} value found".format(field_name))
        for clue in clues:
            if not validate_clue(clue):
                raise IPUZException("Invalid Clue in {} element found".format(field_name))


def validate_enumeration_field(field_name, field_data):
    if not validate_enumeration(field_data):
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_enumerations(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_enumeration(element):
            raise IPUZException("Invalid Enumerations in {} element found".format(field_name))


IPUZ_CROSSWORD_VALIDATORS = {
    "dimensions": validate_dimensions,
    "puzzle": validate_puzzle,
    "saved": validate_crosswordvalues,
    "solution": validate_crosswordvalues,
    "zones": validate_zones,
    "clues": validate_clues,
    "showenumerations": validate_bool,
    "clueplacement": validate_clueplacement,
    "answer": validate_answer,
    "answers": validate_answers,
    "enumeration": validate_enumeration_field,
    "enumerations": validate_enumerations,
    "misses": validate_dict_of_strings,
}
