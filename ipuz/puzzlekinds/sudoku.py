from ipuz.exceptions import IPUZException
from ipuz.structures import (
    validate_calcspec,
    validate_sudokugiven,
    validate_sudokuguess,
    validate_sudokuvalue,
)
from ipuz.validators import validate_bool


def validate_charset(field_name, field_data):
    if type(field_data) not in [str, unicode] or (len(field_data) != 9):
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_cageborder(field_name, field_data):
    if field_data not in ["thick", "dashed"]:
        raise IPUZException("Invalid {} value found".format(field_name))


def validate_cages(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for element in field_data:
        if not validate_calcspec(element):
            raise IPUZException("Invalid CalcSpec in {} element found".format(field_name))


def validate_puzzle(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        if type(line) is not list:
            raise IPUZException("Invalid {} value found".format(field_name))
        for element in line:
            if not validate_sudokugiven(element):
                raise IPUZException("Invalid SudokuGiven in {} element found".format(field_name))
    return True


def validate_saved(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        if type(line) is not list:
            raise IPUZException("Invalid {} value found".format(field_name))
        for element in line:
            if not validate_sudokuguess(element):
                raise IPUZException("Invalid SudokuGuess in {} element found".format(field_name))
    return True


def validate_solution(field_name, field_data):
    if type(field_data) is not list:
        raise IPUZException("Invalid {} value found".format(field_name))
    for line in field_data:
        if type(line) is not list:
            raise IPUZException("Invalid {} value found".format(field_name))
        for element in line:
            if not validate_sudokuvalue(element):
                raise IPUZException("Invalid SudokuValue in {} element found".format(field_name))
    return True


IPUZ_SUDOKU_VALIDATORS = {
    "charset": validate_charset,
    "displaycharset": validate_bool,
    "boxes": validate_bool,
    "showoperators": validate_bool,
    "cageborder": validate_cageborder,
    "puzzle": validate_puzzle,
    "saved": validate_saved,
    "solution": validate_solution,
    "cages": validate_cages,
}
