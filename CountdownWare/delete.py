import shutil
import os
# Input your directory......
with open(f"{os.getcwd()}/dir.txt") as f:
    dir=f.read()
shutil.rmtree(dir)