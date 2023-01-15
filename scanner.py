import socket
import time 
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target_ip = socket.gethostbyname(sys.argv[1])
print('Scan started on the following address: ', target_ip)

def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()

for port in range(65535):
    if port_scan(port):
        print(f'port {port} is open')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')

s.close()


