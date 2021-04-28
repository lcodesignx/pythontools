#!/usr/bin/env python3

import subprocess

def run(command):
    process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
    )

    stdout_stream = process.stdout.read()
    stderr_stream = process.stderr.read()
    returncode = process.wait()
    if not isinstance(stdout_stream, str):
        stdout_stream = stdout_stream.decode('utf-8')
    if not isinstance(stderr_stream, str):
        stderr_stream = stderr_stream.decode('utf-8')
    stdout = stdout_stream.splitlines()
    stderr = stderr_stream.splitlines()

    return stdout, stderr, returncode

def stop_container(container):
    stdout, stderr, code = run(['docker', 'stop', container])
    if code != 0:
        raise RuntimeError(f'Unable to stop {container}')
    else:
        print(f'Container {container} stopped successfully!')

container = input('enter container name: ')
stop_container(container)
