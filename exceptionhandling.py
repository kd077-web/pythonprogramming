#try and except are the exception handling terms used to handled the error in program.
#finally is a clause that is also used as with try and except statements in python
try:
    l=[1,2,3,4]
    i=int(input("enter the index number :"))
    print(l[i])
except:
    print("the operation has been failed")    
finally:
    print("this keyword is always executed")    #this keyword is always executed along with try or except 
    
   