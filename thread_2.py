'''
creating a constructor in thread child classs

'''
from threading import *
class Animal(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("child class constructor",a)
e=Animal(5)
e.start()
print("main thread")
             
'''
creating a thread without using a child class
syntax:
class class_name:
    statements
obj_name=class_name()
obj_thread=Thread(target=obj_name.func_name,args=(arguments))


''' 
#                 multi tasking using a thread(multithreading) this is single threading
from threading import Thread
class hotel:
    def __init__(self,take_order,serve_order) :
        self.take_order=take_order
        self.serve_order=serve_order
    def show(self):
        for i in range(0,3):
            print(f"{self.take_order}",i) 
            print(f"{self.serve_order}",i)
t=hotel("take order from table","serve order to table")
y=Thread(target=t.show) 
y.start()
print("successfully takeed and served the order")      
# in above examole the progrma is not mistake but the use ofn program is wrong this is race condition of a program
              # multi threading program

#from threading import Thread,current_thread
#class flight:
#    def __init__(self,available_seat):
#        self.available_seat=available_seat
#    def show(self,need_seat):
#        name=current_thread.name()
#        print(f"{need_seat} seat  is needed for{name} ")
#        print(f"{self.available_seat} is available for {name}")
#t=flight(1) 
#d=Thread(target=t.show,args=(1,),name='rahul')
#e=Thread(target=t.show,args=(1,),name='ram')
#d.start()
#e.start()
'''
in multithreading race condition arises the unexpected output sequence appearrs this thread race condition
is eliminated by using thread synchronization.
this problem appears when many threads deals with single objectso the thread synchronization solve by using using single th
read for single object until the threads object doesnot finished.
there are fllowing techniques to do thread synchronization they are:
1.using locks
2.using rlocks
3.using semaphores and bounded semaphores


'''
         # using locks
'''
locks are two types acquire and release .acquire locked the object for the current thread and after releasse current thread
will be unlocked and 
another thread is locked and finally the output will be printed in desired sequence matter
semaphore is used when we wsnt to locked either 2 ,3 or 4 thread at once and other respectively.


'''
from threading import Thread,current_thread
class flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
    def show(self,need_seat):

        if self.available_seat >= need_seat:
            name=current_thread().name
            print(f"the seat is available for{name}")
            self.available_seat =self.available_seat - need_seat
        else:
            print("sorry the seat is not available at the moment")
e=flight(1) 
r=Thread(target=e.show,args=(1,),name='rahul')
l=Thread(target=e.show,args=(1,),name='sonam')
r.start()
l.start()
print("hi i am from main thread")
#here race condition is seen so for removing race condition

from threading import *
class flight:
    
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.b=RLock()
    def show(self,need_seat):

        self.b.acquire()
        if self.available_seat >= need_seat:
            name=current_thread().name
            print(f"the seat is available for{name}")
            self.available_seat =self.available_seat - need_seat
        else:
            print("sorry the seat is not available at the moment")
        self.b.release()    
e=flight(1) 
r=Thread(target=e.show,args=(1,),name='rahul')
l=Thread(target=e.show,args=(1,),name='sonam')

r.start()
l.start()
r.join()
l.join()
print("hi i am from main thread")
# in rlock there is searate acquire and release for differrent threads.so there must be multile acquire and release for
#2 threads
#semahore acquire and release for selected threads among many threads.suppose there are 5 threads and we want to execute 2 
#threads than it can be done bysemaphore ,bounded semaphore(should acquire and release as same as many threads.)










                
                
            







                        

       