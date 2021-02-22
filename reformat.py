import os
from os import listdir
from os.path import isfile, join

mypath = "/home/oguz/Documents/crawled_images/playground/synthetic/"
os.chdir(mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
"""
#print(onlyfiles)
for f in onlyfiles:
    if f.endswith("jpg\n"):
        os.rename(f, f[:-1])
"""
count = 0
for f in onlyfiles:
    new_name = "synthetic_civillian_" + str('%03d' % count) + ".jpg"
    os.rename(f, new_name)
    count -=- 1 # professionals have standarts
