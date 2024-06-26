import os
content1=r'''
@echo off

python .\main.py
'''
content2=r'''
@echo off

python .\display.py
'''
content3=r'''
@echo off

python .\timer.py
'''
content4=r'''
@echo off

python .\delete.py
'''

with open(f"{os.getcwd()}/main.bat","w") as f:
    f.write(content1)
with open(f"{os.getcwd()}/display.bat","w") as f:
    f.write(content2)
with open(f"{os.getcwd()}/timer.bat","w") as f:
    f.write(content3)
with open(f"{os.getcwd()}/delete.bat","w") as f:
    f.write(content4)
