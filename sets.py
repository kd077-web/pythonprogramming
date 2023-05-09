#set is a collection of well defined objects in which  repition of data is not printable only single value is printed
#the data in a set is printed in arandom order 
ram={2,3,4,5,6,6,6,6,3}
print(ram)
raja={"ramlakhan",1,2,3,"hike,4.66"}
print(raja)
sky=set()# to check that data type is set or not 
print(type(sky))
#methods in set
#union
raju={1,2,3,4}
ram1={6,7,8,9,4,4,4,4,4,4}
city=raju.union(ram1)
print(city)
#update
city2=raju.update(ram1)
print(city2)
#intersection
hikmat={1,2,3,4,5,6,7,8}
hikmat1={1,3,5,9,10,11}
print(hikmat.intersection(hikmat1))
ortan={1,2,3,4,5}
randy={3,4,6,7,8}
print(ortan.update(randy))#update the value of set ortan with the value randy
print(ortan,randy)
#symmetric difference the value that is not common  will print set ortan
print(ortan.symmetric_difference(randy))
print(ortan.symmetric_difference_update(randy)) #update value of ortan
print(ortan,randy)
#disjoin
jug={5,6,7,8,9,0}
hari={5,6,7,8}
print(jug.isdisjoint(hari))
#isdisjoint checks wheather the set is disjoint or not(disjoint) =the sets that has no element in common is called is called disjoint
#super sert
#if the elements in set B has the set of elements of A then it is called superset
print(jug.issuperset(hari))
#add,remove/discard,pop,del,clear
#add adds the value of other set to one 
#remove and discard remove the elements from set remove throws and errror if there is no such elements and discard doesnot
#pop reoves the element from a set. it may remove anything from set 
#del is used to delete a created set
# clear:if we dont want to delete the set but all the elements in a set we can used clear() method
if 5 in jug:
    print("the element is there")
else:
    print("the element is not there")    

