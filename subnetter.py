#=============AUTHOR=============#
"""
    Autor:      Víctor Velázquez Cid
    Versión:    Alpha 1.5
    Ult. actualización: 1/1/31
    
    Blog:       liteshut.blogspot.com
    GitHub:     https://github.com/vvelc
    Contacto:   victorvelazquezcid@gmail.com
    
    Titulo:     SUBNETTER 2

"""

#=============IMPORTS=============#
from ipaddress import *
import os
import time

#=============DATA=============#
net = ""
subnets = ""

#=============STRINGS=============#
blank = ""
space = " "
inp = ">>"

#=============COLORS=============#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

#=============FUNCTIONS=============#

def setnet(n1=None):
    global inp, net
    if n1 == None:
        print("Lets set IP Network")
        print("Formats: {0}192.168.1.0{1} or {0}192.168.1.0/24{1}".format((color.CYAN+color.BOLD),color.END))
        inp = '[{}IP{}] >> '.format(color.CYAN,color.END)
        n1 = input(inp)

    if not '/' in n1:
        try:
            n1 = ip_address(n1)
        except:
            print("Error: Invalid ip address")
            return None

    if not "/" in str(n1):
        inp = '[{}Prefix{}] >> '.format(color.CYAN,color.END)
        pr = input(inp)
        try:
            if "/" in pr:
                n1 = str(n1)+pr
            else:
                n1 = (str(n1)+'/'+pr)
        except:
            print("Error: Invalid prefix")

    try:
        net = ip_network(n1)
    except:
        print("Error: Invalid network")
    inp = '[{}{}{}] >> '.format(color.CYAN,net,color.END)

def basic():
    global net
    print(net)
    if net == "":
        print("Error: No network selected")
        return None
    
    #basen = str(net)
    #broad = str(net.broadcast())
    hosts = list(net.hosts())
    #print(list(net.subnets()))
    print("[{}+{}] Base network: {}".format(color.CYAN,color.END,hosts[0]-1))
    print("[{}+{}] Usable Hosts:".format(color.CYAN,color.END))
    count = 0
    l = len(str(hosts[-1]))
    for h in hosts:
        h1 = h
        if count % 2 != 0:
            if (hosts.index(h) < len(hosts)-1):
                h2 = hosts[hosts.index(h)+1]
            print(' [{0}+{1}] {2}'.format(color.CYAN,color.END,str(h)))
        else:
            print(' [{0}+{1}] {2:<15}'.format(color.CYAN,color.END,str(h)), end="")
        count += 1

    print("[{}+{}] Broadcast: {}".format(color.CYAN,color.END,h+1))


def help():
    print("""\
================================== HELP ==================================
/{0}set [ip]{1}  Allows to enter IP // Format: 192.168.10.0 or 192.168.10.0/24
/{0}basic{1}     Shows base net, broadcast, first and last usable hosts
/{0}wipe{1}      Deletes existent data
/{0}clear{1}     Cleans the terminal screen
/{0}help{1}      Shows available commands
/{0}exit{1}      Exit Subnetter
==========================================================================\
""".format(color.CYAN,color.END))

def start():
    print("""\
==================================================================""" + color.CYAN + """
   _____ _    _ ____  _   _ ______ _______ _______ ______ _____  
  / ____| |  | |  _ \| \ | |  ____|__   __|__   __|  ____|  __ \ 
 | (___ | |  | | |_) |  \| | |__     | |     | |  | |__  | |__) |
  \___ \| |  | |  _ <| . ` |  __|    | |     | |  |  __| |  _  / 
  ____) | |__| | |_) | |\  | |____   | |     | |  | |____| | \ \ 
 |_____/ \____/|____/|_| \_|______|  |_|     |_|  |______|_|  \_\\""" + color.END + f"""

[{color.CYAN}+{color.END}] Author: Víctor Velázquez Cid
[{color.CYAN}+{color.END}] Version: Alpha 1.5

Type /{color.CYAN}help{color.END} to see available commands. Type /{color.CYAN}exit{color.END} to exit Subnetter
""")

def clear(close=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if close:
        return None
    start()

def wipe():
    global inp,net,subnets

    inp = ">>"
    net = ""
    subnets = ""

def close():
    clear(True)
    exit()

def cmd(cm):
    com = ""
    arg = ""

    if cm[0] == "/":
        if " " in cm:
            com = cm[1:cm.index(" ")]
        else:
            com = cm[1:]

        if " " in cm and cm[cm.index(" "):] != "":
            arg = cm[cm.index(" ")+1:]

        if com == "clear":
            return clear()
        if com == "wipe":
            return wipe()
        elif com == "set":
            if arg != "":
                return setnet(arg)
            else:
                return setnet()
        elif com == "basic":
            return basic()
        elif com == "exit":
            return close()
        elif com == "help":
            return help()
        else:
            print("Error: Non-existent command")
            return None
    else:
        print("Error: Non-existent command")
        return None

#=============SCRIPT=============#
clear()

#help()

while True:
    opt = input("{} ".format(inp))
    
    if len(opt) == 0:
        continue
    
    if opt[0] != "/":
        print("Error: Este comando no es válido")
        continue
    
    cmd(opt)