import os
content=r'''
@echo off

python .\main.py
timeout /t 2 >nul
python .\display.py
python .\timer.py
python .\delete.py
'''

with open(f"{os.getcwd()}/run.bat","w") as f:
    f.write(content)
