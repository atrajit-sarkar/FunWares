import pyfiglet
import time
import os
#Timer text
time.sleep(3)
for i in range(11):
    timer=pyfiglet.figlet_format(f"{10-i}")
    print(timer)
    time.sleep(1)
    os.system("cls")

