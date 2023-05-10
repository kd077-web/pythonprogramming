                # ROCK,SCRISSORS,PAPERS  GAME
'''
assume 1= rock ,2=paper and 3=scrissors
let there are two players computer and user itself
user  


'''
import random
user=int(input("enter 1 for rock or 2 for paper or 3 for  scrissors \n"))
comp=random.randint(1,3)#randit is a function that is used to generate the random numbers in a given range 
print("user:",user)
print("computer:",comp)
def check(comp,user):
    if(comp==user):
        return 0 #draw
    if(user==1 and comp==2):
        return -1# userlose
    if(user==2 and comp==3):
        return -1# user lose
    if(user==3 and comp==1):
        return -1 # user lose
    
cal=check(comp,user)
if(cal==0):
    print("its a draw match play more")  
elif(cal==-1):
    print("computer have won the game")
else:
    print("user have won the game")
          
   
    
 


    
    
