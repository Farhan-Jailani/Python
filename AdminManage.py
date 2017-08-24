import shelve
f1=shelve.open('empdata.txt','c')
employee=f1['emp']
def AddEmployee(username,password,n):
    employee[username]=[password,n]
    employee[username].append(input('enter the first name'))
    employee[username].append(input('enter the last name'))
    employee[username].append(input('enter the age'))
    employee[username].append(input('enter the salary'))
    f1['emp']=employee
    
def DeleteEmployee(username):
    employee.pop(username)
    f1['emp']=employee
def UpdateEmployee(username):
    a=True
    while(a):
        n=input('details to change:  1.password 2.first name 3.last name 4.age 5.salary 6.priority')
        if(n==1):
            employee[username][0]=input('enter the new password')
        elif(n==2):
            employee[username][2]=input('enter the First name')
        elif(n==3):
            employee[username][3]=input('enter the Last Name')
        elif(n==4):
            employee[username][4]=int(input('enter the age'))
        elif(n==5):
            employee[username][5]=float(input('enter the salary'))
        elif(n==6):
            employee[username][0]=int(input('enter the new priority  1.Admin 2.Police 3.User'))
        else:
            f1['emp']=employee
            print('wrong choice')
            a=False
    
    
    
    