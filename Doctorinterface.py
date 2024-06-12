import pandas as pd


data_doctor = pd.read_csv("Doctor.csv")

class Doctor:
      def __init__(self, id, index):
        self.id = id
        self.index = index
        self.name = data_doctor.at[index, "Name"]
        self.specialization = data_doctor.at[index, "Specialization"]
    
    
      def info(self):
        doctor_appointment = self.appointment()
        info = [self.id, self.name, self.specialization, doctor_appointment]
        return info

      def appointment(self):
        list_appointment = [
            data_doctor.at[self.index, "Appointment1"],
            data_doctor.at[self.index, "Appointment2"],
            data_doctor.at[self.index, "Appointment3"],
            data_doctor.at[self.index, "Appointment4"],
            data_doctor.at[self.index, "Appointment5"],
            data_doctor.at[self.index, "Appointment6"],
            data_doctor.at[self.index, "Appointment7"]
        ]
        return list_appointment

      def display(self):
        info = self.info()
        print(f"ID: {info[0]}")
        print(f"Name: {info[1]}")
        print(f"Specialization: {info[2]}")
        print(f"Appointments: {info[3]}")
      
      def Edit_Personal_imfo(self):
            update_imfo = ["Name","Specialization"]
            updates = {}

    
            for field in update_imfo:
                  updates[field] = input(f"Enter the new {field}:\t ")
        
            for field in update_imfo:
                  data_doctor.loc[self.index, field] = updates[field]
            data_doctor.to_csv("Doctor.csv", index=False)
            print(f"{self.id} updated successfully.")

      def Edit_Appointment(self):
            update_imfo = ["Appointment1","Appointment2","Appointment3","Appointment4","Appointment5","Appointment6","Appointment7"]
            update = {}

            for field in update_imfo:
                update_imfo= input(f"Enter the Status of {field} :\t")
                update[field] = update_imfo.upper()
            
 
            for field in update_imfo:
                  data_doctor.loc[self.index, field] = update[field]

            
            data_doctor.to_csv("Doctor.csv", index=False)
            print(f"{self.id} updated successfully.")
          
         
        
        


# id = 61230002
# index_list = data_doctor.index[data_doctor["Id"] == id].tolist()

# if index_list:
#     index = index_list[0] 
#     doctor = Doctor(id, index)
# else:
#     print("Doctor ID not found")
# Exit = False
# while(not Exit):
#       opreation = int(input("1.Display \n2.Edit_Appointment \n3.Edit_Personal_Imfo \n4.Exit\n\t\t:\t"))

#       if opreation == 1:
#             doctor.display()
#       elif opreation == 2:
#             doctor.Edit_Appointment()
#       elif opreation == 3:
#             doctor.Edit_Personal_imfo()
#       elif opreation == 4:
#             print("Thanks You Visting.....!")
#             Exit = True
#       else:
#            print("you Enter Worng Number\n Don't Worrie Try Again")
