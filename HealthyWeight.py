import json
def LoadSetupData():
    with open('HealthyWight.json') as data_file:
        inputs = json.load(data_file)
def AskForName():
    username=input("Hello ! Can you please write a username made from numbers and letters only?" , "/n" , "Note:It should be no less than 3 characters : )")
    password= input( "Please enter a password, no less than 8 characters.")
    return username
    return password
    if len(username) <3:
        print("Note:It should be no less than 3 characters : ), Please try again.")
    if len(password) <8:
         print("Note:It should be no less than 8 characters : ), Please try again.")
    inputs["InitialData"]["usrname"]= username
    inputs["InitialData"]["password"]=password
AskForName()


