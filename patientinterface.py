import pandas as pd

def edit(data, filename, id_of_person, update_imfo):
    id_to_edit = input(f"Enter the {id_of_person} you want to edit: ")
    updates = {}
    
    for field in update_imfo:
        updates[field] = input(f"Enter the new {field}: ")
        
    index = data.index[data[id_of_person] == id_to_edit].tolist()
    
    if index:
        for field in update_imfo:
            data.loc[index, field] = updates[field]
        data.to_csv(filename, index=False)
        print(f"{id_of_person} updated successfully.")
    else:
        print(f"{id_of_person} not found.")

def add(data, filename, id_of_person, add_fields):
    new_entry = {}
    
    new_entry[id_of_person] = input(f"Enter {id_of_person}: ")
    for field in add_fields:
        new_entry[field] = input(f"Enter {field}: ")
    
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    data.to_csv(filename, index=False)
    print("New entry added successfully.")

def display(data):
    print(data)

def decision(data, filename, id_of_person, fields):
    operation = int(input("1. Edit info\n2. Add info\n3. Display info\nChoose an operation: "))
    if operation == 1:
        edit(data, filename, id_of_person, fields)
    elif operation == 2:
        add(data, filename, id_of_person, fields)
    elif operation == 3:
        display(data)
    else:
        print("Invalid operation.")




option = int(input("1. Doctor\n2. Patient\n3. Appointment\nChoose an option: "))
    
if option == 1:
      filename = 'docter.csv'
      id_of_person = 'Id'
      fields = ['Name', 'Specialization']
elif option == 2:
      filename = 'patient.csv'
      id_of_person = 'Id'
      fields = ['Name', 'Disease']
elif option == 3:
      filename = 'appointment.csv'

else:
      print("Invalid option.")

    
data = pd.read_csv(filename, dtype=str)
decision(data, filename, id_of_person, fields)

