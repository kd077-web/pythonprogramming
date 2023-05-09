#tuple is almost same as list data type. it is unchangeable.we cannot change the elements in tuple as in lists.
ram=(3,4,5,6)
if 3 in ram:
    print("yes there is in ram variable")
print(ram[3]) 
#for changing the elements in tuple first we convert the tuple into list and then change elements and again we change the list into tuple
countries=("canada","nepal","japan","china")   
temp=list(countries)
temp.pop(0)
print(temp)
countries=tuple(temp)
print(countries)