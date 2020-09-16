#!/usr/local/bin/python

import pynetbox

def conn_netbox():
    url = 'http://10.109.7.197:8085'
    token = 'd88de5cc584600234fc2cf4fc239c77b169469c6'
    nb = pynetbox.api(url=url, token=token)
    return nb

def get_vm():
    nb = conn_netbox()
    vms = nb.virtualization.virtual_machines.all()

    for vm in vms:
        print(vm)

get_vm()
