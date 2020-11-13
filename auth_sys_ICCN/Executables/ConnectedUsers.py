from auth_sys_ICCN.Executables.SSHconnect import *
import paramiko

def user(t,user,passw):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=t, username=user, password=passw)
    except:
        print("[!]Cannot connect to SSH server")
        exit()
    stdin, stdout, stderr = client.exec_command("grep -e /bin/sh -e /bin/bash -e /bin/ksh -e /bin/zsh -e /bin/csh -e /bin/tcsh /etc/passwd |cut -d\":\" -f1 ")
    A = stdout.read().decode()
    B = A.split("\n")
    err = stderr.read().decode()
    if err:
        print(err)
    return B[:len(B)-1]
def ConnectedUsrNow(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"who")
    x = [elem.split() for elem in tmp]
    tmp = []
    for elem in x:
        if elem[0] == "reboot":
            continue
        tmp += [[elem[i] for i in [0, 2,3]]]
    return tmp


def ConnectedUsrLast(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"last")
    for elem in tmp[:-2]:
        x = elem.split()
        if "reboot" in x: tmp.remove(elem)
        else:
            tmp.remove(elem)
            tmp += [[x[0],x[3]+' '+x[5]+' '+x[4],x[6]]]
    return tmp[2:]

"""
def altConnectedUsrLast(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"last")
    x = [elem.split() for elem in tmp]
    tmp = []
    for elem in x:
        if len(elem) > 6 :
            if elem[0]=="reboot":
                continue
            tmp += [[elem[i] for i in [0,3,4,5,6]]]
    return tmp[:-1]
"""

def ConnectedUsrYesterday(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"last --since yesterday")
    for elem in tmp[:-2]:
        x = elem.split()
        if "reboot" in x: tmp.remove(elem)
        else:
            tmp.remove(elem)
            tmp += [[x[i] for i in [0,3,4,5,6]]]
    return tmp[2:]

def ConnectedUsrMonthAgo(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"last --since -30days")
    for elem in tmp[:-2]:
        x = elem.split()
        if "reboot" in x: tmp.remove(elem)
        else:
            tmp.remove(elem)
            tmp += [[x[i] for i in [0,3,4,5,6]]]
    return tmp[2:]

def ConnectedUsrYearAgo(host,passwd) :
    tmp = SSHexec(host,"root",passwd,"last --since -365days")
    for elem in tmp[:-2]:
        x = elem.split()
        if "reboot" in x: tmp.remove(elem)
        else:
            tmp.remove(elem)
            tmp += [[x[i] for i in [0,3,4,5,6]]]
    return tmp[2:]

def LastUserConnections(host,passwd) :
    tmp = user(host,"root",passwd)
    LastConnection = []
    for elem in tmp :
        SSHresult = SSHexec(host, "root", passwd, "last "+elem)
        try:
            SSHresult = [[SSHresult[0].split()[0],SSHresult[0].split()[3]+' '+SSHresult[0].split()[5]+' '+SSHresult[0].split()[4],SSHresult[0].split()[6]]]
            LastConnection += SSHresult
        except : continue
    return LastConnection


for i in range(1,11+1):
    for p in range(1,11-i+1):
        for n in range(1,11-i-p+1):
            if 2*i+3*p+5*n == 39 and i+p+n==11:
                print([i,p,n])

print("\n")

for i in range(1,19+1):
    for p in range(1,19-i+1):
        for n in range(1,19-i-p+1):
            if 2*i+3*p+5*n == 61 and i+p+n==19 and (n+5==10 or n+4==10):
                print([i,p,n])

4 taw3 5
2 taw3 2
2 taw3 3