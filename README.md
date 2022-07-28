

░█████╗░████████╗███████╗  ███╗░░██╗██████╗░████████╗
██╔══██╗╚══██╔══╝██╔════╝  ████╗░██║╚════██╗╚══██╔══╝
██║░░╚═╝░░░██║░░░█████╗░░  ██╔██╗██║░█████╔╝░░░██║░░░
██║░░██╗░░░██║░░░██╔══╝░░  ██║╚████║░╚═══██╗░░░██║░░░
╚█████╔╝░░░██║░░░██║░░░░░  ██║░╚███║██████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░░░  ╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░
Krd-Pentester
Especially For ROOT ME CTF N3TWORK




# TCP-STREAM-CTF-FTP
Professional TCP STREAM Follower For CTF Network FTP 



# Python Modules 

Pyshark


# File Requierment's

Wireshark Pcap Files


# Source Code 

f3l_n3m = 'ch1.pcap'
STREAM_NUMBER = 0

cap = pyshark.FileCpautre(f3l_n3m,display_filter='tcp.stream eq %d' % STREAM_NUMBER)

while True:
    try:
        p = cap.next()
    
# Banner Available On 

fsymbol 
