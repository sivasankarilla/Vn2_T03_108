#_01_list length by use len()

print("=====length of the list====")
list1=[1,2,3,5,8]
print(len(list1))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
print("======= list construction======")
list2=((1,21,3,6,5,6,))
print(list(list2))

# method
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	                              Description
append()	        Adds an element at the end of the list
clear()	            Removes all the elements from the list
copy()	            Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()	        Add the elements of a list (or any iterable), to the end of the current list
index()             Returns the index of the first element with the specified value
insert()	        Adds an element at the specified position
pop()	            Removes the element at the specified position
remove()	        Removes the item with the specified value
reverse()	        Reverses the order of the list
sort()	            Sorts the list
"""
# append
print("=====append=====")
list3=[1,2,3,5,6]
print("before append:",list3)
list3.append(8)
print("after append:",list3)

# extend
print("=======extend=====")
list4=[1,2,3,5,6,9]
print("before extend:",list4)
list4.extend([10,50,62,35])
print("after extend:",list4)

#.clear()
print("=======clear======")
list5=[95,52,65,644]
print("before clear:",list5)
list5.clear()
print("after clear:",list5)
#copy
print("======copy======")
list6=["siva","kishore",154,3142.5,785]
print("before copy:",list6)
list7=list6.copy()
print("after copy",list7)
print(id(list6),id(list7)) #different id's was created
#count
print("======= count =======")
list8=[1,2,3,5,6,1,3,1,5,3,6]
print(list8)
print("how many times 1 repated:",list8.count(1))#use print in count
#index()
print("======= index ======")
list9=[4,5,6,8,65,255,155,641,752]
print(list9)
print(list9.index(5)) #indexing is used to know the indexing position of the value

print("=======insert=======")
list10=["mango","banana","apple"]
print("before insert",list10)
list10.insert(2,"coconut")
print("after insert",list10) #To insert a new list item, without replacing any of the existing values,

print("=====pop=====")
#The pop() method removes the specified index.
list11=[11,"may",10.2,45,65]
print("before pop",list11)
list11.pop(1)
print("after pop",list11)
#If you do not specify the index, the pop() method removes the last item.
list11.pop()
print("after pop with out index",list11)
print("=====remove=====")
#The remove() method removes the specified item.
list12=["banana","mango","coconut","apple"]
print("before remove:",list12)
list12.remove("coconut")
print("after remove:",list12)
print("=====reverse=====")
#
list13=['shankar','sai','swamy','nagu']
print("before reverse:",list13)
list13.reverse()
print("after reverse:",list13)
print("=====sort=====")
#The reverse() method reverses the current sorting order of the elements
list14=["tarun","nagu","kumar","sadhguru"]
print("before sort:",list14)
list14.sort()
print("after sort",list14)
print("=====sort.reverse=====")
list15=["tarun","nagu","kumar","sadhguru"]
list15.sort(reverse = True)
print("sort reverse:",list15)

