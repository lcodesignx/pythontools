#!/usr/local/bin/python3

# A system information gathering script
import subprocess

# system info
def uname_func():
    uname = 'uname'
    uname_arg = '-a'
    print(f'Gathering system information with {uname} command:\n')
    subprocess.call([uname, uname_arg])

# disk info
def disk_func():
    diskspace = 'df'
    diskspace_arg = '-h'
    print(f'Gathering diskpace information with {diskspace} command:\n')
    subprocess.call([diskspace, diskspace_arg])

# memory info
def mem_func():
    memory = 'free'
    memory_args = '-m'
    print(f'Gathering system memory information with {memory} command:\n')
    subprocess.call([memory, memory_args])

# main function
def main():
    uname_func()
    disk_func()
    mem_func()

if __name__ == '__main__':
    main()
