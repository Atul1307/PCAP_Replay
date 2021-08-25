from mininet.topo import Topo
from mininet.util import irange
from mininet.cli  import CLI
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController, OVSController
from mininet.log import setLogLevel, info
import pandas as pd
from nfstream import NFStreamer
from collections import defaultdict

from scapy.base_classes import Net


class custom_topo(Topo):
    "Configurable Timepass Topology"
    
    def build(self):
        for i,j in hosts1.items():
            self.addHost(i,ip = j)
        for i in swt1:
            self.addSwitch(i)
        for k,v in d.items():
            for i in v:
                self.addLink(k,i)
        

        
def tryf():
    
    df = pd.read_csv("try1.csv")
    df = df.drop(df[df['Destination'] == 'Broadcast'].index)
    df.drop(df.index[(df["Source"] == "fe80::76da:daff:fe14:6e4e")],axis=0,inplace=True)
    column_values = df[["Source", "Destination"]].values.ravel()
    unique_values =  set(pd.unique(column_values))

    my_streamer = NFStreamer(source="try1.pcap", # or network interface
                         decode_tunnels=True,
                         bpf_filter=None,
                         promiscuous_mode=True,
                         snapshot_length=1536,
                         idle_timeout=120,
                         active_timeout=1800,
                         accounting_mode=0,
                         udps=None,
                         n_dissections=20,
                         statistical_analysis=False,
                         splt_analysis=0,
                         n_meters=0,
                         performance_report=0)

    lst = []
    abc = []
    for flow in my_streamer:
        abc.append(flow.src_mac)
        abc.append(flow.dst_mac)
        lst.append(flow.src_ip)
        lst.append(flow.dst_ip)

    lk = set(lst)

    #Hosts
    hosts = unique_values.intersection(lk)

    #Renaming the hosts to h1,h2...
    global hosts1
    hosts1 = {}
    j = 1
    for i in hosts:
        string = 'h'
        string += str(j)
        hosts1[string]=i
        j += 1

    global swt_ip 
    swt_ip = [] #for storing the ip address of the switches which were discovered using their MAC address 
    swt_mac = ['01:00:5e:00:00:fb','d0:81:7a:b4:68:f6','74:da:da:14:6e:4e','ff:ff:ff:ff:ff:ff']
    
    #Adding switches in s1,s2 format
    global swt1
    swt1 = []
    for i in range(4):
        string = 's'
        string += str(i)
        swt1.append(string)
    
    t = -1
    for i in swt_mac:
        t = t+1
        swt_ip.append([])
        for flow in my_streamer:
            if(flow.src_mac == i):
                swt_ip[t].append(flow.src_ip)
            elif(flow.dst_mac == i):
                swt_ip[t].append(flow.dst_ip)


    fset = set(frozenset(x) for x in swt_ip)
    lst = [list(x) for x in fset]

    #Storing switch and host pair, in s1,h1 format
    global d
    d = defaultdict(list)
    for i in range(4):
        string = 's'
        string += str(i)
        for j in range(len(lst[i])):
            for key,value in hosts1.items():
                if(lst[i][j] == value):
                    d[string].append(key)


def runNet():
    "Create and run the network"
    info( "*** Starting network\n" )
    topo = custom_topo()
    net = Mininet( topo = topo)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    net.addLink(net.get('s0'),net.get('s1'))
    net.addLink(net.get('s1'),net.get('s2'))
    net.addLink(net.get('s2'),net.get('s3'))
    

    info( '*** Starting switches\n')
    net.get('s3').start([c0])
    net.get('s2').start([c0])
    net.get('s1').start([c0])
    net.get('s0').start([c0])

    net.get('h1').setDefaultRoute(intf='h1-eth0')
    net.get('h2').setDefaultRoute(intf='h2-eth0')
    net.get('h3').setDefaultRoute(intf='h3-eth0')
    net.get('h4').setDefaultRoute(intf='h4-eth0')
    net.get('h5').setDefaultRoute(intf='h5-eth0')
    net.get('h6').setDefaultRoute(intf='h6-eth0')
    net.get('h7').setDefaultRoute(intf='h7-eth0')
    net.get('h8').setDefaultRoute(intf='h8-eth0')
    net.get('h9').setDefaultRoute(intf='h9-eth0')
    net.get('h10').setDefaultRoute(intf='h10-eth0')
    net.get('h11').setDefaultRoute(intf='h11-eth0')
    net.get('h12').setDefaultRoute(intf='h12-eth0')
    net.get('h13').setDefaultRoute(intf='h13-eth0')
    net.get('h14').setDefaultRoute(intf='h14-eth0')
    net.get('h15').setDefaultRoute(intf='h15-eth0')
    net.get('h16').setDefaultRoute(intf='h16-eth0')
    net.get('h17').setDefaultRoute(intf='h17-eth0')
    net.get('h18').setDefaultRoute(intf='h18-eth0')
    net.get('h19').setDefaultRoute(intf='h19-eth0')
    net.get('h20').setDefaultRoute(intf='h20-eth0')
    net.get('h21').setDefaultRoute(intf='h21-eth0')
    net.get('h22').setDefaultRoute(intf='h22-eth0')
    net.get('h23').setDefaultRoute(intf='h23-eth0')
    net.get('h24').setDefaultRoute(intf='h24-eth0')
    net.get('h25').setDefaultRoute(intf='h25-eth0')
    net.get('h26').setDefaultRoute(intf='h26-eth0')
    net.get('h27').setDefaultRoute(intf='h27-eth0')

    net.start()
    CLI(net)
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    
    tryf()
    runNet()
   
