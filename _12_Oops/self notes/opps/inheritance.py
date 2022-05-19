"""
--->creating a new class from already existing class
--->object of one class acquires the properties of object of another class

IN this 4types of inheritance
1.single inheritance
2.multilevel inheritance
3.Hierarchical inheritance
4.multiple inheritance
"""

# #single inheritance
# class parent:
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def fun2(self):
#         print("this is child class")
# obj=child()
# obj.fun2()
# obj.fun1()

#multilevel inheritance
#
# class parent:
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def fun2(self):
#         print("this is child class")
# class grandchild(child):
#     def fun3(self):
#         print("this is grandchild class")
# obj=grandchild()
# obj.fun3()
# obj.fun2()
# obj.fun1()
#
# #Hierarchical inheritance
# class parent:
#     def fun1(self):
#         print("this is parent class")
# class child1(parent):
#     def fun2(self):
#         print("this is child1 class")
# class child2(parent):
#     def fun3(self):
#         print("this is child2 class")
# obj=child2()
# obj.fun1()
# obj.fun3()
# obj1=child1()
# obj1.fun2()
# obj1.fun1()

# #multiple inheritance
# class father:
#     def fun1(self):
#         print("this is father class")
# class mother:
#     def fun2(self):
#         print("this is mother class")
# class child(father,mother):
#     def fun3(self):
#         print("this is child class")
# obj=child()
# obj.fun1()
# obj.fun2()
# obj.fun3()


#super key word
#
# class A:
#     def __inti__(self):
#         print("this is class a")
#     def fun1(self):
#         print("this is parent class")
# class B(A):
#     def __init__(self):
#         print("this is class b")
#         super().__init__()  #we can access the parent class in child class
#     def fun2(self):
#         print("this is child class")
# obj=B()
#


class Animal():
    def __init__(self):
        print("animal created")
    def who_am_i(self):
        print("i am an animal")
    def eat(self):
        print("i am eating")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def bark(self):
        print("")
mydog = Dog()
mydog.eat()
mydog.
mydog.who_am_i()
mydog.bark()