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
    
    
    