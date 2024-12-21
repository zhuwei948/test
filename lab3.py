
#!/usr/bin/env python
import paramiko
import time
import getpass
username = raw_input('Username: ')
password = getpass.getpass('password: ')
f = open("ip_list.txt","r")
for line in f.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    print "Successfully connect to ", ip
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("df -h\n")
    remote_connection.send("ls -l\n")
    time.sleep(1)
    output = remote_connection.recv(65535)
    print output
f.close()
ssh_client.close
