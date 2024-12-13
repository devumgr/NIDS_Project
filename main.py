from analysis.inspect_packets import inspect
from analysis.http_analysis import analyze_http
from analysis.dns_analysis import analyze_dns
from analysis.pcap_analysis import analyze_pcap

def main():
    while True:
        print("\nChoose an action:")
        print("1. Inspect live packets")
        print("2. Analyze HTTP traffic")
        print("3. Analyze DNS traffic")
        print("4. Analyze saved .pcap file")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                inspect()
            elif choice == "2":
                analyze_http()
            elif choice == "3":
                analyze_dns()
            elif choice == "4":
                analyze_pcap()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

