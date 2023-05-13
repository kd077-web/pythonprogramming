#if we want to change the parent class in child class we can use overriding method

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_name(self):
        return self.x*self.y  
class area(shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)
    def print_name1(self):
        return 3.14*super().print_name() #overriden 
    
w=area(4) 
print(w.print_name1()) 

#here in above example we hacve overridden the parent function 
    

