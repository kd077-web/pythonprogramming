from threading import Thread
class Animal(Thread) :
    def dog(self):
        for i in range(5):
            print("hello buddy we all are from child")
g=Animal()
g.dog()

g.start()
g.join()  

for i in range(5):
    print("hello ia am from main thread")  
    