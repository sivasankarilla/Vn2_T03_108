"""
Tuple:
-----
1.sequence ------> To maintain certain order.

2.Tuple is homogenous and Heterogeneous data type.
Homogenous means ----> By using single data type Ex(integers,strings,float).
Heterogeneous ----> By using Multiple datatype.
EX:(employee details: employee id= 108,employee name = "shankar",employee height = 5.4).

3.Tuple represents by () and (,)cama separated by values ----> parenthesis.

4.Tuple is immutable data type
immutable means -----> value cannot be change
Ex: (employee id = "shankar")

5.Tuple allows duplicate values
Ex:(name = "shankar",name = "satish",name = "shankar")


"""
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print("====tuple allow duplicate values=====")
tuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple2)
print("====tuple length=====")
tuple3=("apple", "banana", "cherry")
print(tuple3)
print("length of the tuple:",len(tuple3))


print("====tuple Constructor=====")
tuple4 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple4)
print("====tuple =====")
#You can access tuple items by referring to the index number, inside square brackets:
tuple5=("apple", "banana", "cherry")
print(tuple5[2])
print("====tuple range indexing=====")
tuple6=("apple", "banana", "cherry",'mango',"tomato")
print(tuple6[2:5])
print("=====tuple in membership=====")
tuple7 = ("apple", "banana", "cherry")
if "apple" in tuple7:
  print("Yes, 'apple' is in the fruits tuple")
print("=======Change Tuple Values====")
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple8=("apple", "banana", "cherry")
x=list(tuple8)
x.append("orange")
tuple8=tuple(x)
print(tuple8)
print("======= adding of two tuples=====")
tuple9=("apple", "banana", "cherry")
z=("orange",)
tuple9 += z
print(tuple9)#When creating a tuple with only one item, remember to include a comma after the item,
             # otherwise it will not be identified as a tuple.
print("=====unpacking of tuple=====")
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
tuple10=("apple", "banana", "cherry") #ex:- packing
# Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(ss,sos,sss)=tuple10
print(ss)
print(sos)
print(sss)
print("====Using Asterisk*===")
#If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list
tuple11=("apple", "banana", "cherry","orange","cherry")
(_2,_3,*_4)=(tuple11)
print(_2)
print(_3)
print(_4)
print("======joing of tuple=====")
tuple12=("apple", "banana", "cherry","orange","cherry")
tuple13=tuple12+tuple10 #adding of two tuples
print(tuple13)
print(tuple10*2)
print("=======tuple methods=======")
tuple14=(1,1,2,2,62,5,52,2,6,1,51,25,51,5)
#count
print("tuple count of 2:",tuple14.count(2))
#index
print("tuple index of 62",tuple14.index(62))
