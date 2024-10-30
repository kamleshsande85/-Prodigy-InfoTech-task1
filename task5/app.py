# from scapy.all import sniff
# from scapy.layers.inet import IP, TCP, UDP
# from scapy.config import conf
# conf.LFP_METHOD = "libpcap"  # Use libpcap for LPM

# def packet_callback(packet):
#     # Check if the packet has an IP layer
#     if IP in packet:
#         ip_src = packet[IP].src
#         ip_dst = packet[IP].dst
#         protocol = packet[IP].proto
        
#         # Determine the protocol
#         if protocol == 6:  # TCP
#             proto_name = "TCP"
#         elif protocol == 17:  # UDP
#             proto_name = "UDP"
#         else:
#             proto_name = "Other"
        
#         print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {proto_name}")
        
#         # If the packet contains TCP or UDP layer, display payload
#         if packet.haslayer(TCP):
#             payload = packet[TCP].payload
#             print(f"TCP Payload: {bytes(payload)}")
#         elif packet.haslayer(UDP):
#             payload = packet[UDP].payload
#             print(f"UDP Payload: {bytes(payload)}")
#         print("-" * 50)

# # Start sniffing packets on the network
# print("Starting packet sniffing...")
# sniff(prn=packet_callback, store=0)
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine the protocol
        if protocol == 6:  # TCP
            proto_name = "TCP"
        elif protocol == 17:  # UDP
            proto_name = "UDP"
        else:
            proto_name = "Other"

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {proto_name}")

        # If the packet contains TCP or UDP layer, display payload
        if packet.haslayer(TCP):
            payload = packet[TCP].payload
            print(f"TCP Payload: {bytes(payload)}")
        elif packet.haslayer(UDP):
            payload = packet[UDP].payload
            print(f"UDP Payload: {bytes(payload)}")
        print("-" * 50)

# Start sniffing packets on the network
print("Starting packet sniffing...")
sniff(prn=packet_callback, store=0, count=10)  # Limit to 10 packets for demonstration