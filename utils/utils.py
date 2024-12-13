from scapy.all import sniff, wrpcap

def capture_packets(filter="", count=10):
    """Capture network packets."""
    print(f"Capturing {count} packets with filter: {filter}")
    packets = sniff(filter=filter, count=count)
    return packets

def save_packets(packets, filename):
    """Save packets to a .pcap file."""
    wrpcap(filename, packets)  # Save packets to the specified file
    print(f"Saved {len(packets)} packets to {filename}.")
