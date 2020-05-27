#encoding in utf-8

#Basic scanner scipt dev by Albouffon.
#Updates will arrive soon, with an other tools.

import socket
import subprocess                  
import errno                       
from datetime import datetime      
import sys                         
 
subprocess.call('clear', shell=True)                              

banner = '''                                                          
 __    __     ______     __   __   ______     ______     __  __    
/\ "-./  \   /\  __ \   /\ \ / /  /\  ___\   /\  __ \   /\_\_\_\   
\ \ \-./\ \  \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __ \  \/_/\_\/_  
 \ \_\ \ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\   /\_\/\_\ 
  \/_/  \/_/   \/_____/   \/_/      \/_____/   \/_/\/_/   \/_/\/_/ 

'''
print(banner)

sock_server = raw_input('\033[31mmoveax>\033[0m Enter the target adresse ip : ')
sock_server_IP = socket.gethostbyname(sock_server)
print '-'*60
print '\033[31mmoveax>\033[0m The IPV4 of the target is : ', sock_server_IP
print '-'*60
print '\033[31mmoveax>\033[0m Please wait, the process is underway on', sock_server_IP,'. . .'
print '-'*60
t1 = datetime.now()

try: 
    for port in range(21, 520) :
        sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=sock_server.connect_ex((sock_server_IP, port))
        if result == 0:
            print 'Port {} is : open'.format(port)
            sock_server.close()

except KeyboardInterrupt:
    print 'U have pressed Ctrl+C.'
    sys.exit()

t2 = datetime.now()
total = t2 - t1
print '-'*60
print '\033[31mmoveax>\033[0m The process ended in ',total, 'second.'
