from datetime import date
from model.tools.validator import *


class EmployeeInformation:
    def __init__(self,id,name,family,checkin_shift,checkout_shift,shift_location):
        self._id = id
        self._name = name
        self._family = family
        self._checkin_shift = checkin_shift
        self._checkout_shift = checkout_shift
        self._shift_location = shift_location

    def __repr__(self):
        return f"{self.__dict__}"

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    def get_family(self):
        return self._family

    def set_family(self, family):
        if isinstance(family,str):
            self._family = family

        else:
            raise ValueError("Invalid Family")

    def get_checkin_shift(self):
        return self._checkin_shift

    def set_checkin_shift(self, checkin_shift):
        if isinstance(checkin_shift,date):
            self._checkin_shift = checkin_shift
        else:
            raise ValueError("Invalid Checkin Shift")

    def get_checkout_shift(self):
        return self._checkout_shift

    def set_checkout_shift(self, checkout_shift):
        if isinstance(checkout_shift,date):
            self._checkout_shift = checkout_shift
        else:
            raise ValueError("Invalid Checkout Shift")

    def get_shift_location(self):
        return self._shift_location

    def set_shift_location(self, shift_location):
        if shift_location_validator(shift_location):
            self._shift_location = shift_location
        else:
            raise ValueError("Invalid Location")


    id = property(get_id,set_id)
    name = property(get_name,set_name)
    family = property(get_family,set_family)
    checkin_shift = property(get_checkin_shift,set_checkin_shift)
    checkout_shift = property(get_checkout_shift,set_checkout_shift)
    shift_location = property(get_shift_location)
