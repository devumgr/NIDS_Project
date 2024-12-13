from scapy.all import sniff

def analyze_http():
    def http_handler(packet):
        if packet.haslayer("IP"):
            ip_layer = packet["IP"]
            print(f"HTTP Packet: {ip_layer.src} -> {ip_layer.dst}")
            print(packet.summary())

    print("Capturing HTTP packets...")
    sniff(filter="tcp port 80", count=5, prn=http_handler)

if __name__ == "__main__":
    analyze_http()

