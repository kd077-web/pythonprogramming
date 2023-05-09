#for opening a ile we use open(par1,par2) par1 is filename and par 2 is read(r),write(w) mode,append mode(a)
#READING A FILE
'''f=open("file.txt",'r')#here r mode is default .even if this paramater is not written r  mode will be specefied
text=f.read()
print(text)
f.close()'''
#WRITING IN A FILE
f=open("file1.txt",'w')
text1=f.write("i am not from kathmandu. I am from jwalakhel")
print(text1)
f.close()
#by using with statement we can also read,write or append to a file 
#for example  the pupose of using with statement is that we donot have to close a file
with open("file1.txt",'w') as f:
    f.write("i am from pokhara")