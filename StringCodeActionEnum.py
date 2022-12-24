from enum import Enum

class StringCodeActionEnum(Enum):
    SPACE = "-"
    ENTER = "|"
    INDENTATION = "#"
    CLASS_ATTRIBUTE = "$"