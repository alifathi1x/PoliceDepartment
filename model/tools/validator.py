import re

def shift_location_validator(shift_location):
    if shift_location == "tehran":
        return shift_location
    else:
        raise ValueError("Invalid shift Location")

def national_id_validator(national_id):
    return re.match(r"^[0-9]{1,10}$", national_id)

def crime_type_validator(crime_type):
    crime_type_list = ["Murder","robbery","hostage"]
    if crime_type == crime_type_list:
        return True
