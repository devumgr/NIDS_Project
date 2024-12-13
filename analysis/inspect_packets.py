from utils.utils import capture_packets

def inspect():
    print("Capturing one packet for inspection...")
    packets = capture_packets(count=10)
    if packets:
        packet = packets[0]  # Get the first packet
        print("\nPacket Summary:")
        print(packet.summary())
        print("\nPacket Details:")
        print(packet.show())
    else:
        print("No packets captured.")

if __name__ == "__main__":
    inspect()
