import pandas as pd
from scapy.all import *
import random
    
df = pd.read_csv("try1.csv")
df = df.drop(df[df['Destination'] == 'Broadcast'].index)
df.drop(df.index[(df["Source"] == "fe80::76da:daff:fe14:6e4e")],axis=0,inplace=True)
column_values = df[["Source", "Destination"]].values.ravel()
unique_values =  set(pd.unique(column_values))

src_r = df['Source'].tolist()
src_li = list(set(src_r))
src_li.remove('Apple_b4:68:f6')
dst_r = df['Destination'].tolist()
dst_li = list(set(dst_r))
dst_li.remove('D-LinkIn_14:6e:4e')

p = 0
            
for i,j in zip(src_r,dst_r):
    for f in src_li:
        if(f == i):
            sr = f
            for b in dst_li:
                if(b == j):
                    source_port = random.randint(1,65535)
                    source_ip = f 
                    IP1 = IP(src = source_ip, dst = b)
                    TCP1 = TCP(sport = source_port, dport = 80)
                    pkt = IP1 / TCP1
                    print(b)
                    send(pkt,inter = .001)
                    print ("packet sent ", p)
                    p = p + 1
