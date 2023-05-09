#in python we can raise custom error by raising keyword raise

a=int(input("enter any number between 5 and 9"))
if(a<5 and a<9):
    raise ValueError("please enterany number between 5 and 9")
#we can raise many errors such as valueerror,memory error,key, index error.....



