''' list is one of the most important and most used data type in python 

'''
marks=[3,4,5,6,7,5,4,4,3,32]
print(marks)
print(type(marks))
print(marks[-5:-3])
if 6 in marks:
    print("yes there is")
print(marks.count(6))  
# we can use jump slicing also as
print(marks[-7:-2:2]) #here jump slicing is used as 2
#list methods 
print(marks.append(4444))

print(marks.insert(1,500000))
m=[1000000,20000]
print(marks.extend(m))#extends m in list l
k=marks+m#joins or concatenate two list
print(k) ,
print(marks.reverse())

