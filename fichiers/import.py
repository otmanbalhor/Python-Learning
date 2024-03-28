
import os
import shutil

source = "mountain.jpg"

target = "images/mountain.jpg"

shutil.copy(source,target)
os.remove(source)
