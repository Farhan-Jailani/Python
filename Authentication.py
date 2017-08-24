fp=open('Employee.txt','r')
n=int(fp.readline())
employee={}
for i in range(n):
    strs=(fp.readline()).split()
    employee[strs[0]]=[strs[1],int(strs[2])]
def Authenticate(username,password,n):
    if(employee[username][0]==password and employee[username][1]==n):
        return True
    else:
        return False