'''
to understand the concept of decorators we should have the following knowledge
1.function can be used as object
2.function can be store in a variable
3.we can passed the function to the parameter of another function
4.we can return a function from a function
5.you can store them in data structures such as hash tables, lists
 '''
                  #EG.FUNCTION TREATED AS OBJECTS

def raja(text):
    print(text.upper())
raja("hello")
rajak=raja #function store in variable
rajak("mountain")

             #EG.PASSING A FUNCTION AS A ARGUMENT  TO  ANOTHER FUNCTION

def to_upper(text):
    print(text.upper())   

def to_lower(text1):
    print(text1.lower())

def all(func):
    fa=func("i am ramlakhan")
    print(fa)

print(all(to_upper))





                               



       
           

           



          
        
                  