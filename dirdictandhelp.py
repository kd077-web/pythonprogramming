# dir() :it lists all all the attributes and methods of a given list,dictionary or any other data types
#including dunder method (dunder method are __ type methods)
x=[1,2,3,4,5]
print(dir(x))
print(x.__init__)

     #__dict__ this method print all values in form of dictionary

     #help: this method gives all documentation that you have print
class person:
    def __init__(self,anme):
        self.anme=anme
a=person("ram") 
print(a.anme) 
print(help(person))      

