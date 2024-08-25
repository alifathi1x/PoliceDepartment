from model.entity.employee_information import EmployeeInformation
from datetime import datetime

date1 = datetime.now()
date2 = datetime.now()

employee = EmployeeInformation(1,"ali","abolfathi",date1,date2,"shirz")
print(employee)