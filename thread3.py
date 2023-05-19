#thread communication:two or more threads communicate with each other
#1.event 
#2.condition 
#3.queue
#one threads signal an event and others wait for it..
#event have internal flag set()methods true turn on flag and clear() method turn off the flag.when wait()func is call
#it block until flag is true.
from threading import *
from time import sleep

def switch_light():
    sleep(3)
    e.set()
    
    
    print("green light is on")
    sleep(3)
    print("red light is on")
    
    e.clear()
def switchoff() :
    e.wait()
    while e.is_set():
        print("you can go")
    print("done")        
e=Event()
t1=Thread(target=switch_light)
t2=Thread(target=switchoff)
t1.start()
t2.start()


