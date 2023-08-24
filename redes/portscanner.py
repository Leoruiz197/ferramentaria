from math import floor
import socket
import threading
import time
import sys

logo = r"""                                                                                                                                                                                                                                                 
  _____   ____  _____ _______    _____  _____          _   _ _   _ ______ _____  
 |  __ \ / __ \|  __ \__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
 
"""

print(logo)
def test_open_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False

def worker_function(start_port, end_port, target_ip, open_ports):
    for port in range(start_port, end_port + 1):
        if test_open_port(target_ip, port):
            print(f"Porta {port} está aberta em {target_ip}")
            open_ports.append(port)

def loading_animation():
    animation = "|/-\\"
    idx = 0
    while not done_event.is_set():
        sys.stdout.write("\r" + "Aguarde... " + animation[idx % len(animation)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

def main():
    target_ip = input("Digite o endereço IP alvo: ")
    start_port = int(input("Digite a porta inicial a ser testada: "))
    end_port = int(input("Digite a porta final a ser testada: "))
    num_threads = floor((end_port-start_port)/10)  # Número de threads
    print(f"Threads criadas: {num_threads}")
    
    total_ports = end_port - start_port + 1
    ports_per_thread = total_ports // num_threads
    threads = []
    open_ports = []

    global done_event
    done_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    start_time = time.time()

    for i in range(num_threads):
        start_range = start_port + i * ports_per_thread
        end_range = start_range + ports_per_thread - 1
        if i == num_threads - 1:  # A última thread pode precisar cobrir portas restantes
            end_range = end_port
        thread = threading.Thread(target=worker_function, args=(start_range, end_range, target_ip, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    done_event.set()
    loading_thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if open_ports:
        print("\nPortas abertas:")
        open_ports.sort()  # Ordena a lista de portas
        for port in open_ports:
            print(port)
    else:
        print("\nNenhuma porta aberta.")

    print(f"Tempo total de execução: {elapsed_time:.2f} segundos.")

if __name__ == "__main__":
    main()
