from model.entity.prisoner_information import PrisonerInformation

class PrisonerController:
    def save(self,id,name,family,national_id,address,crime_type,crime_location,investigation_report):
        try:
            prisoner = PrisonerInformation(id,name,family,national_id,address,crime_type,crime_location,investigation_report)
            return True, f"prisoner saved {prisoner}"

        except Exception as e:
            return False, f"{e}"


    def remove(self,id,name,family,national_id,address,crime_type,crime_location,investigation_report):
        try:
            prisoner = PrisonerInformation(id,name,family, national_id,address,crime_type,crime_location,investigation_report)
            return True, f"prisoner removed {prisoner}"

        except Exception as e:
            return False, f"{e}"