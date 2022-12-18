import sys
import time
import os
print("Mah-Editor")
print("Exit for '<END>'")
source_code = ""
while True:
    line = sys.stdin.readline()
    if line.startswith("<END>"):
        break
    source_code += line

f = open("text.txt","w+")
f.write(source_code)
def t():
    current_time = time.localtime()
    ctime = time.strftime('%H:%M:%S', current_time)
    return '[' + ctime + ']'
user = os.getlogin( )
f.write(f"\nMah-Editor log: \n time: {t()} , Edited for user: {user}\n")
f.close()
