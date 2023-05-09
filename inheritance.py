
                #HIERARICHAEL INHERITANCE
class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

a = Person("ram", 24)

print("the name of student is",a.name)
print("the age of student is ",a.age)

class student(Person):
    def __init__(self,roll):
        self.roll = roll
b=student(4)   
print("the roll no of student is ",b.roll)
 
class manager(Person):
     def __init__(self,hour):
            self.hour=hour

a=manager(7)  
print("the working hours of manager is ",a.hour)
'''
there are 5 types of inheritance they are
1. single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hierarichael inheritance 
5.hybrid inheritance
1. derived class is inheritated from parent class
2. when two  or more than two base classes are inheritated to single derived classes is called multiple inheritance
3.when derived class is inheritated successively one after another from the successive base class is called multilevel 
inheritance eg grandfather to father to son
4.when many derived classes are created from one base classes then it is called hierarichael inheritance
5. when multiple inheritance isformed and again multiple inheritance is formed by combining the formed derived classes 
and so on is called multiple inheritance 
'''

                                      #MULTILEVEL INHERITANCE

# to inherit properties from grandfather to father and father to son we shold invoke the constructor
class grandfather:
     def __init__(self,grandfathername):
            self.grandfathername=grandfathername
class father(grandfather) :
      def __init__(self,grandfathername,fathername):
            self.fathername=fathername
            grandfather.__init__(self,grandfathername)#invoke
class son(father):
      def __init__(self,grandfathername,fathername,sonname):
            self.sonname=sonname
            father.__init__(self,grandfathername,fathername)#invoke
      def print_name(self):
            print("the name of grandfather is",self.grandfathername)      
            print("the name of father is",self.fathername)
            print("the name of son is",self.sonname) 
a=son("madhav kedar kiran","kedar kiran","kiran") 
print(a.grandfathername)   
a.print_name()
                  #MULTIPLE INHERITANCE

class oop:
      def __init__(self,mark1):
            self.mark=mark1
            
class dsa:
      def __init__(self,mark2):
            self.mark=mark2
class student(oop,dsa):
      def __init__(self,name,mark1,mark2):
            self.name=name
            self.mark1=mark1
            self.mark2=mark2
                        
a=student("kiran",59,66)
print(a.name)
print(a.mark1)
print(a.mark2)

class Animal:
      def __init__(self,breed):
            self.breed=breed
      def show(self):
            print(f"the breed of animal is:{self.breed} " )   

class dog(Animal):
      def __init__(self,breed,species):
            
            self.species=species
            Animal.__init__(self,breed)
      def show(self):
            Animal.show(self)#overridig a method of classs animal
            print(f"the species of dog is:{self.species}")
            
class cat(dog):
      def __init__(self,breed,species,colony):
            self.colony=colony

            dog.__init__(self,breed,species)
      def show(self):
            dog.show(self)
            print(f"the colony of cat is :{self.colony}")
a=cat("germanstephard","limbre","tonga") 
a.show()           
           
      
                      



              
                        
                      
                        
             
            
      


                              




                            














        

