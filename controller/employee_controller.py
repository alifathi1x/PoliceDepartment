from model.entity.employee_information import EmployeeInformation

class EmployeeController:
    def save(self,id,name,family,checkin_shift,checkout_shift,shift_location):
        try:
            employee = EmployeeInformation(id,name,family,checkin_shift,checkout_shift,shift_location)
            return True, f"employee saved {employee}"
        except Exception as e:
            return False, f"{e}"

    def remove(self,id,name,family,checkin_shift,checkout_shift,shift_location):
        try:
            employee = EmployeeInformation(id,name,family,checkin_shift,checkout_shift,shift_location)
            return True, f"employee removed {employee}"

        except Exception as e:
            return False, f"{e}"


    def find_all(self):
        try:
            return True, f"find all employees"

        except Exception as e:
            return False, f"{e}"
