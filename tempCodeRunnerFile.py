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