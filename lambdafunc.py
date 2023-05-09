#lambda functios are the anonymous function .it is defined by using lambda keyword and has following syntax
#lambda arguments:expression
#example of lambda functions
var=lambda x,y:x*y+y*y
print(var(1,2))
#the wworking of similarities between the general function and lambda function but for writing code in single line we can 
# used lambda functions it is not comulsary to use. lambda functions are commonly used as arguments 


rajmarga=lambda x:x*x
print(rajmarga(1))

iterab=[1,2,3,4]
for item in iterab:
    ram=list(map(rajmarga,iterab))
    print(ram)



