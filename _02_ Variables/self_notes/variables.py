"""
variables----> store the data.
---->variable is a name that is used to refer to memory location.
                            (or)
     variables is containers for store data values

memory allocation:
-----------------
# variable to store heap mechanism.
# stack memory and heap memory.
# stack memory  by using to store the variables (names).
# heap memory by using to store the values.
a = 10

# variable declaration:
----------------------
# valid a,A,string(name),a1,name_123,_name123
# in valid numbers not accepted,a1@

#multi words variable names:
---------------------------
---->camel case
#each word, except the first,start with acapital letter.
ex:-myNameIs="shankar"
---->pascal case
#each word start with a capital letter.
ex:-MyNameIs="shankar"
---->snake case
#each word separated by an underscore character
ex:-my_name_is= "shankar"
a = 10
print(a)

name = "shankar"
print(name)

A = 10
print(A)

a1 = 123
print(a1)


_name123 = "shankar"
print(_name123)


"""
print("====creating variables=====")
x=10            #x is of type int          #this is write operation
y="shankar"     #y is now of type  str
print(x)                                   #this is read operation
print(y)

print("======casting======")
x2 = float(5)
X2 = int(3.5)
print(x2)
print(X2)

print('======get the type=====')

x3=5
y3="shankar"
z3=6.5
print(type(x3),type(y3),type(z3),id(x3),id(y3),id(z3))

print("===many values to multiple varibles===")
x4,y4,z4=10,"shankar",100.5
print(x4)
print(y4)
print(z4)
print("===one value to multiple varibles===")
x5=y5=z5=50
print(x5)
print(y5)
print(z5)