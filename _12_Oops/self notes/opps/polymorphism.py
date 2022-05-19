"""
polymorphism
-------------------------------------------------
--->polymorphism was derived from geek words poly means "many"
and morphic means "forms",which means multiple forms or more than one form
--->An operation exhibits different behaviors in different instances

ex:-
operator overloading
method overloading

types of polymorphism:
1.compile-time
a)method over-loading
-------------------------
    ---> In same class same method(function) names and different parameters
2.Run-time
b)Method over-riding
-------------------------
    --->different class same function or method names and different parameters
"""
# #method overloading
# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=1):
#         return a+b+c
#
# obj=A()
# print(obj.sum(1,2))


#method over-riding
class A:
    def display(self):
        print("this is class A")
class B(A):
    print("this is class B")
    super().display()
obj=B()
obj.display()