#!/usr/bin/python

import pynetbox
import csv

# create pynetbox api connection object
def conn_netbox():
    url = 'http://10.109.7.197:8085'
    token = 'd88de5cc584600234fc2cf4fc239c77b169469c6'
    nb = pynetbox.api(url=url, token=token)
    return nb

# function gets all devices in netbox and places them in a list
def get_dev():
    conn = conn_netbox()
    devices = conn.dcim.devices.all()
    lst_dev = []

    for device in devices:
        lst_dev.append(device)
    return lst_dev

# convert python list into csv file
def to_csv():
    lst = get_dev()

    # write list to csv file
    with open('netbox-inventory.csv', 'w') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(lst)

    # display list of devices to the console
    for i in lst:
        print(i)

def main():
    to_csv()
    get_vm()

if __name__ == '__main__':
    main()
