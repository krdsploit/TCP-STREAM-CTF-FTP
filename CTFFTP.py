import pyshark


banner = ''' 



░█████╗░████████╗███████╗  ███╗░░██╗██████╗░████████╗
██╔══██╗╚══██╔══╝██╔════╝  ████╗░██║╚════██╗╚══██╔══╝
██║░░╚═╝░░░██║░░░█████╗░░  ██╔██╗██║░█████╔╝░░░██║░░░
██║░░██╗░░░██║░░░██╔══╝░░  ██║╚████║░╚═══██╗░░░██║░░░
╚█████╔╝░░░██║░░░██║░░░░░  ██║░╚███║██████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░░░  ╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░

Krd-Pentester

Especially For ROOT ME CTF N3TWORK



'''

f3l_n3m = 'ch1.pcap'
STREAM_NUMBER = 0

cap = pyshark.FileCpautre(f3l_n3m,display_filter='tcp.stream eq %d' % STREAM_NUMBER)

while True:
    try:
        p = cap.next()
    except StopIteration:
        try:
            print(p.data.data.binary_value)
        except AttributeError:
            pass