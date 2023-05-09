##readline methods reads a single line from a line .if we want to read a multtiple line from a line we used loop
#f=open("file1.txt","a")
#text=f.write("stack is a non-primitive linear data structure in which elements are push and popped only from one top called top of stack.")

#print(text)
#f.close()
#f=open("file1.txt",'r')
#while True:
#    text=f.readline()
#    if not text:
#        break
#    print(text)

f=open("file.txt","r")
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    print(line)
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"the marks of stuudent{i} in english subject is:{m1}")
    print(f"the marks of  student{i} in oop subject is:{m2}")
    print(f"the marks of  student {i} in DSA subject is:{m3}")
    #similarly we can use writelines as readlines to write in a file
    #seek,tell() methods
    #seek methhod print from which character we should print 
    #if "ingliana is good " is wrtten in a file and we have used seek(4) then excluding ingl all others characters are rinted
    #and tell function tells an drint that uto how many character have we seeked
    #and truncate is also used to print that how many characters that we have to print
