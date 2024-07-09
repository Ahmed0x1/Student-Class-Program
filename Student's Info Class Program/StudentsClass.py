#Others

def isRepeat(stName):
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as repeat:
        data = repeat.readlines()

    parts = []
    for i in range(len(data)):
        parts.append(data[i].strip().split("::"))

    for i in range(0 , len(parts) , 1):
        for j in range(0 , len(parts), 1):
            if stName == parts[i][j]:
                return True
            else:
                return False

def isThere(student):
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as st:
        data = st.readlines()

        for i in data:
            if student == i:
                return True
            
            else:
                continue

        return False

#Student Settings functions

def checkData():
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as Data:
        check = Data.readlines()

        if check == []:
            return True
        
        else:
            return False
#--------------------------        

def fAdding(stName , stDegree , stPhoneNumber , stAddress):
    with open(".\\Project\\SaveData\\studentInfo", 'w') as Add:
        Add.write(f"{stName}::{stDegree}::{stPhoneNumber}::{stAddress}\n")

def lAdding(stName , stDegree , stPhoneNumber , stAddress):
    with open(".\\Project\\SaveData\\studentInfo", 'a') as Add:
        Add.write(f"{stName}::{stDegree}::{stPhoneNumber}::{stAddress}\n")

def addStudent():
    stName = input("Enter student name: ")
    stDegree = float(input("Enter student degree: "))
    stPhoneNumber = input("Enter student phone number: ")
    stAddress = input("Enter student address: ")

    if isRepeat(stName):
        print("\nERROR: Student is already exited!!.")
        studentSettings()
    else:
        if checkData():
            fAdding(stName , stDegree , stPhoneNumber , stAddress)

        else:
            lAdding(stName , stDegree , stPhoneNumber , stAddress)

    print("-------------------(Student Added)-------------------")
    studentSettings()

#--------------------------

def modifying(student, stName , stDegree, stPhoneNumber , stAddress):
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as st:
        data = st.readlines()

    sizeOfData = len(data)
    indexOfStudent = 0

    for i in range(0 , sizeOfData , 1):
        #print(i)
        if student == data[i]:
            indexOfStudent = i
        
        else:
            continue
    
    data[indexOfStudent] = f"{stName}::{stDegree}::{stPhoneNumber}::{stAddress}\n"

    with open(".\\Project\\SaveData\\studentInfo" , 'w') as modify:
        modify.writelines(data)  

def modifyStudent():
    stName = input("Enter student name: ")
    stDegree = float(input("Enter student degree: "))
    stPhoneNumber = input("Enter student phone number: ")
    stAddress = input("Enter student address: ")

    student = f"{stName}::{stDegree}::{stPhoneNumber}::{stAddress}\n"

    if isThere(student):
        print("-------------------(Student Modifying Now)-------------------")
        stName = input("Enter student name: ")
        stDegree = float(input("Enter student degree: "))
        stPhoneNumber = input("Enter student phone number: ")
        stAddress = input("Enter student address: ")
        modifying(student , stName , stDegree, stPhoneNumber , stAddress)

    else:
        print("not found")
    print("-------------------(Student Modified)-------------------")
    studentSettings()

#--------------------------

def specificRemoveStudent(student):
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as st:
        data = st.readlines()

    sizeOfData = len(data)
    indexOfStudent = 0

    for i in range(0 , sizeOfData , 1):
        #print(i)
        if student == data[i]:
            indexOfStudent = i
        
        else:
            continue
    
    data[indexOfStudent] = ""

    with open(".\\Project\\SaveData\\studentInfo" , 'w') as Remove:
        Remove.writelines(data)

    print("-------------------(Student is Removed)-------------------")
    removeStudent()

def allRemoveStudent():
    with open(".\\Project\\SaveData\\studentInfo" , 'w') as st:
        pass
    
    print("-------------------(All Students Are Removed)-------------------")
    removeStudent()

def removeStudent():
    print("-------------------(Student Removed)-------------------")
    print("[1] specific Student")
    print("[2] all Students")
    print("[3] Return")
    choice = input("[?]: ")
    
    if choice == "1":
        stName = input("Enter student name: ")
        stDegree = float(input("Enter student degree: "))
        stPhoneNumber = input("Enter student phone number: ")
        stAddress = input("Enter student address: ")
        student = f"{stName}::{stDegree}::{stPhoneNumber}::{stAddress}\n"

        specificRemoveStudent(student)

    elif choice == "2":
        allRemoveStudent()

    elif choice == "3":
        studentSettings()

    else:
        print("Error in your choice, please select again.")
        removeStudent()


#--------------------------
#Student Info functions

def listInShow():
    print("[1] Return")
    choice = input("[?]: ")

    if choice == "1":
        main()

    else:
        print("Error in your choice, please select again.")
        listInShow()

def showStudent():
    #print data here
    #show = open("path" , 'r')
    stNum = 0
    with open(".\\Project\\SaveData\\studentInfo" , 'r') as show:
        stShow = show.readlines()
        for i in stShow:
            print(i)
            stNum +=1

    print(f"-------------------(Student Number {stNum})-------------------")
    print("[1] Return")
    choice = input("[?]: ")

    if choice == "1":
        main()

    else:
        print("Error in your choice, please select again.")
        listInShow()
        

#--------------------------
#Main functions

def studentSettings():
    print("-------------------(Student Settings)-------------------")
    print("[1] Add Student")
    print("[2] Modify Student")
    print("[3] Remove Student")
    print("[4] Return")
    choice = input("[?]: ")
    
    if choice == "1":
        addStudent()

    elif choice == "2":
        modifyStudent()

    elif choice == "3":
        removeStudent()

    elif choice == "4":
        main()

    else:
        print("Error in your choice, please select again.")
        studentSettings()

def studentsInfo():
    print("-------------------(Students Info)-------------------")
    print("[1] Show Student")
    print("[2] Return")
    choice = input("[?]: ")
    
    if choice == "1":
        showStudent()

    elif choice == "2":
        main()

    else:
        print("Error in your choice, please select again.")
        studentsInfo()

def about():
    print("-------------------(About)-------------------")
    print("student class we need sometimes program to manage\nour student in class such as thier degree, names, \nphone number, address, the aim from this help the\nteacher in his class.")
    print("[1] Return")
    choice = input("[?]: ")

    if choice == "1":
        main()

    else:
        print("Error in your choice, please select again.")
        about()
#--------------------------

def main():
    choice = ""
    print("-------------------(Student class)-------------------")
    print("[1] Student Settings")
    print("[2] Students Info")
    print("[3] About")
    print("[4] exit")
    choice = input("[?]: ")
    
    if choice == "1":
        studentSettings()

    elif choice == "2":
        studentsInfo()

    elif choice == "3":
        about()

    elif choice == "4":
        exit()

    else:
        print("Error in your choice, please select again.")
        main()

main()