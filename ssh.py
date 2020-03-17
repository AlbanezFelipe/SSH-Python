############################################
# Simple Python script for SSH automation using paramiko
# Connect with a ssh session e execute a list of commands once
# Maybe has some bugs
#
# By: Felipe Albanez Contin
#
# Feel free to use and edit this script for any purpose
#
############################################

from paramiko import SSHClient
import paramiko
import time

############################################
# SSH configuration
############################################

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

############################################
# SSH Parameters
############################################

ip = "0.0.0.0"
user = "root"
password = "password"

############################################
# Commands to execute in ssh (list sequence)
############################################

commands = [
	"uname -a",
	"lscpu",
	"free"
]

############################################

def openSSH():
    ssh.connect(
        hostname=ip,
        port=22,
        username=user,
        password=password
    )

############################################

def runCommands(commands):

    #Open Shell
    shell = ssh.invoke_shell()
    time.sleep(.5)
    printAnswer(shell.recv(65535))

    #Execute commands
    for command in commands:
        shell.send(command + "\n") # run command
        time.sleep(.5)
        printAnswer(shell.recv(65535)) # print answer
        print("\n---------------------------------------\n")

############################################

def closeSSH():
    ssh.close()
    print("connection closed")

############################################

def printAnswer(s):
    print(str(s).replace("\\n", "\n").replace("\\r", "\r"))

############################################
# Flow
############################################

openSSH()
runCommands(commands)
closeSSH()

