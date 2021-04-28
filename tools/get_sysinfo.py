#!/usr/bin/env python3

import subprocess
import os
import pandas as pd

# ensure script is being executed with superuser privileges
if os.geteuid() != 0:
    exit('Please run with sudo privileges or a root.')

# Get serial number and hostname
hostname_cmd = "hostname | cut -d'.' -f1"
hostname = subprocess.check_output(hostname_cmd, shell=True).decode('utf-8')
serial_cmd = "dmidecode -t system | grep -i serial | awk '{ print $NF }'"
serial = subprocess.check_output(serial_cmd, shell=True).decode('utf-8')

# Get the system's manufacturer and model
manuf_cmd = "dmidecode -t system | grep -i manufacturer | awk -F ':' '{ print $2 }' | sed -e 's/^[ \t]*//'"
manufacturer = subprocess.check_output(manuf_cmd, shell=True).decode('utf-8')
model_cmd = "dmidecode -t system | grep -i product | awk -F ':' '{ print $NF }' | sed -e 's/^[ \t]*//'"
model = subprocess.check_output(model_cmd, shell=True).decode('utf-8')

# Get operating system and version
os = subprocess.check_output('cat /etc/redhat-release', shell=True).decode('utf-8')

# Get system memory and hdd/ssd info
mem_cmd = "free -h | sed -n 2p | awk '{ print $2 }'"
memory = subprocess.check_output(mem_cmd, shell=True).decode('utf-8')
hdd_cmd = "lsblk | grep disk | cut -d' ' -f1"
hdd = subprocess.check_output(hdd_cmd, shell=True).decode('utf-8')
hdd_name = hdd.strip('\n')
hdd_capacity_cmd = "lsblk | grep disk | awk '{ print $4 }'"
hdd_capacity = subprocess.check_output(hdd_capacity_cmd, shell=True).decode('utf-8')
hdd_model_cmd = "udevadm info --query=all --name=/dev/" + hdd_name + "| grep -i SCSI_MODEL | sed -n 1p | cut -d'=' -f2"
hdd_model = subprocess.check_output(hdd_model_cmd, shell=True).decode('utf-8')
hdd_serial_cmd = "udevadm info --query=all --name=/dev/" + hdd_name + "| grep -i serial_short | cut -d'=' -f2"
hdd_serial = subprocess.check_output(hdd_serial_cmd, shell=True).decode('utf-8')

df = pd.DataFrame({
    'Hostname': [hostname.strip('\n')],
    'SerialNumber': [serial.strip('\n')],
    'Manufacturer': [manufacturer.strip('\n')],
    'Model': [model.strip('\n')],
    'OS': [os.strip('\n')],
    'Memory': [memory.strip('\n')],
    'HDD_Capacity': [hdd_capacity.strip('\n')],
    'HDD_Model': [hdd_model.strip('\n')],
    'HDD_Serial': [hdd_serial.strip('\n')]
    })

df.to_csv('demo.csv', index=False)
