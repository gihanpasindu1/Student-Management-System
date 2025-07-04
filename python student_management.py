#variable initialize
ChoiceNum=0
NICs=0
Stud_IDs=0
Ph_Numbers=0
BirthDates=0
TutGroups=0
Centres=0
Fname=""
Lname=""
Addresses=""
StudentID=[]
StudentNIC=[]
BirthDate=[]
PhoneNumber=[]
TutGroup=[]
Centre=[]
Address=[]
FirstName=[]
LastName=[]
indexes1=[]
commen_indexs=[]
Centres_indexes=[]
tutgroups_index=[]
attend_dates=[]
attendance={}


#main menu

print("                IIT Campus             ")
print()
print("                Main Menu            ")
print()
print("1. Enroll a new student")
print("2. View details of a student")
print("3. View details of all the students according to the branch")
print("4. Update student details")
print("5. Mark attendance")
print("6. View attendance")
print("7. Exit")

#taking user input number

ChoiceNum=int(input("                            Your Choice :"))
print()

while True:


##ADDING A NE STUDENT 

    if ChoiceNum==1:
            print()
            print("                     IIT Campus             ")
            print()
            print("                Enroll a new student           ")
            print()
#getting student ID and checking it correct or not 
            while True:
                Stud_IDs=str(input("Student ID                         -  "))
                if len(Stud_IDs)==9 and Stud_IDs.isdigit():
                    Stud_IDs=Stud_IDs
                    break
                    
                else:
                    print("Please Enter 9 Digits Student ID")
                    
                
#getting student NIC and checking it correct or not 
        
            while True:
                NICs=str(input("NICs                               -  "))
                if len(NICs)==10:
                    NICs=NICs
                    break
                    
                else:
                    print("Please Enter Valid NICs")
                                

#getting student First Name

            while True:
                Fname=str(input("First Name                         -  "))
                if len(Fname)<=10 and Fname.isalpha():
                    Fname==Fname
                    break
                    
                else:
                    print("Enter Valid Name")

#getting student Last Name

            while True:
                Lname=str(input("Last Name                          -  "))
                if len(Lname)<=15 and Lname.isalpha():
                    Lname=Lname
                    break
                    
                else:
                    print("Enter Valid Name")

                
#getting student Birth Date

            BirthDates=str(input("Birth Date                         -  "))
        
#getting student address

            while True:
                Addresses=str(input("Permanent Address                  -  "))
                if len(Addresses)<=15 :
                    Addresses=Addresses
                    break
                    
                else:
                    print("Enter Valid Address")
            
#getting student phone number and check it valid or not

            while True:
                Ph_Numbers=str(input("Phone Number                       -  "))
                if len(Ph_Numbers)==10 and Ph_Numbers.isdigit():
                    Ph_Numbers=Ph_Numbers
                    break
                    
                else:
                    print("Please Enter Valid Phone Number")
                                



#getting student group            

            TutGroups=str(input("Tutorial Group                     -  "))

#getting student center            

            Centres=str(input("Center                             -  "))
            
           


            #print(StudentID,StudentNIC,FirstName,LastName,Address,PhoneNumber,TutGroup,Centre)
            while True:
                save=str(input("Do you want to save the details (yes/no)? :"))
                print()

                if save=="yes":
                
#saving student details

                    StudentID.append(Stud_IDs)
                    StudentNIC.append(NICs)
                    FirstName.append(Fname)
                    LastName.append(Lname)
                    BirthDate.append(BirthDates)
                    Address.append(Addresses)
                    PhoneNumber.append(Ph_Numbers)
                    TutGroup.append(TutGroups)
                    Centre.append(Centres)

                    print("==========Student details saved===========")
                    print()
                    print()
