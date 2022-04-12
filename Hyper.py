## Terminal by unofficialdxnny
import os
import platform
import getpass
from datetime import datetime
import time
import random


platform = platform.platform()


class bcolors:
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

now = datetime.now()

 
   

banner = f'''
 ██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗             
 ██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗        
\033[91m ███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝  
\033[94m ██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗
\033[94m ██║  ██║   ██║   ██║     ███████╗██║  ██║  
\033[94m ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝
\033[94m \033\033[94mCreated by unofficialdxnny \033[1;31m(\033[1;33mDanial Ahmed\033[1;31m)
\033[93m Currently running on {platform}    
'''



username = getpass.getuser()




os.system('cls')
print(banner)
os.system('title Hyper - unofficialdxnny')

description = '''

Hey! Im unofficialdxnny and this is 'Hyper'

Hyper can be used to execute entered commands
perform advanced administrative functions. 
Hyper can also be used to troubleshoot and solve certain kinds of Windows issues.

'''
while True:
    

    maininput = input(f' Hyper@{username}> ').lower()
    os.system(f'{maininput}')


    if maininput == 'cls':
        os.system('cls')
        print(banner)

 

    elif maininput == '':
        print('')
        print(' Please enter a command than press enter')
        time.sleep(1)
        os.system('cls')
        print(banner)
        print('')

    elif maininput == 'hyper':
        print('')
        print(description)
        print('')
