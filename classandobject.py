class person:
    name=input("ennter person name")
    age=int(input("enter your nage"))
a=person()
print(a.name)
print(a.age)

#syntax of class and object in oop
# class class_name:
#    dsts
#    function
#object creation 
#a=class_name() here a is object
class pers:
    
    def ra(self):
        print(f"the name of student is {self.name}" )
a=pers()
b=pers()  
a.name="subham"  
b.name="rajan"
print(a.ra())
print(b.ra())

class Person:
      def __init__(self, name, age):#the _init_function is used if we want to assign the value in object creation
          self.name = name
          self.age = age

p1 = Person("John", 36)#here value is assigned in object creation

print(p1.name)
print(p1.age)  

# self is always written as arguments to specify each object when there are multiple objects

                      #constructor : the functions as same name as class name,initialization 
#the _init_method is a constructor.it is called automatically called during object creation
#there are two types of constructor in python they are 1. parametrized constructor 2. default constructor parametrized con
#structor takes arguments while using a init function but default constructor doesnot takes any arguments






       



        










    