"""
Set:
---
1.Set is unordered collection of elements , represnented {}
2.It doesn't allow duplicate values
3.Indexing and Slicing are not possible
4.Set is immutable

eg:a={1,2,2,3}
print(a)
{1,2,3}
"""
print("======= sit =======")
set1={13,5,85,5.2,54,515,5,5,13,5.2,515}
print(set1)
print("=====membership ======")
set2 = {"apple", "banana", "cherry"}
print("banana" in set2)
print("=======Add Set Items======")
#To add one item to a set use the add() method
set3= {"apple", "banana", "cherry"} #add
set3.add("orange")
print(set3)
print("======add sets======")
#To add items from another set into the current set, use the update() method.
set4={"apple", "banana", "cherry"}
set5={1,2,3.5,35,642,55}
set4.update(set5)
print(set4)
print("======Add Any Iterable======")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print("=====set methods======")
#add()
# Adds an element to the set
set6={"apple", "banana", "cherry"}
print("before add :",set6)
set6.add("orange")
print("after add :",set6)
#clear()
#Removes all the elements from the set
set7={152,2502,520,3.02,"shankar"}
print("before clear:",set7)
set7.clear()
print("after clear:",set7)
#copy()
#Returns a copy of the set
set8={"apple", "banana", "cherry"}
print("before copy",set8)
set9=set8.copy()
print("after copy:",set9)
#difference()
#Returns a set containing the difference between two or more sets
set9={"apple", "banana", "cherry"}
set10={"shankar", "banana", "mani"}

print("before difference of set9,set10",set9,set10)
print("after the difference of set9-set10:",set9.difference(set10))#this is equal to print(set9-set10)
print("after the difference of set10-set9:",set10.difference(set9))
#pop,discard,remove                                 difference
#pop-->Removes an element from the set    Remove the last item by using the pop() method:

#discard-->Remove the specified item        If the item to remove does not exist,
                                            # discard() will NOT raise an error.


#remove-->Removes the specified element     If the item to remove does not exist,
                                                # remove() will raise an error
set10={"apple", "banana", "cherry"}

set10.pop()
print(set10)
set11={"apple", "banana", "cherry"}
set11.remove("banana")
print(set11)
set12={"apple", "banana", "cherry"}
set12.discard("shankar")
print(set12)
#difference_update()
'''The difference_update() method removes the items that exist in both sets.

The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
#intersection()
#Return a set that contains the items that exist in both set x, and set y:

x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z1 = x.intersection(y1)

print(z1)



