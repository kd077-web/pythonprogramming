'''in oop concept while we are defining methods inside class the self argument is not mandatory.for not making it mandatory
we should use static method following example illustrate the concept of static method in python

'''
class animal:
    def __init__(self,name):
        self.name=name
    @staticmethod       #staticmethod  
    def print_name(a,b):
        return (a+b)
    

a=animal("giraffe")
print(a.name)
print(a.print_name(2,3))



 
    

