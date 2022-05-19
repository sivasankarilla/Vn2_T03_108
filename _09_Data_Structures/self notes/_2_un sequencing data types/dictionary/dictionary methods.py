"""

Method	                    Description
clear()---->	  Removes all the elements from the dictionary
copy()---->	      Returns a copy of the dictionary
fromkeys()---->	  Returns a dictionary with the specified keys and value
get()---->	      Returns the value of the specified key
items()---->	  Returns a list containing a tuple for each key value pair
keys()---->	      Returns a list containing the dictionary's keys
pop()---->	      Removes the element with the specified key
popitem()---->	  Removes the last inserted key-value pair
setdefault()----> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()---->	  Updates the dictionary with the specified key-value pairs
values()---->	  Returns a list of all the values in the dictionary
"""
print("======clear=======")
car = {"brand": "Ford","model": "Mustang","year": 1964}
print("before clear:",car)
car.clear()
print("after claer:",car)



print("======copy=======")
car1 = {"brand": "Ford","model": "Mustang","year": 1964}
print("before copy:",car1)
car2=car1.copy()
print("after copy:",car2)



print("======formkeys=======")
#dict.fromkeys(keys, value)
x3=("apple","mango","banana","cherry")
y3=(100)
z3=dict.fromkeys(x3,y3)
print("after fromkeys:",z3)



print("======get()=======")
car4 = {"brand": "Ford","model": "Mustang","year": 1964}
print("before get:",car4)
car5=car4.get("year")
print("after get year:",car5)

#ex:-
print("====ex2=====")
car6 = {"brand": "Ford","model": "Mustang","year": 1964}
x5 = car6.get("price", 15000)
print(x5)



print("======items()=======")
car7 = {"brand": "Ford","model": "Mustang","year": 1964}
print(car7.items())



print("======keys=======")
car8 = {"brand": "Ford","model": "Mustang","year": 1964}
print(car8.keys())


print("======pop=======")
#dictionary.pop(keyname, defaultvalue)
car9 = {"brand": "Ford","model": "Mustang","year": 1964}
car9.pop("model")
print(car9)


print("======popitem=======")
car10 = {"brand": "Ford","model": "Mustang","year": 1964}
car10.popitem()
print(car10)


print("======setdefault=======")
#dictionary.setdefault(keyname, value)
car11 = {"brand": "Ford","model": "Mustang","year": 1964}
s=car11.setdefault("model","shankar")
print(s)

print("======update=======")
#dictionary.update(iterable)
car12 = {"brand": "Ford","model": "Mustang","year": 1964}
car12.update({"colour":"black"})
print(car12)


print("======values=======")
car13 = {"brand": "Ford","model": "Mustang","year": 1964}
v=car13.values()
print(v)

#ex:-
car14 = {"brand": "Ford","model": "Mustang","year": 1964}

y = car14.values()

car14["year"] = 2018

print(y)