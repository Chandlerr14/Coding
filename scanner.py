import sys
import socket
from datetime import datetime as dt
# define our target
start = input("Enter the id: ")
target = socket.gethostbyname(start)

print('-'*50)
print("Scanning target"+target)
print("Time started: "+str(dt.now()))
print('-'*50)

try:
    for port in range(430, 445):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator i.e if port open result is 0 else 1
        if result != 0:
            print("Port{} is close".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting the scan.")
    sys.exit()

except socket.gaierror:
    print("Hostname did not dissolve.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
