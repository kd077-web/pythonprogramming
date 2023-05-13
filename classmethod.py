'''
while defining a method inside a class it is not mandatory to  define instance of arguments of function instesd
we can directly give instance to class 
'''
class ram:
    position="manager"
    def __init__(self,name):
        self.name=name
    @classmethod    
    def newcompany(cls,anothername):
        cls.position=anothername
    def print_name(self):
        print(f"the name of person is {self.name} and the name of position is{self.position}")  
e=ram("hikmat") 
print(e.print_name())
e.newcompany("tesla") 
print(e.print_name())   
