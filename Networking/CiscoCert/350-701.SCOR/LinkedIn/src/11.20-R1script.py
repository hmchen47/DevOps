#!/usr/bib/env python3

import getpass
import sys
import telnetlib

HOST = "192.168.122.252"
user = input("Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t")
tn.write("int lo0/0")
tn.write("ip addr 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print(tn.read_all())
