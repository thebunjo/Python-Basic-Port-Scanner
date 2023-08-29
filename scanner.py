import socket
import threading
import time

def tarama(host):
    port_list = [21, 22, 23, 25, 53, 80, 139, 443, 445, 3306, 8080, 3389, 5900, 8081]
    print_lock = threading.Lock()

    def port_scan(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        result = sock.connect_ex((host,port))
        sock.close()
        with print_lock:
            if result == 0:
                print(f"{port} Open.")
            else:
                print(f"{port} Closed or filtered..")
    threads = []
    for port in port_list:
        thread = threading.Thread(target=port_scan, args=(port,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    host = input("Host: ")
    tarama(host)
