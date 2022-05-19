"""
class&object
-------------------------------------------------
    class and object are interrelated with each other

    class:
    --->provides the definition of an object
    --->collection of objects
    --->a blueprint to create a class
    --->the 'class' :keyword is used to create a class
    --->python constructor is defined with __init__()method.
    --->python doesn't support multiple constructors in aclass i.e. no constructor overloading.

"""
# class Shankar():
#     d=12
#
#     print("this is class")
#     def display(self):
#         a=10
#         b=12
#         print(a,b)
# obj=Shankar()
# obj.display()
# print(obj.d)
#
#

class Mobile:
    def __int__(self,brand,battery,ram,camera,price): #__init__ function is used to initialization of varibles
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("battery:",self.battery)
        print("ram:",self.ram)
        print("camera:",self.camera)
        print("price:",self.price)


obj=Mobile("apple","battery","ram","camera","price")
obj.display()



