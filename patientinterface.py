import pandas as pd

data_patient = pd.read_csv("patient.csv")

class Patient:
    def __init__(self, id, index):
        self.id = id
        self.index = index
        self.name = data_patient.at[index, "Name"]
        self.Disease = data_patient.at[index, "Disease"]
    
    def info(self):
        patient_appointment = self.appointment()
        info = [self.id, self.name, self.Disease, patient_appointment]
        return info

    def appointment(self):
        list_appointment = [
            data_patient.at[self.index, "Appointment1"],
            data_patient.at[self.index, "Appointment2"],
            data_patient.at[self.index, "Appointment3"],
            data_patient.at[self.index, "Appointment4"],
            data_patient.at[self.index, "Appointment5"],
            data_patient.at[self.index, "Appointment6"],
            data_patient.at[self.index, "Appointment7"]
        ]
        return list_appointment

    def display(self):
        info = self.info()
        print(f"ID: {info[0]}")
        print(f"Name: {info[1]}")
        print(f"Disease: {info[2]}")
        print(f"Appointments: {info[3]}")
      
    def Edit_Personal_info(self):
        edit_p = int(input("What do you want to change? \n 1.Name - Enter 1 \n 2. Disease - Enter 2  \n 3.Both - Enter 3:\t"))
        if edit_p == 1:
            print(f"Your Current Name is {self.name}.\n")
            new_name = input("\nEnter new Name : ")
            data_patient.loc[self.index, "Name"] = new_name
            data_patient.to_csv("patient.csv", index=False)
        elif edit_p == 2:
            print(f"Your current Disease info: {self.Disease}")
            new_disease = input("Enter new Disease :")
            data_patient.loc[self.index, "Disease"] = new_disease
            data_patient.to_csv("patient.csv", index=False)
        elif edit_p == 3:
            update_info = ["Name", "Disease"]
            for field in update_info:
                data_patient.loc[self.index, field] = input(f"Enter the new {field}:\t ")
            data_patient.to_csv("patient.csv", index=False)
            print(f"{self.id} updated successfully.")
        else:
            print("Invalid input")

# id = 21300002
# index_list = data_patient.index[data_patient["Id"] == id].tolist()

# if index_list:
#     index = index_list[0] 
#     patient_obj = Patient(id, index)
# else:
#     print("Patient ID not found")

# Exit = False
# while not Exit:
#     operation = int(input("1.Display  \n2.Edit Personal Info \n3.Exit\n\t\t:\t"))

#     if operation == 1:
#         patient_obj.display()
#     elif operation == 2:
#         patient_obj.Edit_Personal_info()
#     elif operation == 3:
#         print("Thank you for visiting!")
#         Exit = True
#     else:
#         print("Invalid input. Please try again.")
