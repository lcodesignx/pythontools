#!/Users/lupera1/Applications/anaconda3/bin/python

import subprocess
import pynetbox

def conn_netbox():
    url = 'http://10.109.7.197:8085'
    token = 'd88de5cc584600234fc2cf4fc239c77b169469c6'
    nb = pynetbox.api(url=url, token=token)
    return nb

# store all vms in a list
vms = conn_netbox().virtualization.virtual_machines.all()

def update_netvm():
    ansibledistribution = 'RedHat'
    major_release = subprocess.check_output("awk '{ print $6 }' /etc/redhat-release", shell=True)
    release = subprocess.check_output("awk '{ print $6 }' /etc/redhat-release | cut -d'.' -f1", shell=True)
    comment = 'python auto-generated test'
    for vm in vms:
        vm.update({'comments':comment, 'custom_fields':{
            'ansibledistribution':ansibledistribution, 'major_release': major_release.decode("utf-8"), 'release': release.decode("utf-8")
            }})

def main():
    update_netvm()

if __name__ == '__main__':
    main()
