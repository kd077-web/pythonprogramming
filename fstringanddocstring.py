ram="my name is {} and i live in {}"
name="hikmat"
place="kathmandu"
print(ram.format(name,place))#format place name variable value in ram variable as my name is hikmat and live in kathmandu
print(f"my name is {name} and i live in {place}")
#it is newly introduced after python 3.6 onwards
price=44.555555
print(f"the price of chocolate is {price:.2f}")
print(f"the price of chocolate1 is {price:.3f}")

#docstring
#docstring has same syntax as multiline comments starting and ending with '''
#it is just written after the function definition otherwise it willnot work
def ram(a):
    '''your value is a, so print a'''
    print(a**2)
ram(5)
print(ram.__doc__)# it will print docstring
def addition(a,b):
    '''the addition of number is possible'''
    return(a+b)
c=addition(3,2)
print(c)
print(addition.__doc__)# it is docstring syntax to print the code inside ''' ''' .
