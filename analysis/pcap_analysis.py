from scapy.all import rdpcap

def analyze_pcap():
    file_path = "data/captured_packets.pcap"
    print(f"Reading packets from {file_path}...")
    packets = rdpcap(file_path)
    print(f"Number of packets: {len(packets)}")

    for i, packet in enumerate(packets[:5], 1):  # Analyze the first 5 packets
        print(f"\nPacket {i}:")
        print(packet.summary())
        print(packet.show())

if __name__ == "__main__":
    analyze_pcap()