#again printing main menu
                    print("                IIT Campus             ")
                    print()
                    print("                Main Menu            ")
                    print()
                    print("1. Enroll a new student")
                    print("2. View details of a student")
                    print("3. View details of all the students according to the branch")
                    print("4. Update student details")
                    print("5. Mark attendance")
                    print("6. View attendance")
                    print("7. Exit")

                    # Taking user input number
                    ChoiceNum = int(input("                            Your Choice :"))
                    print()
                    break
                    

                elif save=="no":

                    print("Student details NOT saved")
                    print()
                    print("                IIT Campus             ")
                    print()
                    print("                Main Menu            ")
                    print()
                    print("1. Enroll a new student")
                    print("2. View details of a student")
                    print("3. View details of all the students according to the branch")
                    print("4. Update student details")
                    print("5. Mark attendance")
                    print("6. View attendance")
                    print("7. Exit")

                    #taking user input number

                    ChoiceNum=int(input("                            Your Choice :"))
                    print()

                    print()
                    print()
                
                    ## ADD MAIN MENU HERE
                    break
                else:
                    print("please use only lowercase letters")
                   


            
                #print(StudentID,StudentNIC,FirstName,LastName,Address,PhoneNumber,TutGroup,Centre)
                
                
            
                
            
## VIEW DETAILS OF  A STUDENT

    elif ChoiceNum==2:

            print("                     IIT Campus             ")
            print()
            print("                View details of a students           ")
            print()
            while True:
                Stud_IDs=str(input("Student ID                          -  "))
                
                if len(Stud_IDs)==9 and Stud_IDs.isdigit():
                    
                    if Stud_IDs in StudentID:
                        IndexNo=StudentID.index(Stud_IDs)
                        print()
                        print("NICs                               -  ",StudentNIC[IndexNo])
                        print("Phone Number                       -  ",PhoneNumber[IndexNo])
                        print("First Name                         -  ",FirstName[IndexNo])
                        print("Last Name                          -  ",LastName[IndexNo])
                        print("Tutorial Group                     -  ",TutGroup[IndexNo])
                        print("Center                             -  ",Centre[IndexNo])
                        print()
                        
                        

                        save=str(input("Do you want to view another student’s details (yes/no)?"))
                        print()
                        
                        

                        if save=="yes":
                            print()
                            
                            
                                
                        elif save=="no":
#printing main mene again
                            print()
                            print("                IIT Campus             ")
                            print()
                            print("                Main Menu            ")
                            print()
                            print("1. Enroll a new student")
                            print("2. View details of a student")
                            print("3. View details of all the students according to the branch")
                            print("4. Update student details")
                            print("5. Mark attendance")
                            print("6. View attendance")
                            print("7. Exit")

                            # Taking user input number
                            ChoiceNum = int(input("                            Your Choice :"))
                            print()
                            break
                                                    
                        
                        else:
                            print("enter yes or no (in lowercase letters)")
                        
                    else:
                        print()
                        print(" This student is not in the database ")
                        print()
                else:
                    print()
                    print("Enter a valid student ID ")
                    print()
                                              
