#!/usr/bin/python3

import subprocess
import pynetbox

# Comment test
def conn_netbox():
    url = 'http://10.109.7.197:8085'
    token = 'd88de5cc584600234fc2cf4fc239c77b169469c6'
    nb = pynetbox.api(url=url, token=token)
    return nb

# Comment test
def create_vm():
    # system data
    name_bytes = subprocess.check_output("hostname", shell=True)
    name_string = name_bytes.decode("utf-8")
    cores_bytes = subprocess.check_output("lscpu | egrep '^CPU\(' | awk '{ print $2 }'", shell=True)
    cores_string = cores_bytes.decode("utf-8")
    mem_bytes = subprocess.check_output("free -m | sed -n 2p | awk '{ print $2 }'", shell=True)
    mem_string = mem_bytes.decode("utf-8")
    disk_bytes = subprocess.check_output("fdisk -l /dev/sda | grep Disk | sed -n 1p | awk '{ print $3 }' | awk -F '.' '{ print $1 }'", shell=True)
    disk_string = disk_bytes.decode("utf-8")

# Comment test
    nb = conn_netbox()
    nb.virtualization.virtual_machines.create(
           name = name_string,
           role = nb.dcim.device_roles.filter(q="Server")[1].id,
           cluster = nb.virtualization.clusters.filter(q="aplcloud")[0].id,
           vcpus = cores_string,
           memory = mem_string,
           disk = disk_string,
    )

create_vm()

