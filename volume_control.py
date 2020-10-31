import sounddevice as sd
import numpy as np
import os
from time import sleep
def decrease(a):
    os.system("nircmd.exe changesysvolume -3000")
    #sleep(1)
    print(a)
    return
def increase(a):
    #os.system("nircmd.exe changesysvolume +5000")
    os.system("nircmd.exe setsysvolume 65000")
    #sleep(1)
    print("up")
    return

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    #print(int(volume_norm))
    vol=int(volume_norm)
    
    if(vol>=250):
        decrease(vol)
    elif(vol<70):
        increase(vol)
    else:
        pass
       
with sd.Stream(callback=print_sound):
    a=1000*3600
    sd.sleep(2*a)
