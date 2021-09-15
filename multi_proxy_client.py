#!/usr/bin/env python3
import socket
from multiprocessing import Pool

HOST = 'localhost'
PORT = 8001
payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
BUFFER_SIZE = 1024

def main(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(addr)        
        #send the data and shutdown
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        #continue accepting data until no more left
        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        #always close at the end!
        s.close()

if __name__ == "__main__":
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(main, address * 3)