## VIEW DETAILS OF THE STUDENTS ACCORDING TO THE BRANCH


    elif ChoiceNum==3:
        
            print("                IIT Campus             ")
            print()
            print("      View details of all the students            ")
            print()  
            while True:
                Centres = input("Branch Name                -  ")
                indexes1 = []  

                found = False  

                for i in range(len(Centre)):
                    if Centre[i] == Centres:
                        found = True
                        indexes1.append(i)

                if found:
                    print("\nNIC                   Student ID                First Name               Last Name          Tut Group")
                    print()
                    
                    for num in indexes1:
                        print(StudentNIC[num], "          ", StudentID[num], "               ", FirstName[num], "                        ", LastName[num], "                   ", TutGroup[num])
                        print()
                    save=str(input("Do you want to update student details (yes/no)?"))
                    
                    if save=="yes":
                        ChoiceNum=4
                        break
                    elif save== "no":
                        print()
                        print("                IIT Campus             ")
                        print()
                        print("                Main Menu            ")
                        print()
                        print("1. Enroll a new student")
                        print("2. View details of a student")
                        print("3. View details of all the students according to the branch")
                        print("4. Update student details")
                        print("5. Mark attendance")
                        print("6. View attendance")
                        print("7. Exit")

                        # Taking user input number
                        ChoiceNum = int(input("                            Your Choice :"))
                        print()
                        break 
                    else:
                        print("Please enter 'kurunagala', 'galle', or 'colombo'")
                        
                else:
                    print("Please enter 'kurunagala', 'galle', or 'colombo'")
            


    elif ChoiceNum==4:
        
            print("                     IIT Campus             ")
            print()
            print("                Update Student Details           ")
            print()
            while True:
                Stud_IDs=str(input("Student ID                         -  "))
                if Stud_IDs in StudentID:
                    IndexNo=StudentID.index(Stud_IDs)
                    while True:
                        NICs=str(input("NICs                               -  "))
                        if len(NICs)==10:
                            NICs=NICs
                            break
                            
                        else:
                            print("Please Enter Valid NICs")
                                        

        #getting student First  Name again

                    while True:
                        Fname=str(input("First Name                         -  "))
                        if len(Fname)<=10 and Fname.isalpha():
                            Fname==Fname
                            break
                            
                        else:
                            print("Enter Valid Name")

        #getting student Last Name again

                    while True:
                        Lname=str(input("Last Name                          -  "))
                        if len(Lname)<=15 and Lname.isalpha():
                            Lname=Lname
                            break
                            
                        else:
                            print("Enter Valid Name")

                        
        #getting student Birth Date again

                    BirthDates=str(input("Birth Date                         -  "))
                
        #getting student address

                    while True:
                        Addresses=str(input("Permanent Address                  -  "))
                        if len(Addresses)<=15 :
                            Addresses=Addresses
                            break
                            
                        else:
                            print("Enter Valid Address")
                    
        #getting student phone number and check it valid or not

                    while True:
                        Ph_Numbers=str(input("Phone Number                       -  "))
                        if len(Ph_Numbers)==10 and Ph_Numbers.isdigit():
                            Ph_Numbers=Ph_Numbers
                            break
                            
                        else:
                            print("Please Enter Valid Phone Number")
                                        



        #getting student group            

                    TutGroups=str(input("Tutorial Group                     -  "))

        #getting student center            

                    Centres=str(input("Center                             -  "))

                    while True:
                        save=str(input("Do you want to save new details (yes/no)? :"))
                        print()

                        if save=="yes":
                        
        #saving student details

                            StudentID[IndexNo]=Stud_IDs
                            StudentNIC[IndexNo]=NICs
                            FirstName[IndexNo]=Fname
                            LastName[IndexNo]=Lname
                            BirthDate[IndexNo]=BirthDates
                            Address[IndexNo]=Addresses
                            PhoneNumber[IndexNo]=Ph_Numbers
                            TutGroup[IndexNo]=TutGroups
                            Centre[IndexNo]=Centres

                            print("==========Student details updated===========")
                            print()
                            print()
        #again printing main menu
                            print("                IIT Campus             ")
                            print()
                            print("                Main Menu            ")
                            print()
                            print("1. Enroll a new student")
                            print("2. View details of a student")
                            print("3. View details of all the students according to the branch")
                            print("4. Update student details")
                            print("5. Mark attendance")
                            print("6. View attendance")
                            print("7. Exit")

                            # Taking user input number
                            ChoiceNum = int(input("                            Your Choice :"))
                            print()
                            break
                            

                        elif save=="no":

                            print("Student details NOT saved")
                            print("                IIT Campus             ")
                            print()
                            print("                Main Menu            ")
                            print()
                            print("1. Enroll a new student")
                            print("2. View details of a student")
                            print("3. View details of all the students according to the branch")
                            print("4. Update student details")
                            print("5. Mark attendance")
                            print("6. View attendance")
                            print("7. Exit")

                            #taking user input number

                            ChoiceNum=int(input("                            Your Choice :"))
                            print()

                            print()
                            print()
                        
                            ## ADD MAIN MENU HERE
                            break
                        else:
                            print("please use only lowercase letters")
                    
                


                    break
                else:
                    print("enter valid student id or this student not in database")

                
    elif ChoiceNum==5:
                    Centres_indexes=[]
                    tutgroups_index=[]
                    found=False
                    print("                IIT Campus             ")
                    print()
                    print("               Mark attendance           ")
                    print()
                    
                    while True:
                        Centres=str(input("Center               -    "))
                        if len(Centres)==0:
                            print("please enter center")
                        else:
                            break
                    while True:
                        TutGroups=str(input("Tutorial Group       -       "))
                        if len(TutGroups)==0:
                            print("please enter group")
                        else:
                            break
                    while True:   
                            
                        dates=str(input("Date           -         "))
                        if len(dates)==0:
                            print("please enter date")
                        else:
                            break
            
                    print()
                    print("Student ID           Absent/present")
                    print()

                    for i in range(len(StudentID)):
                        if Centre[i] == Centres and TutGroup[i] == TutGroups:
                            commen_indexs.append(i)

                    if len(commen_indexs) == 0:
                        
                        print()
                        print("No students found for the specified center and tutorial group.")
                        print()

                    else:
                        
                        for i in commen_indexs:
                        
                            
                            mark=input(StudentID[i]+"           ")
                            
                            if StudentID[i] in attendance:
                                attendance[StudentID[i]][dates] = mark
                            else:
                                attendance[StudentID[i]] = {dates: mark}

                        print()
                        while True:
                            save=str(input("Do you want to save new details (yes/no)? :"))
                            print()

                            if save=="yes":
                                
                                print("                IIT Campus             ")
                                print()
                                print("                Main Menu            ")
                                print()
                                print("1. Enroll a new student")
                                print("2. View details of a student")
                                print("3. View details of all the students according to the branch")
                                print("4. Update student details")
                                print("5. Mark attendance")
                                print("6. View attendance")
                                print("7. Exit")

                                #taking user input number

                                ChoiceNum=int(input("                            Your Choice :"))
                                print()

                                print()
                                print()
                                commen_indexs.clear()
                                break
                            
                            elif save=="no":
                                save=input("Do you want to exite(yes/no)? ")
                                if save=="yes":
                                    print()
                                    
                
    elif ChoiceNum==6:
                  
                    print("                IIT Campus             ")
                    print()
                    print("                Main Menu            ")
                    print()
                    while True:
                        Stud_IDs=str(input("Student ID                         -  "))
                        if len(Stud_IDs)==9 and Stud_IDs.isdigit():
                            Stud_IDs=Stud_IDs
                            break
                            
                        else:
                            print("Please Enter 9 Digits Student ID")
                            
                    Frome_Date=input("From (YYYY.MM.DD)        - ")
                    To_Date=input("To (YYYY.MM.DD)       - ")
                    
                    print()
        
        # Validate the date range and display attendance records
                    print("Date           Present/Absent")
                    print("--------------------------------")
                    records_found = False
                    
                    if Stud_IDs in attendance:
                        attend_dates = list(attendance[Stud_IDs].keys())  # Get list of attendance dates for the student

                        # Check if both Frome_Date and To_Date are in attend_dates
                        if Frome_Date in attend_dates and To_Date in attend_dates:
                            Frome_Date_index = attend_dates.index(Frome_Date)
                            To_Date_index = attend_dates.index(To_Date)
                            
                            # Loop through the date range
                            for attend in attend_dates[Frome_Date_index:To_Date_index + 1]:
                                if attendance[Stud_IDs][attend] == '1':
                                    print(attend, "          Present")
                                else:
                                    print(attend, "          Absent")
                                records_found = True
                                
                            save=input("Do you want to continu (yes/no)")
                            if save == "no":
                                # Exit the loop and break to the main menu
                                break
                            elif save == "yes":
                                # Show main menu if the user answers "yes"
                                print()
                                print("                IIT Campus             ")
                                print()
                                print("                Main Menu            ")
                                print()
                                print("1. Enroll a new student")
                                print("2. View details of a student")
                                print("3. View details of all the students according to the branch")
                                print("4. Update student details")
                                print("5. Mark attendance")
                                print("6. View attendance")
                                print("7. Exit")

                                # Taking user input number
                                ChoiceNum=int(input("                            Your Choice :"))
                                print()         
                                break    
                            else:
                                print("Invalid input. Returning to main menu.")
                                break   
                                
                        else:
                            print("No details in this date range.")
                            records_found = True  # To prevent "No attendance records" message

                    if not records_found:
                        print("No attendance records found for this student in the specified date range.")
                        
                        

    elif ChoiceNum==7:
        print("bye")
        break

        
       



