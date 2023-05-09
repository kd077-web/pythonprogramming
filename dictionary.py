#dictionary is also one of the most used datatype in python . it consists of key and values.it is most used data type in django

ram={"school":"crystal","place":"kathmandu"}
print(ram)
z=ram.keys()# print the keys of variable ram
print(z)
print(ram.values())
print(ram["school"])
#    or
print(ram.get('place'))
#after the python 3.7 the dictionary is ordered - b 
#update
employeeid={1:23,2:33,3:33,4:43}
employeeid1={8:66,6:77,5:87,7:97}
employeeid.update(employeeid1)
print(employeeid)
#this method id different other than set as it is print in ordered
#for clearing the key and values from dictionary we use clr() eg. ep1.clr()
#to remove item from the key and values we use pop eg. ep1.pop(key)
#for removing last item from the dictionary we use popitem()
#for deleting the dictionary we use del eg del ep1



