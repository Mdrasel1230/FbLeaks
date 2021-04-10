# coding: utf-8
import re
import requests
import argparse
import sys
from subprocess import PIPE, Popen
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="Give your target facebook id link")
parser.add_argument("-f", "--file", required=True, help="Give your target country leak file")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN+"""
                                                                          
  █████▒▄▄▄▄    ██▓    ▓█████ ▄▄▄       ██ ▄█▀  ██████ 
▓██   ▒▓█████▄ ▓██▒    ▓█   ▀▒████▄     ██▄█▒ ▒██    ▒ 
▒████ ░▒██▒ ▄██▒██░    ▒███  ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
░▓█▒  ░▒██░█▀  ▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
░▒█░   ░▓█  ▀█▓░██████▒░▒████▒▓█   ▓██▒▒██▒ █▄▒██████▒▒
 ▒ ░   ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
 ░     ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
 ░ ░    ░    ░   ░ ░      ░    ░   ▒   ░ ░░ ░ ░  ░  ░  
        ░          ░  ░   ░  ░     ░  ░░  ░         ░  
             ░                                                                   
                                                                          
 ---------------- Coded By Md Rasel Bhuyan ---------------
""")

if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)
args = parser.parse_args()

r = requests.Session()

url = args.url

rget = r.get(url)

bt = BeautifulSoup(rget.content, features="lxml")

html = bt.prettify()

reg = re.findall(r'fb://profile/\d+" property="al:android:url"/>', html)
reg = reg[0]
reg = reg.replace('fb://profile/', '')
reg = reg.replace('" property="al:android:url"/>', '')
print('Target profile id: '+"https://facebook.com/profile.php?id="+reg+"\n")

go = "cat {0} | grep '{1}' | sed 's/\r//g' | tr '\n' ':' ".format(args.file,reg)

def cmdline(command):
	process = Popen(args=command, stdout=PIPE, shell=True)
	return process.communicate()[0]
run = cmdline(go)

if len(run) !=0:
	print("Found!"+"\n")
	run = str(run).replace("b'", "")
	run = str(run).replace("'", "")
	print(run)
else:
	print("BadLuck :) Not Found!")	
