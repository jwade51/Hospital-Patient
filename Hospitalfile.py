def Hospital_tracker(patient, age, status):
    patient= input( " Please type in patient's name:")
    age= int(input("Please enter the patient's age:"))
    status= bool(input("Is this a new or an old patient? (True for new, False for old):"))
    
    return(patient,age,status)

def display_info(patient, age, status): #function to display the information entered by the user.
    print("\nPatient Name : ", patient) #printing the patient's name 
    print("Age           : ", age)       #printing the patient's age
    if status == True:     #if the patient is new then it will show 'New Patient' otherwise 'Old Patient'.
        print('Status         : New' ) #New Patient
        print("Status: New")
    else:
        print("Status: Old")
        
# Main Program
print ("Welcome to the hospital tracker! \n\n")  

name, age, stat = Hospital_tracker('',0,False) 
display_info(name, age, stat)  #calling the function to display the information entered by the user


