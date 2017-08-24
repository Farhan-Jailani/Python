import shelve
f1=shelve.open('empdata.txt','c')
employee=f1['emp']
f1.close()
def Authenticate(username,password,n):
    if(employee[username][0]==password and employee[username][1]==n):
        return True
    else:
        return False