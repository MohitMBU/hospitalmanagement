import pandas as pd 
import getpass

def read_login():
      with open('login.txt','r') as f:
            contents = f.readlines()
            new_content = []

            for line in contents:
                  flied =line.split(',')
                  flied[1] = flied[1].rstrip()
                  new_content.append(flied)

      return new_content
      

def logins(login):
      for i in range(0,3):
            User_Name = str(input("Enter User Name\t:\t"))
            Password = getpass.getpass("Enter password\t:\t ")
            # Password_hash = str(hash(Password))
            logged_in = False
            for line in login:
                  if line[0] == User_Name and not logged_in:
                        if line[1] == Password:
                              logged_in = True
                              return logged_in
            
            chocies_2 = int(input(("Account Not Found \n 1. Create a Account \n 2. Try to login again")))
            if chocies_2 == 1:
                  create(login)
            elif chocies_2 == 2:
                  logins(login) 
            else:
                  raise Exception("Error invalid input")

                  






def create(login):
      status_create = False 
      User_Name = str(input("Enter User Name\t:\t"))
      Password = getpass.getpass("Enter password\t:\t ")
      Comf_Pass= getpass.getpass("Comform password\t:\t ")
      
      for i in range(0,3):
            if Comf_Pass == Password:
                  New_user = [User_Name,Password]
                  login.append(New_user)
                  status_create = True
                  break
            else:
                  print("Password and Commform Pass has no match Please correct it ")
      if status_create:
            print("Login to Continue futher")
            logins(login)
      else:
             pass






def chocies():
            login_status = False
            login = read_login()
            choice = int(input("1.Login\n2.Create Account"))

            if choice == 1:
                  login_status = logins(login)
                  if login_status : return login_status
                  else:
                        print("Account Not Found Create A Account OR Try Again")
                        create
            
            elif choice == 2:
                  create_status = create(login)
                  if create_status:
                        print("Login to Proceed Futher")
                        login_status = logins(login)
                        return login_status
                        
            else:
                  raise Exception("Enter OPtion is invalid")




login = read_login()
chocies()


 

