'''
IPScaner(Unfinished)
Can scan only 500 diapasons automaticaly
in the directory must be file Dia.txt, why, because.
'''
import socket
import subprocess as sub
import threading

while True:
    try:
        
        PR = int(input("Port : "))#Port
        if PR<=0 or PR>65535:
            print('Invalid port')
            continue       
        break
    except:
        print('Invalid port')
QOS = 0.4 #Quality Of Scan, less = faster
file = open('srvrs('+str(PR)+').txt','w')#Out file


def IPdia(cont):
    cont = list(cont)
    ip = []
    NM = ''
    for i in range(len(cont)):
        if cont[i]=='.'or cont[i]=='-':
            ip.append(int(NM))
            NM = ''
        else:
            NM =NM + cont[i]
    try:
        ip.append(int(NM))
        return ip
    except:
        print(NM)
    

def scan(ip,ew,es):
    ips = []
    for first in range(ip[0],ip[4]+1):
        for second in range(ip[1],ip[5]+1):
            for third in range(ip[2],ip[6]+1):
                for fourth in range(ip[3],ip[7]+1):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(QOS)
                    ipn = str(first)+'.'+str(second)+'.'+str(third)+'.'+str(fourth)
                    
                    try:
                        sock.connect((ipn,PR))
                        ips.append(ipn)
                        
                    except:
                        continue
    ew.wait() # wait for event
    ew.clear()
    if ips!=[]:
        print(ips)
        port = str(port)
        for i in range(len(ips)):
            file.write(ips[i]+':'+port+'\n')
    es.set()



def CheckIps():
    dia = []
    try:
        File = open('Dia.txt','r')
    except:
        print("Can`t find file Dia.txt!\nStoping")
        return 
    cont = True
    while cont:
        cont = File.readline()
        dia.append(IPdia(cont))
    File.close()
    dia.remove(None)
    n = len(dia)
    if n > 500:
        n = 501
    e = []
    t = []
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Eenot Scanner(RAW)~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nScanning started...")
    for i in range(n+1):
        e.append(threading.Event())
    for i in range(n):
        t.append(threading.Thread(target = scan, args=(dia[i],e[i],e[i+1])))

    for i in range(n):
        t[i].start()
    for i in range(n):
        try:
            e[i].set()
        except:
            break
    for i in range(n):
        t[i].join()
        
    

CheckIps(PR)
file.close()
#sub.call('shutdown /s',shell = True) #optional
input('Done!')

