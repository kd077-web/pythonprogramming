#for using a time module in your program you should first import time.fo;;owing program/eg. illustrate the concept of ti
#me module
# 
#             time.time(): print the time in seconds from 1970s to tillnow
from time import time,ctime,localtime
import time
def usingwhile():
    i=0
    while i<2300:
        i=i+1
        print(i)
def usingfor():
    for i in range(2300):
        print(i) 
init=time.time()        
usingwhile()
print(time.time()-init)
init=time.time() 
usingfor()       

print(time.time()-init)

                        #time.sleep(seconds)
print(5) 
time.sleep(3)
print("this is displayed after 3 seconds")


#              time.strftime():
# it format the time on basis of given string

t=time.localtime() # localtime gives the time of localplace
f=time.strftime("%y-%m-%h",t)
print(f)

epoch=time()
print(epoch)
print(ctime())
str=localtime()
print(str.tm_mon)
print(str.tm_mday)
print(str.tm_year)
                   # datetime class
from datetime import datetime
dt=datetime(year=2023,month=14,day=31)  
dt1=datetime(2022,5,23) 
print(dt)    
print(dt1) 
   #datetime.now():it gives the current date,time or datetime.today() 
   # similarly we have dateclass and timeclass aswell
   #time delta           

 


