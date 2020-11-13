from auth_sys_ICCN.Executables.SSHconnect import *

def AddUser(host,passwd,username,userpasswd) :
    SSHexec(host,"root",passwd,"useradd "+username)
    SSHexec(host,"root",passwd,'echo "'+username+':'+userpasswd+'" | chpasswd')

def DelUser(host,passwd,username) :
    SSHexec(host,"root",passwd,"userdel -fr "+username)

def ModUserPwd(host,passwd,username,usernewpasswd):
    SSHexec(host,"root",passwd,'echo "'+username+':'+usernewpasswd+'" | chpasswd')

def utilexist(host,password,name):
    s = SSHexec(host, 'root', password, 'cat /etc/passwd | grep ' + name)
    if len(s) == 0:
        return False
    else:
        return True