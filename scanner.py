#!/bin/python3

import sys
import socket
from datetime import datetime

# Define Target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    
else:
    print("You didn't provide a target, dummy")
    print("Syntax: python3 scanner.py <ip or hostname>")

# if you want to run it from something other than linux terminal
# target = '10.24.24.1'

#Scan ports
def scan_ports():
    
    #Banner
    print('-' * 50)
    print(f'Scanning target {target}')
    print(f'Time started: {str(datetime.now())}')
    print('-' * 50)

    try:
        start = datetime.now()
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port)) #Returns 0 if port is open, 1 if not
            if result == 0:
                print(f"Port {port} is open!")
            s.close()
        finish = datetime.now()
        print("Port scan complete, it took", finish - start)
        print('-' * 50)
    
    except KeyboardInterrupt:
        print("\nAborting port scan because the user didn't want it to finish for some reason.")
        print('-' * 50)
        sys.exit()
    except socket.gaierror:
        print("Hostname couldn't be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to the server.")
        sys.exit()