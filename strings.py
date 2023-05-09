r=''' "ramm is a goood"
oliioiiiiiikk
jkjolklkjjjj
'''
print(r)
#for a multilinne string we use quotqtion trile timmes at start and end
#idexing in string
e="rote hhhh  hhjjj"
print(e[2])
#for loop i string
for character in e:
    print(character)
#string methods     
a="harry* &&&&!!!!! !!!!!"
print(len(a))#len counts how many no of characters are there
print(a.upper())
print(a.lower())
#strings are immutable

print(a.rstrip("!"))#rstrip removes exclamations,powers
#use of replace
print(a.replace("harry","kiran"))
#use of split : its split the given string into lists
print(a.split(" "))
#capitalize : it capitalize the first letter of a word
#center: align the output to center on a given width eg 20 30 it aligns according  it counts the output no and create space
print(a.center(60))
#count: it counts no of strings repeated in a given variable

print(a.count("harry"))
#endswith : it checks wheather the assigned string is ends with the the specefied characters or not 
print(a.endswith("!!"))
#find:find the index of search character
z= "ram i'S  a goodboy.he  is helps neddy one"
print(z.find("is"))
#index and find method are same but if there  is no occurence of searched string then find methods return -1 and index 
#methox raise exception when the search string is not occured
#isalphanum: it returns bool if there is alphanumeric chara in a string or not eg. A a Z z...same as isalpha
#printable checks wheather the string is printable or not
print(a.isprintable())
#isspace:checks wheather a string contain space or nor
#swapcase :swaps the uppercse char to lowercase and uppercase to lowercase










