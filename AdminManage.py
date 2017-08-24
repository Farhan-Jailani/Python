fp=open('Employee.txt','r')
n=int(fp.readline())
employee={}
usernames=[]
for i in range(n):
    strs=(fp.readline()).split()
    usernames.append(strs[0])
    employee[strs[0]]=[strs[1],int(strs[2]),strs[3],strs[4],int(strs[5]),float(strs[6])]
def AddEmployee(username,password,n):
    usernames.append(username)
    employee[username]=[password,n]
    employee[username].append(input('enter the first name'))
    employee[username].append(input('enter the last name'))
    employee[username].append(input('enter the age'))
    employee[username].append(input('enter the salary'))
    save()
def save():
    fp1=open('Employee.txt','w')
    fp1.write(str(employee.__len__()))
    for username in usernames:
        fp1.write('\n'+username+' '+employee[username][0]+' '+str(employee[username][1])+' '+employee[username][2]+' '+employee[username][3]+' '+str(employee[username][4])+' '+str(employee[username][5]))
    
    