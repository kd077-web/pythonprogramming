#import
import math
print(math.floor(4.66))
print(math.ceil(4.01))
from math import sqrt,sinh
print(sqrt(25)*sinh(1))

from math import *#(* indicates that we are importing all modules of math such as sqrt,sinh,pi etc.)   
#we can also import in another way like from math import sqrt as s . here we can use s instead of using sqrt
# to see what we can do with math we should do as print(dir(math))
import math
print(dir(math))
#we can use other file program into another file by importing filename a s from list import *,
import python 
python.welcome()#here when we import from another file it is printed two times so to solve this problem 
#use if__name=="__python__" here python is another file which we have imported j