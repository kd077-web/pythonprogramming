#                          MAP
#for applying the same function in different elements we can used map function
#for examlple
#def cube(x):
#    return x*x*x
#list=[1,2,3,4,5]
#newlist=[]
#for item in list:
#    newlist.append(cube(item))
#    print(newlist)
#the above example innclude many operation so we used here map function as
#syntax  map(function,iterable)
def square(x):
    return x*x
l=[1,2,3,4,5]
ram=list(map(square,l))
print(ram)
#here instead for defining a function for code redundancy we can used lambda as 


#                      FILTER

#the synntax of filter is :  filter(funnc,iterable)
#filter is used to select onnly those elements in  a list that matched to if else statements
#                          REDUCE

# to use reduce functions we must import reduce as; from functools import reduce
from functools import reduce
ra=list(reduce(lambda x,y:x+y,l))
print(ra)






 

    

