

a=int(input("enter your age "))
if a<=18:
    print("you cannot watch " ,a)
else:
    print("you can watch you are fully eligible") 
a=input("enter the name of student\n")
print("the name of student is\n",a)
b=int(input("enter the roll numbe rof student\n"))
print("the roll number of student is \n",b)
print("enter the each subject marks of student\n")
x=int(input("enter the marks obtained by a student in oop\n"))
y=int(input("enter the marks obtained by a student in discrete structure\n"))
z=int(input("enter the marks obtained by a student in digital logic\n"))
w=int(input("enter the marks obtained by a student in artificial intelligence\n"))
totalmarks=x+y+z+w
print("the total marks obtained by astudent is\n",totalmarks)
if (x<40 or y<40 or  z<40 or  z<40):
    print("the student has failed\n")
elif(x>=40 or y>=40 or z>=40 or w>=40 ):
    print("congratulations the student has passed\n")
else:
    pass 
percent=((totalmarks/400)*100)
print("the total percentage of student is:",percent)

#matchcase statements
ram=int(input("enter any number "))
match ram:
    case 0:#the match case statements is same as switch case statements as in c and c++
        #here break isnot use in case statements as in c and c++
        
        print("you are in case 0")
    case 1:
        
        print("you are in case 1")  
    case 5:
        

        print("you are in case 5")
    case _ if(ram==56):
        print(ram,"it is 56")

    case _ if (ram<30):
        print("this is the required answer")   

    

