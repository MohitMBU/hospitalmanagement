import pandas as pd

def get_appointment(appointments):
    obj = {
        1: "9 am to 10 am",
        2: "10 am to 11 am",
        3: "11 am to 12 pm",
        4: "12 pm to 1 pm",
        5: "2 pm to 3 pm",
        6: "3 pm to 4 pm",
        7: "4 pm to 5 pm"
    }
    for i in range(1, 8):
        if appointments[i - 1] != "Appointment Fix":
            print(f"{i}\t:\t{obj[i]}")
        else:
            print(f"{i}\t:\tAppointment Fix")
    
    Appointment = int(input("Choose the Slot According To Your Need: "))
    if 1 <= Appointment <= 7:
        if appointments[Appointment - 1] != "Appointment Fix":
            appointments[Appointment - 1] = "Appointment Fix"
            print(f"Appointment Fix  for {obj[Appointment]} This Slot ")
        else:
            print("This slot is already booked.")
    else:
        print("Invalid slot selected.")
    return appointments

data_Doctor = pd.read_csv("docter.csv", dtype=str)
print(data_Doctor)

print("\n\n\n****************** Select the Doctor From Which You Want Appointment ******************\n\n\n")

Doctor = input("Enter the Id of doctor: ")

if Doctor in data_Doctor['Id'].values:
    index = data_Doctor.index[data_Doctor['Id'] == Doctor].tolist()[0]
    appointments = [
        data_Doctor.at[index, 'Appointment1'], 
        data_Doctor.at[index, 'Appointment2'], 
        data_Doctor.at[index, 'Appointment3'], 
        data_Doctor.at[index, 'Appointment4'], 
        data_Doctor.at[index, 'Appointment5'], 
        data_Doctor.at[index, 'Appointment6'], 
        data_Doctor.at[index, 'Appointment7']
    ]
    new_appointments = get_appointment(appointments)
    data_Doctor.at[index, 'Appointment1'] = new_appointments[0]
    data_Doctor.at[index, 'Appointment2'] = new_appointments[1]
    data_Doctor.at[index, 'Appointment3'] = new_appointments[2]
    data_Doctor.at[index, 'Appointment4'] = new_appointments[3]
    data_Doctor.at[index, 'Appointment5'] = new_appointments[4]
    data_Doctor.at[index, 'Appointment6'] = new_appointments[5]
    data_Doctor.at[index, 'Appointment7'] = new_appointments[6]
    data_Doctor.to_csv("docter.csv", index=False)
else:
    print("Doctor not found.")
