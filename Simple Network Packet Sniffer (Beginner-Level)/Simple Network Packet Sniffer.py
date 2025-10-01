from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Sniffing packets... (Press CTRL+C to stop)")
sniff(prn=packet_callback, count=10)  # capture 10 packets
