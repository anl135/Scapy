from scapy.all import *
import random
import sys

#Github Comment

def sending():
    data = IP(src='1.1.1.1', dst='192.168.50.198')/TCP(sport=1024, dport=53, flags='S')
    send(data)
    data_1 = IP(src='1.1.1.2', dst='192.168.50.198') / TCP(sport=1025, dport=53, flags='S')
    send(data_1)
    data_2 = IP(src='1.1.1.3', dst='192.168.50.198') / TCP(sport=1026, dport=53, flags='S')
    send(data_2)
    data_3 = IP(src='1.1.1.4', dst='192.168.50.198') / TCP(sport=1027, dport=53, flags='S')
    send(data_3)
    data_4 = IP(src='1.1.1.5', dst='192.168.50.198') / TCP(sport=1028, dport=53, flags='S')
    send(data_4)
    data_5 = IP(src='1.1.1.6', dst='192.168.50.198') / TCP(sport=1029, dport=53, flags='S')
    send(data_5)
    data_6 = IP(src='1.1.1.7', dst='192.168.50.198') / TCP(sport=1030, dport=53, flags='S')
    send(data_6)
    data_7 = IP(src='1.1.1.8', dst='192.168.50.198') / TCP(sport=1031, dport=53, flags='S')
    send(data_7)
    data_8 = IP(src='1.1.1.9', dst='192.168.50.198') / TCP(sport=1032, dport=53, flags='S')
    send(data_8)
    data_9 = IP(src='1.1.1.10', dst='192.168.50.198') / TCP(sport=1033, dport=53, flags='S')
    send(data_9)




if __name__ == '__main__':
    sending()