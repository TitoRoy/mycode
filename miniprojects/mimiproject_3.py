#!/usr/bin/env python

#to know the present status of network devices

from netmiko import Netmiko
from getpass import getpass

#password object is created to login to the network devices
password = getpass()

#creating a device inventory list for to control 
cisco1 = {
    'host': 'cisco1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_ios',
}

cisco2 = {
    'host': 'cisco2.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_ios',
}

nxos1 = {
    'host': 'nxos1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_nxos',
}

srx1 = {
    'host': 'srx1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'juniper_junos',
}

#loop over the devices on the list
for device in (cisco1, cisco2, nxos1, srx1):
    net_connect = Netmiko(**device)
#display the last prompt of each devices
print(net_connect.find_prompt())
