from scapy.all import ARP, Ether, srp

def scan_devices(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    ip_range = input("Digite o intervalo de IPs a serem escaneados (ex. 192.168.1.0/24): ")
    devices = scan_devices(ip_range)

    print("Dispositivos encontrados na rede:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

if __name__ == "__main__":
    main()
