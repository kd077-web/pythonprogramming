#break and continue are used in iteration  in for loop break is used to terminate the iteration method for
#lopp as per the given condition and continue is used similar in iterative method to skip the given condition and further continue the
#iterative methods following example illustrate the concept of break and continue in python
#lets create a multiplication table of 2
for i in range(12):
    if (i==9):
        break
    print("2*",i+1,"=",2 *(i+1))

#now we use same program to illustrate the concept of  continue too
for i in range(12):
    if (i==5):
        continue
    print("2*",i+1,"=",2 *(i+1))

    
 

    

