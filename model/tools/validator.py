import re

def shift_location_validator(shift_location):
    if shift_location == ("tehran","shiraz","esfahan","kish") and re.match("^[a-zA-Z]{2,30}$",shift_location):
        return True
    else:
        raise ValueError("Invalid shift_location")