from model.tools.validator import *

class PrisonerInformation:
    def __init__(self,id,name,family,national_id,address,crime_type,crime_location,investigation_report):
        self._id = id
        self._name = name
        self._family = family
        self._national_id = national_id
        self._address = address
        self._crime_type = crime_type
        self._crime_location = crime_location
        self._investigation_report = investigation_report

    def __repr__(self):
        return f"{self.__dict__}"

    def get_id(self):
        return self._id
    def set_id(self,id):
        if isinstance(id,int):
            self._id = id
        else:
            raise ValueError("Invalid id type")

    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name,str):
            self._name = name
        else:
            raise ValueError("Invalid name")

    def get_family(self):
        return self._family
    def set_family(self, family):
        if isinstance(family,str):
            self._family = family
        else:
            raise ValueError("Invalid family")

    def get_national_id(self):
        return self._national_id
    def set_national_id(self, national_id):
        if national_id_validator(national_id):
            self._national_id = national_id
        else:
            raise ValueError("Invalid national id")

    def get_address(self):
        return self._address

    def set_address(self,address):
        if isinstance(address,str):
            self._address = address
        else:
            raise ValueError("Invalid address")


    def get_crime_type(self):
        return self._crime_type

    def set_crime_type(self,crime_type):
        if crime_type_validator(crime_type):
            self._crime_type = crime_type
        else:
            raise ValueError("Invalid crime_type")


    def get_crime_location(self):
        return self._crime_location

    def set_crime_location(self,crime_location):
        if isinstance(crime_location,str):
            self._crime_location = crime_location

        else:
            raise ValueError("Invalid location")

    def get_investigation_report(self):
        return self._investigation_report

    def set_investigation_report(self,investigation_report):
        if isinstance(investigation_report,str):
            self._investigation_report = investigation_report

        else:
            raise ValueError("Invalid investigation_report")


    id = property(get_id,set_id)
    name = property(get_name,set_name)
    family = property(get_family,set_family)
    national_id = property(get_national_id,set_national_id)
    address = property(get_address,set_address)
    crime_type = property(get_crime_type,set_crime_type)
    crime_location = property(get_crime_location,set_crime_location)
    investigation_report = property(get_investigation_report,set_investigation_report)
