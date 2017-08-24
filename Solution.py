import Authentication
import AdminManage
userType=int(input('Select the user type     1.Admin   2.Police Officer   3.User'));
if(userType==1):
    username=input('Username: ')
    password=input('Password: ')
    if(Authentication.Authenticate(username, password, userType)):
        print('1.Add employee  2.Delete Employee 3.update Details 4.view Details  5.exit')
        choice=int(input())
        if(choice==1):
            AdminManage.AddEmployee(input('enter username'),input('enter password'), 2)
    else:
        print('wrong username/password')
elif(userType==2):
    username=input('Username: ')
    password=input('Password: ')
    if(Authentication.Authenticate(username, password, userType)):
        pass
    else:
        print('wrong username/password')
elif(userType==3):
    username=input('Username: ')
    password=input('Password: ')
    if(Authentication.Authenticate(username, password, userType)):
        pass
    else:
        print('wrong username/password')