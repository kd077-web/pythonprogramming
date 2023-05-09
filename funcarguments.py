'''
there are 4 types of function arguments in python they are:
1.  default arguments
2.  keyword arguments
3.  variable length arguments
4.  required arguments 


'''
#default arguments
def adddition(a=3,b=5):
    print("the addition of numbers is",((a+b)/2))
adddition(b=5)  
#keyword arguments
#in keyword arguments the order of arguments doesnot matter in function call eg.  def addition(a=6,b=7): 
#in func call additionn def(b=7,a=3)
#in required arguments we must pass a value  to first argument  eg  def add(a,b=3): add(5)
#variable length arguments
def add(*numbers): # *representstuple and ** represents dictionary
    print(type(numbers))
    for i in numbers:
        print(i)
add(1,2,3,4,5)  

#now using returning a function 
#when we return instead in printing inside function we can assign avariable in func call to print 
def subtract(x,y):
    return(x-y)
c=subtract(5,7)
print(c)
