#encoding in utf-8

#Basic scanner scipt dev by Albouffon.
#Updates will arrive soon, with an other tools. 

import hashlib
import subprocess
import sys
import errno
from datetime import datetime

subprocess.call('clear', shell=True)

banner = '''                                                          
 __    __     ______     __   __   ______     ______     __  __    
/\ "-./  \   /\  __ \   /\ \ / /  /\  ___\   /\  __ \   /\_\_\_\   
\ \ \-./\ \  \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __ \  \/_/\_\/_  
 \ \_\ \ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\   /\_\/\_\ 
  \/_/  \/_/   \/_____/   \/_/      \/_____/   \/_/\/_/   \/_/\/_/ 
'''
print(banner)

while True:
  choice = raw_input('\033[31mmoveax>\033[0m Do u want to [1] encrypt or [2] decrypt a word ? : ')
  if choice == '1':
    print '-'*60
    choice_1 = raw_input('\033[31mmoveax>\033[0m Enter the word u want to encrypt : ')
    print '-'*60
    print '\033[31mmoveax>\033[0m Here are the available hashing algorithms that you can use :'
    print '-'*60
    print '-> sha224 [1] \n-> sha256 [2] \n-> sha1 [3] \n-> sha384 [4] \n-> sha512 [5]'
    print '-'*60
    choice_2 = raw_input('\033[31mmoveax>\033[0m What algorithm options do you want to use ? : ')
    print '-'*60
  
  if choice_2 == '1':
    print '\033[31mmoveax>\033[0m Please wait, the hashing process is underway with the algorithm :', choice_2
    print '-'*60
    result = hashlib.sha224(choice_1).hexdigest()
    print '\033[31mmoveax>\033[0m The process went well, here is the result :',result
    print '-'*60
  
  if choice_2 == '2':
    print '\033[31mmoveax>\033[0m Please wait, the hashing process is underway with the algorithm :', choice_2
    print '-'*60
    result = hashlib.sha256(choice_1).hexdigest() 
    print '\033[31mmoveax>\033[0m The process went well, here is the result :',result
    print '-'*60

  if choice_2 == '3':
    print '\033[31mmoveax>\033[0m Please wait, the hashing process is underway with the algorithm :', choice_2
    print '-'*60
    result = hashlib.sha1(choice_1).hexdigest()
    print '\033[31mmoveax>\033[0m The process went well, here is the result :',result
    print '-'*60

  if choice_2 == '4':
    print '\033[31mmoveax>\033[0m Please wait, the hashing process is underway with the algorithm :', choice_2
    print '-'*60
    result = hashlib.sha384(choice_1).hexdigest()
    print '\033[31mmoveax>\033[0m The process went well, here is the result :',result
    print '-'*60

  if choice_2 == '5':
    print '\033[31mmoveax>\033[0m Please wait, the hashing process is underway with the algorithm :', choice_2
    print '-'*60
    result = hashlib.sha512(choice_1).hexdigest()
    print '\033[31mmoveax>\033[0m The process went well, here is the result :',result
    print '-'*60
    
  if choice == '2':
    print '-'*60
    choice_1 = raw_input('\033[31mmoveax>\033[0m Enter the word u want to decrypt : ')
    print '-'*60
    print '\033[31mmoveax>\033[0m Here are the available algorithms that you can use :'
    print '-'*60
    print '-> sha224 [1] \n-> sha256 [2] \n-> sha1 [3] \n-> sha384 [4] \n-> sha512 [5]'
    print '-'*60
    choice_2 = raw_input('\033[31mmoveax>\033[0m What algorithm options do you want to use ? : ')
    print '-'*60