#!/usr/bin/env python
import paramiko
import time

ip = "172.16.1.1"
username = "zhuwei"
password = "123.com"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=username,password=password)

print ("Sucessfully login to ", ip)

command = ssh_client.invoke_shell()
#command = ssh.invoke_shell()
#command.send("ls \n")
command.send("ls -l \n")
command.send("df -h \n")
time.sleep(1)
output = command.recv(65535)
print output
ssh_client.close