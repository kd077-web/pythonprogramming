'''
 both instance and class variable are used in python oops.
 the instance variable is used for only the instance/single object but the class variable is used for all objects 
 for eg. if we want to display the company name we dont have to create the instance variable for different objects and m
 ethods.following program illustrate the concept the of the instance and class variable.
'''
class animal:
    another_name="ram"
    def __init__(self,name):
        self.name=name
    def rm(self):
        print(f"the name of person is{self.name} and his another name is{self.another_name}")
a=animal("hiki")
print(a.rm())
b=animal("donkey") 
print(b.rm())       
