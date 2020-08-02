#!/usr/local/bin/python
from datetime import datetime

filename = 'guest_bookt.txt'

username = ''
while (username != 'e'):
    username = input('Enter your name: program exits if you enter (e) ')
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    
    if (username == 'e'):
        print("Exiting program...")
    else:
        with open(filename, 'a') as f:
            f.write(username + ' : ' + timestampStr + '\n')
        print(f'Welcome to Python programming, {username}')
