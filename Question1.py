''' 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
--> Each employee information consists of Name, DOB, Height, City, State. 
--> Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
--> Finally print the list of the Employee objects.
'''

import json

with open("C:\\Users\\VIVEK\\Documents\\Edyoda Assignments\\Assignment6\\Assignment1\\employee.json") as file:

    class Employee:
        def data(self):
            return json.load(file)                               # Using "load" to read the data of json file

    obj = Employee()
    print(obj.data())



# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

dictionary = [{"Andhra Pradesh": "Vishakapatnam"},{"Arunachal Pradesh":"Itanagar"},{"Assam":"Dispur"},{"Bihar": "Patna"},{"Chhattisgarh":"Raipur"},{"Goa":"Panaji"},{"Gujrat":"Gandhinagar"}]

with open("Edyoda dict.json","w+") as file1:
    json.dump(dictionary,file1)                                    # Using "dump" to wite data into json file 
    print("Succefully added dictionary into json file.")