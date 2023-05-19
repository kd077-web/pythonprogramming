'''
multitasking means doing multiple tasks.there are two types of multitasking they are
1.process based multitasking
2.thread based multitasking
 process based multitasking can be expalained on basis of os in pc.here we can perform differrent or open different operations such
 as. opening youtube,using vs code,using notrpsd,independently .

 in thread  based multitasking each task in a  same program has seperate flow of execution which are independent of another.
 eg. many account holders of state bank of nepal are withdrawing,crediting or performing different operations through mobile 
 banking at same time independently this is a concept of multithreading.
'''

          # main thread
          
 #whenever we wrote a program it is a main thread
 # eg.
import threading
t=threading.current_thread().getName() #this gives which type of thread is used
print(t)
print("i am ramlakhan")  
                 #Creating a thread without using a class
'''
thread class of threading module is used to create threads.to create our own thread we need to create object of 
thread class
following are the ways to create the threads.
1.creating a thread without using a class
2.creating athread using a child class to thread class 
3.creating a thread without using a child class to thread class
'''  
'''                 1.
for creating a thread class we need to import as:
from threading import Thread
here Thread is a class and now we should create a thread object and use as:
syntax: anythread_object=Thread(target=function_name,args=(arguments)) here args must be tuple
to start a thread or call we need to use start() as: objectname.start()
following program illustrate the concept of thread
'''
from threading import Thread
def disp(a,b):
    print("this is a child thread", a,b)
t= Thread(target=disp,args=(1,2))#thread object 
t.start()   
print("success")#mainthread
#its thread cannot be determined which will be printed one after another either main thread or child thread


                       #SET AND GET THREAD NAME
#current_thread,getName(),setName(name)
#current thread :this function return current thread object

from threading import Thread,current_thread
def raj():
    print("i am from achild thread",current_thread().getName()) 
e=Thread(target=raj)
e.start()      
print("i am from main thread",current_thread().getName())
# by using  current_thrwad().name we can also get the name of thread
          #2. creating a thread to by creating a cclass
from threading import Thread
class rak(Thread):
    def method(self):
        print("w e are from only a child class")
t=rak() 
t.start() 
#start() run()   and join()
#join: the func of join thread is to execute the child thread then only other threads 
from threading import Thread
class Animal(Thread) :
    def dog(self):
        for i in range(5):
            print("hello buddy we all are from child")
g=Animal()

g.start()
g.join()  

for i in range(5):
    print("hello ia am from main thread")  
    
            
    
                                     
