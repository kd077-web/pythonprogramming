'''
in python if we want to call the function of parent class in the child class we use super keyword  as 
super().func_name of parent class.following example illustrate the concept of super keyword in python
'''
class parent_class:
    def print_parent(self):
        
        print("we are from parent ")
class child_class(parent_class):
    def print_child(self):
        super().print_parent()
        print("we are  child class") 
w=child_class()  
w.print_child()
#you can also inherit the constructor __init__ by using super keyboard
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id  
class programmer(employee):
    def __init__(self,name,id,lang):
        self.lang=lang
        super().__init__(name,id)
r=programmer("ram",33,"maithili") 
print(r.name)                      