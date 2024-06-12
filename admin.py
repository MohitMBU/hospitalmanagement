#here Admin can add new patient and doctor 
import pandas as pd

#Creation of variable

Var_1 = "Doctor"
Var_2 = "Patient"


def add(data, filename, id_of_person, add_fields):
    new_entry = {}      
    new_entry[id_of_person] = Id_Genrator(len(data,filename))
    print(f"Id of This Person Will be {new_entry[id_of_person]}")
    for field in add_fields:
        new_entry[field] = input(f"Enter {field}: ")
    
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    data.to_csv(filename, index=False)
    print("New entry added successfully.")


def Id_Genrator(data_length,filename):
      Num = data_length + 1
      if filename == 'Doctor.csv':
            Id = 61230000 + Num
      else:
            Id  = 21300000  + Num
      return Id



Exit = False
while(not Exit):
      choices = int(input(f"Add Imformation about \n1.{Var_1} \n2.{Var_2}\n3.Exit\n\n\t\t\t\t:\t"))
      if choices == 1:
            filename = 'Doctor.csv'
            data = pd.read_csv(filename)
            id_of_person = 'Id'
            fields = ['Name', 'Specialization']
            add(data, filename, id_of_person, fields)

      elif choices == 2:
            filename = 'patient.csv'
            data = pd.read_csv(filename)
            id_of_person = 'Id'
            fields = ['Name', 'Disease']
            add(data, filename, id_of_person, fields,choices)
      elif choices == 3:
            print("Thanks...!")
            Exit = True
      else:
            print("You have Entered Wrong choices of number \n Please try again...!")
