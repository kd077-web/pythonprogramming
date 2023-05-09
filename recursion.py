#recursion is a method to define something in terms of itself.a function that defines itself is called a recusive function.
#following program illustrate the concept of recursion
def fact(n):
    if(n==0):
        return 1;
    else:
        return n*fact(n-1);
y=fact(5)
print("the factorial of a number is",y)