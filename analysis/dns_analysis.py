from scapy.all import sniff

def analyze_dns():
    def dns_handler(packet):
        if packet.haslayer("DNS"):
            dns_layer = packet["DNS"]
            if dns_layer.qr == 0:  # Query
                print(f"DNS Query: {dns_layer.qd.qname.decode()}")
            else:  # Response
                print(f"DNS Response Transaction ID: {dns_layer.id}")

    print("Capturing DNS packets...")
    sniff(filter="udp port 53", count=5, prn=dns_handler)

if __name__ == "__main__":
    analyze_dns()



