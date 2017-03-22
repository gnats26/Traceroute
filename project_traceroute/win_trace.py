# done in windows
import win_os_check
# import pexpect
# print(os_check.command)
# child = pexpect.spawn('tracert google.com')
#
# while 1:
#     line = child.readline()
#     if not line: break
#     print(line)

# '''THIS METHOD OPENS A CMD WINDOW SUBPORCESS IS GOOD COZ I DONT KNOW'''
# from subprocess import Popen, PIPE
# host = "google.com"
# p = Popen(['tracert', host], stdout=PIPE)
# while True:
#     line = p.stdout.readline()
#     if not line:
#         break
#     print(line)

import os
import json
import subprocess
# out = os.system('tracert google.co.in > output.txt')
file = open("output.txt")
# print(file.read())
with open('output.txt') as f:
    lines = f.readline()
    for lines in iter(f):
        print(lines)
        lines = f.readline()
    f.close()
# reader = open("output.txt")
# with open("output.txt") as fin:
#     content = json.loads(fin.read())
# print(type(content))
# with open("stringJson.txt", "w") as fout:
#     json.dump(content, fout, indent=1)


# print(out)
# batcmd = 'dir'
# result = subprocess.check_output(batcmd, shell=True)
# print(result)


# '''GOT THIS FROM BLOGS.ORACLE'''
# import socket
# def main(dest_name):
#     dest_addr = socket.gethostbyname(dest_name)
#     port = 33434
#     max_hops = 30
#     icmp = socket.getprotobyname('icmp')
#     udp = socket.getprotobyname('udp')
#     ttl = 1
#     while True:
#         recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
#         send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
#         send_socket.setsockopt(socket.SOL_IP,socket.IP_TTL,ttl)
#         message = input("")
#         recv_socket.bind((message.decode(),port))
#         send_socket.sendto(message.encode(), (dest_name,port))
#         curr_addr = None
#         curr_name = None
#
#         try:
#             _, curr_addr = recv_socket.recvfrom(512)
#             curr_addr = curr_addr[0]
#         except socket.error:
#             pass
#         finally:
#             send_socket.close()
#             recv_socket.close()
#
#         if curr_addr is not None:
#             curr_host = "%s (%s)" %(curr_name, curr_addr)
#
#         else:
#             curr_host = "*"
#         print("%d \t %s" %(ttl, curr_host))
#
#         ttl += 1
#         if curr_addr == dest_addr or ttl > max_hops:
#             break
#
#         pass
#
# if __name__ == "__main__":
#     main('google.com')
#