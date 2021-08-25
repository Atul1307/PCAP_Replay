#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   link=TCLink, #must be added in order to change link  parameters eg. bw,delay etc. 
                   build=False)
                   #,ipBase='0.0.0.0'
                   #)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    
    h1  = net.addHost('h1',  cls=Host, ip='10.0.0.1',  defaultRoute=None)
    h2  = net.addHost('h2',  cls=Host, ip='10.0.0.2',  defaultRoute=None)
    h3  = net.addHost('h3',  cls=Host, ip='10.0.0.3',  defaultRoute=None)
    h4  = net.addHost('h4',  cls=Host, ip='10.0.0.4',  defaultRoute=None)
    h5  = net.addHost('h5',  cls=Host, ip='10.0.0.5',  defaultRoute=None)
    h6  = net.addHost('h6',  cls=Host, ip='10.0.0.6',  defaultRoute=None)
    h7  = net.addHost('h7',  cls=Host, ip='10.0.0.7',  defaultRoute=None)
    h8  = net.addHost('h8',  cls=Host, ip='10.0.0.8',  defaultRoute=None)
    h9  = net.addHost('h9',  cls=Host, ip='10.0.0.9',  defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    
    h11 = net.addHost('h11', cls=Host, ip='10.1.0.1', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.1.0.2', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.1.0.3', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.1.0.4', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.1.0.5', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.1.0.6', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.1.0.7', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.1.0.8', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.1.0.9', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.1.0.10',defaultRoute=None)
    
    h21 = net.addHost('h21', cls=Host, ip='10.2.0.1', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.2.0.2', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.2.0.3', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.2.0.4', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.2.0.5', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.2.0.6', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.2.0.7', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.2.0.8', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.2.0.9', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.2.0.10',defaultRoute=None)
    
    h31 = net.addHost('h31', cls=Host, ip='10.3.0.1', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.3.0.2', defaultRoute=None)
    h33 = net.addHost('h33', cls=Host, ip='10.3.0.3', defaultRoute=None)
    h34 = net.addHost('h34', cls=Host, ip='10.3.0.4', defaultRoute=None)
    h35 = net.addHost('h35', cls=Host, ip='10.3.0.5', defaultRoute=None)
    h36 = net.addHost('h36', cls=Host, ip='10.3.0.6', defaultRoute=None)
    h37 = net.addHost('h37', cls=Host, ip='10.3.0.7', defaultRoute=None)
    h38 = net.addHost('h38', cls=Host, ip='10.3.0.8', defaultRoute=None)
    h39 = net.addHost('h39', cls=Host, ip='10.3.0.9', defaultRoute=None)
    h40 = net.addHost('h40', cls=Host, ip='10.3.0.10',defaultRoute=None)
    
    h41 = net.addHost('h41', cls=Host, ip='10.4.0.1', defaultRoute=None)
    h42 = net.addHost('h42', cls=Host, ip='10.4.0.2', defaultRoute=None)
    h43 = net.addHost('h43', cls=Host, ip='10.4.0.3', defaultRoute=None)
    h44 = net.addHost('h44', cls=Host, ip='10.4.0.4', defaultRoute=None)
    h45 = net.addHost('h45', cls=Host, ip='10.4.0.5', defaultRoute=None)
    h46 = net.addHost('h46', cls=Host, ip='10.4.0.6', defaultRoute=None)
    h47 = net.addHost('h47', cls=Host, ip='10.4.0.7', defaultRoute=None)
    h48 = net.addHost('h48', cls=Host, ip='10.4.0.8', defaultRoute=None)
    h49 = net.addHost('h49', cls=Host, ip='10.4.0.9', defaultRoute=None)
    h50 = net.addHost('h50', cls=Host, ip='10.4.0.10',defaultRoute=None)
    
    h51 = net.addHost('h51', cls=Host, ip='10.5.0.1', defaultRoute=None)
    h52 = net.addHost('h52', cls=Host, ip='10.5.0.2', defaultRoute=None)
    h53 = net.addHost('h53', cls=Host, ip='10.5.0.3', defaultRoute=None)
    h54 = net.addHost('h54', cls=Host, ip='10.5.0.4', defaultRoute=None)
    h55 = net.addHost('h55', cls=Host, ip='10.5.0.5', defaultRoute=None)
    h56 = net.addHost('h56', cls=Host, ip='10.5.0.6', defaultRoute=None)
    h57 = net.addHost('h57', cls=Host, ip='10.5.0.7', defaultRoute=None)
    h58 = net.addHost('h58', cls=Host, ip='10.5.0.8', defaultRoute=None)
    h59 = net.addHost('h59', cls=Host, ip='10.5.0.9', defaultRoute=None)
    h60 = net.addHost('h60', cls=Host, ip='10.5.0.10',defaultRoute=None)
    
    h61 = net.addHost('h61', cls=Host, ip='10.6.0.1', defaultRoute=None)
    h62 = net.addHost('h62', cls=Host, ip='10.6.0.2', defaultRoute=None)
    h63 = net.addHost('h63', cls=Host, ip='10.6.0.3', defaultRoute=None)
    h64 = net.addHost('h64', cls=Host, ip='10.6.0.4', defaultRoute=None)
    h65 = net.addHost('h65', cls=Host, ip='10.6.0.5', defaultRoute=None)
    h66 = net.addHost('h66', cls=Host, ip='10.6.0.6', defaultRoute=None)
    h67 = net.addHost('h67', cls=Host, ip='10.6.0.7', defaultRoute=None)
    h68 = net.addHost('h68', cls=Host, ip='10.6.0.8', defaultRoute=None)
    h69 = net.addHost('h69', cls=Host, ip='10.6.0.9', defaultRoute=None)
    h70 = net.addHost('h70', cls=Host, ip='10.6.0.10',defaultRoute=None)
    
    h71 = net.addHost('h71', cls=Host, ip='10.7.0.1', defaultRoute=None)
    h72 = net.addHost('h72', cls=Host, ip='10.7.0.2', defaultRoute=None)
    h73 = net.addHost('h73', cls=Host, ip='10.7.0.3', defaultRoute=None)
    h74 = net.addHost('h74', cls=Host, ip='10.7.0.4', defaultRoute=None)
    h75 = net.addHost('h75', cls=Host, ip='10.7.0.5', defaultRoute=None)
    h76 = net.addHost('h76', cls=Host, ip='10.7.0.6', defaultRoute=None)
    h77 = net.addHost('h77', cls=Host, ip='10.7.0.7', defaultRoute=None)
    h78 = net.addHost('h78', cls=Host, ip='10.7.0.8', defaultRoute=None)
    h79 = net.addHost('h79', cls=Host, ip='10.7.0.9', defaultRoute=None)
    h80 = net.addHost('h80', cls=Host, ip='10.7.0.10',defaultRoute=None)
    
    h81 = net.addHost('h81', cls=Host, ip='10.8.0.1', defaultRoute=None)
    h82 = net.addHost('h82', cls=Host, ip='10.8.0.2', defaultRoute=None)
    h83 = net.addHost('h83', cls=Host, ip='10.8.0.3', defaultRoute=None)
    h84 = net.addHost('h84', cls=Host, ip='10.8.0.4', defaultRoute=None)
    h85 = net.addHost('h85', cls=Host, ip='10.8.0.5', defaultRoute=None)
    h86 = net.addHost('h86', cls=Host, ip='10.8.0.6', defaultRoute=None)
    h87 = net.addHost('h87', cls=Host, ip='10.8.0.7', defaultRoute=None)
    h88 = net.addHost('h88', cls=Host, ip='10.8.0.8', defaultRoute=None)
    h89 = net.addHost('h89', cls=Host, ip='10.8.0.9', defaultRoute=None)
    h90 = net.addHost('h90', cls=Host, ip='10.8.0.10',defaultRoute=None)
    
    h91 = net.addHost('h91', cls=Host, ip='10.9.0.1', defaultRoute=None)
    h92 = net.addHost('h92', cls=Host, ip='10.9.0.2', defaultRoute=None)
    h93 = net.addHost('h93', cls=Host, ip='10.9.0.3', defaultRoute=None)
    h94 = net.addHost('h94', cls=Host, ip='10.9.0.4', defaultRoute=None)
    h95 = net.addHost('h95', cls=Host, ip='10.9.0.5', defaultRoute=None)
    h96 = net.addHost('h96', cls=Host, ip='10.9.0.6', defaultRoute=None)
    h97 = net.addHost('h97', cls=Host, ip='10.9.0.7', defaultRoute=None)
    h98 = net.addHost('h98', cls=Host, ip='10.9.0.8', defaultRoute=None)
    h99 = net.addHost('h99', cls=Host, ip='10.9.0.9', defaultRoute=None)
    h100 = net.addHost('h100', cls=Host, ip='10.9.0.10', defaultRoute=None)

    
    
    info( '*** Add links\n')
    net.addLink(s1,  s2)
    ##############################
    net.addLink(h1,  s1)
    net.addLink(h2,  s1)
    net.addLink(h3,  s1)
    net.addLink(h4,  s1)
    net.addLink(h5,  s1)
    net.addLink(h6,  s1)
    net.addLink(h7,  s1)
    net.addLink(h8,  s1)
    net.addLink(h9,  s1)
    net.addLink(h10, s1)
    
    net.addLink(h11, s1)
    net.addLink(h12, s1)
    net.addLink(h13, s1)
    net.addLink(h14, s1)
    net.addLink(h15, s1)
    net.addLink(h16, s1)
    net.addLink(h17, s1)
    net.addLink(h18, s1)
    net.addLink(h19, s1)
    net.addLink(h20, s1)
    
    net.addLink(h21, s1)
    net.addLink(h22, s1)
    net.addLink(h23, s1)
    net.addLink(h24, s1)
    net.addLink(h25, s1)
    net.addLink(h26, s1)
    net.addLink(h27, s1)
    net.addLink(h28, s1)
    net.addLink(h29, s1)
    net.addLink(h30, s1)
    
    net.addLink(h31, s1)
    net.addLink(h32, s1)
    net.addLink(h33, s1)
    net.addLink(h34, s1)
    net.addLink(h35, s1)
    net.addLink(h36, s1)
    net.addLink(h37, s1)
    net.addLink(h38, s1)
    net.addLink(h39, s1)
    net.addLink(h40, s1)
    
    net.addLink(h41, s1)
    net.addLink(h42, s1)
    net.addLink(h43, s1)
    net.addLink(h44, s1)
    net.addLink(h45, s1)
    net.addLink(h46, s1)
    net.addLink(h47, s1)
    net.addLink(h48, s1)
    net.addLink(h49, s1)
    net.addLink(h50, s1)
    
    net.addLink(h51, s2)
    net.addLink(h52, s2)
    net.addLink(h53, s2)
    net.addLink(h54, s2)
    net.addLink(h55, s2)
    net.addLink(h56, s2)
    net.addLink(h57, s2)
    net.addLink(h58, s2)
    net.addLink(h59, s2)
    net.addLink(h60, s2)
    
    net.addLink(h61, s2)
    net.addLink(h62, s2)
    net.addLink(h63, s2)
    net.addLink(h64, s2)
    net.addLink(h65, s2)
    net.addLink(h66, s2)
    net.addLink(h67, s2)
    net.addLink(h68, s2)
    net.addLink(h69, s2)
    net.addLink(h70, s2)
    
    net.addLink(h71, s2)
    net.addLink(h72, s2)
    net.addLink(h73, s2)
    net.addLink(h74, s2)
    net.addLink(h75, s2)
    net.addLink(h76, s2)
    net.addLink(h77, s2)
    net.addLink(h78, s2)
    net.addLink(h79, s2)
    net.addLink(h80, s2)
    
    net.addLink(h81, s2)
    net.addLink(h82, s2)
    net.addLink(h83, s2)
    net.addLink(h84, s2)
    net.addLink(h85, s2)
    net.addLink(h86, s2)
    net.addLink(h87, s2)
    net.addLink(h88, s2)
    net.addLink(h89, s2)
    net.addLink(h90, s2)
    
    net.addLink(h91, s2)
    net.addLink(h92, s2)
    net.addLink(h93, s2)
    net.addLink(h94, s2)
    net.addLink(h95, s2)
    net.addLink(h96, s2)
    net.addLink(h97, s2)
    net.addLink(h98, s2)
    net.addLink(h99, s2)
    net.addLink(h100, s2)


    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s2').start([c0])
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
