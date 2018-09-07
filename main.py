import sys
import time
import urllib.request
from appscript import app, mactypes
from random import randint
import os



def set_desktop_background(file):
    se = app('System Events')
    desktops = se.desktops.display_name.get()
    #app('Finder').desktop_picture.set(mactypes.File(file))
    for d in desktops:    
        desk = se.desktops[d]    
        desk.picture.set(mactypes.File(file))

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()
    

def save(url):    
    random = randint(0, 1)
    filename = str(random)+".jpg"
    urllib.request.urlretrieve(url, filename, reporthook)
    print("\nfinito")
    set_desktop_background(filename)
    for i in range(0,2):
       if os.path.isfile(str(i)+".jpg") and i != random:
           os.remove(str(i)+".jpg")
    set_desktop_background(filename)


save("https://source.unsplash.com/random",)

