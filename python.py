#in python else can be used in forloop and whileloop too.
#for i in range(1):
#    print("you have range ")
#else:
#    print("you donot have range")   
#
#for i in range (4) :
#   if i==2:
#        break;
#   print(i)
#else:
#    print('unchocky')


ques1=["what is the capital city of nepal?","1.lalitpur",'2.kathmandu',"3.pokhara","4.bhaktapur"] 
ques2=["what is the condition whwn we try to push elements in stack although it is full?","1.stack underflow","2.stack overflow","3.both","4.none"]
ques3=["8848 microprocessor consists of how many pins?","1.20 pins","2.39pins","3.19pins","4.40pins"]
print("what is the capital city of nepal?\n 1.lalitpur\t\t\t2.kathmandu\n3.pokhara\t\t\t4.bhaktapur")
b=int(input("choose a number between 1 and 4"))
cash=[1000,2000,3000,10000,20000,50000,320000]

match(b):
        case 1:
            if(ques1[1]):
                print("you have choosen wrong answer ")
                print("you are out of game")
        case 2:   
            if(ques1[2]):
                print("you have choosen right answer")
                print("you have won rs.1000")
                
        case 3:
            if(ques1[3]) :
                print("you have choosen wrong answer")
                print("ypu are out of game")    
        case 4:
            if(ques1[4]) :
                print("you have choosen wrong answer")  
                print("you are out of the game")
        case _ :  #default
            print("out of scope,please enter a number within range between 1 and 4")

questions=[
    ["what is the capital of nepal","kathmandu","pokhara","biratnagar","bhaktapur"],
    ["how many pins are there in microprocessor 8848","19","40","20","39"],
    ["what is a chromatic number of c6","2","3","6","4"],
    ["what is the symbol of conjuction","^","<",">","^^"]
]  
levels=[1000,2000,3000,10000,40000,100000,300000]
for i in range(0,len(questions)):
    print(f"{questions[i]}\n1.{questions[i][0]}\t\t  ")



def welcome():
    print("you are warm welcome")

if __name__=="__python__":
    welcome()        





      



      

