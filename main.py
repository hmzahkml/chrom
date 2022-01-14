

import os
import time
import socket
import sys
import ctypes
import subprocess
import shutil
import zipfile
import hashlib
import argparse
import getpass
import re
import inquirer
import time
import password



sys.stdout.flush()
os.system('color 0A')
NOERROR = open(os.devnull, 'w')
VERSION =1.0
BVHRUN = "\BrowsingHistoryView.exe"

def banner():
    os.system('color 0A')

    print('''
    
                - - - - - - - - - - - - - - - - - - - 
 
                       ###                       ##
 #####                  ##                   #   ##
##   #                  ##                  ##
##      ### #  ###    ####  ### ##   ###   #### ###   ####  #####
##       #### ## ##  ## ##   ## ##  ## ##   ##   ##  ## ###  ## ##
##  ###  ##    ####  ## ##   ## ##   ####   ##   ##  ##  ##  ## ##
##  ##   ##   ## ##  ## ##   ## ##  ## ##   ##   ##  ### ##  ## ##
 #####  ####   #####  #####   #####  #####   ## ####  ####  ### ###



                     ##
#####                ##               #    ###  ## ## ## ##
 ## ##                               ##   ## ## ## ## ## ##
 ## ## ### #  ####  ###  ###   ###  ####     ## ## ## ## ##
 ####   #### ## ###  ## ## ## ## ##  ##     ##  ## ## ## ##
 ##     ##   ##  ##  ## ##### ##     ##    ##
 ##     ##   ### ##  ## ##    ###    ##   ##### ## ## ## ##
####   ####   ####   ##  ####  ####   ##  ##### ## ## ## ##
                     ##
                    ##

                - - - - - - - - - - - - - - - - - - - 
                     H A M Z A
                                v{}
                - - - - - - - - - - - - - - - - - - -
    
    
    '''.format(VERSION))


def get_browser_history():
    """Collect the browser history"""
    print("[+] Getting User Browsing History\n", flush=True)
    bhv_exe_path = os.path.realpath('.')  + BVHRUN
    bhv_param = " /SaveDirect /sort 3 /VisitTimeFilterType 1 /cfg " + "BrowsingHistoryView.cfg /scomma "+os.path.realpath('.')+"/memory/BrowsingHistoryView.csv  "
    bhv_command = bhv_exe_path + bhv_param
    bhv_run = bhv_command
    
    subprocess.call(bhv_run, stderr=NOERROR)
    
def get_browser_history2():
    """Collect the browser history"""
    print("[+] Getting User Browsing History\n", flush=True)
    bhv_dir = os.path.realpath('.') + "\\BrowsingHistoryView\\"
    bhv_exe_path = bhv_dir + "BrowsingHistoryView.exe"
    bhv_param = " /SaveDirect /sort 3 /VisitTimeFilterType 1 /cfg " + "BrowsingHistoryView.cfg /scomma " + CASEFOLDER + "/LiveResponseData/BasicInfo/BrowsingHistoryView.csv  "
    bhv_command = bhv_exe_path + bhv_param
    bhv_run = bhv_command
    subprocess.call(bhv_run, stderr=NOERROR)

def mem_scrape():
    os.system('color 0A')
    """Acquires a raw memory dump from the target system"""
    print("[+] Memory acquisition\n", flush=True)
    # variable to point to the "memory" subdir of current directory
    mem_dir = os.path.realpath('.') + "\\memory\\"
    print (mem_dir)
    # setting up variables to run winpemem with different parameters
    mem_acq_get = mem_dir + "winpmem_mini_x64_rc2.exe "+mem_dir+"\\memdump.raw"
    # executing winpmem
    subprocess.call(mem_acq_get, stderr=NOERROR)

def has_admin_access():
    """Admin rights check and exit if they are not found """
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print("\n[+] Has Local Admin rights? [NO]\n")
        open("DFIRTriage must be ran as Local ADMIN.txt", 'w')
        sys.exit(0)
    else:
        print("\n[+] Has Local Admin rights? [YES]")


def choices():
        os.system('color 0A')
        questions = [
        inquirer.List('answer',
                        message="What artifacts do you need?",
                        choices=['browsing history', 'cached imaages', 'memory key finds', 'passwords', 'emails', 'Exit'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        return (answers["answer"])
        
    

def yesno():
        os.system('color 0A')
        confirm = {
        inquirer.Confirm('confirmed',
                        message="Do you want to acquire the memory ?" ,
                        default=True),
        }
        confirmation = inquirer.prompt(confirm)
        return (confirmation["confirmed"])

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def passwordd():
    """Collect Passwords"""
    print("[+] Getting Passwords\n", flush=True)
    excute = "py.exe" + " .\password.py"
    subprocess.call(excute, stderr=NOERROR)
    print("hiiiii")


sys.stdout.flush()
VERSION =1.0
#has_admin_access()
while True:
    clearConsole()
    os.system('color 0A')
    banner()
    if yesno()==True:    
        mem_scrape()
    cohice=choices()
    if cohice=='browsing history':
       #call browsing history function
        print ("here we show you the browsing history ") 
        get_browser_history()
        time.sleep(5)
    if cohice=='cached imaages':
       #call browsing history function
        print ("here we show you the cached imaages ") 
        time.sleep(5)
        
    if cohice=='memory key finds':
       #call browsing history function
        print ("here we show you the results of the keyFinds") 
        time.sleep(5)
        


    if cohice=='passwords':
        #call browsing history function
        print ("here we show you the results of the passwords") 
        time.sleep(5)    
        passwordd()
        yesno()
        
    if cohice=='Emails':
       #call browsing history function
        print ("here we show you the Emailes ") 
        time.sleep(5)
        
    if cohice=='Exit':
       #call browsing history function
        print ("bye bye ") 
        sys.exit(0)
        
    
    