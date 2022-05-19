# print("="*5,"(1)table of the given number","="*5)
# def mul_table(multiple,multiplayer):
#     for i in range(1,multiplayer+1):
#         a = i * multiple
#         print(multiple,"*",i,"=",a)
# multiple= int(input("enter the what multiple:"))
# multiplayer= int(input("enter multiplayer upto you want"))
# mul_table(multiple,multiplayer)

# print("="*5,"(2)sum all the numbers in a list, set,tuple","="*5)
#
# def sum(num):
#     count=0
#     for i in num:
#         count=count+i
#     print(count)
# list1=[1,2,3,5,6,4]
# set1={1,6,5,9,5,3}
# tuple1=(1,5,6,9,10)
#
# sum(list1)
# sum(set1)
# sum(tuple1)


# print("="*5,"(3)multiply all the numbers in list,set,tuple","="*5)
# def multiply(num1):
#     count=1
#     for i in num1:
#         count=count*i
#     print(count)
# list2=[1,2,3,5,6,4]
# set2={1,6,5,9,5,3}
# tuple2=(1,5,6,9,10)
#
# multiply(list2)
# multiply(set2)
# multiply(tuple2)



# print("="*5,"(4)accepts a string and calculate the number of upper-case letters and lower case letters","="*5)
# def string_test(str):
#     upper=0
#     lower=0
#     for c in str:
#         if c.isupper():
#            upper+=1
#         elif c.islower():
#            lower+=1
#         else:
#            pass
#     print ("Original String : ", str)
#     print ("No. of Upper case characters : ", upper)
#     print ("No. of Lower case Characters : ", lower)
#
# string_test('You Are Strong Than You Think')


# print("="*5,"(5)write a function to take number as input and print its square value","="*5)
# def square_of_number(num):
#     square=num*num
#     return square
#
# num=int(input("enter a value:"))
# result=square_of_number(num)
# print("square of given number is",result)




# print("="*5,"(6)write a function to accept 2 number as input and return sum.","="*5)
# def sum_of_values(a,b):
#     sum=a+b
#     return sum
# a=int(input("enter first value:"))
# b=int(input("enter second value:"))
# print(sum_of_values(a,b))




# print("="*5,"(7)write a function to check whether the given number is even are odd","="*5)
# def even_or_odd(num1):
#     if num1 % 2 == 0:
#         print(num1,"is even number")
#     else:
#         print(num1,"is odd number")
#
# num=int(input("enter a value"))
# even_or_odd(num)


# print("="*5,"(8)write a function to find factorial of given number","="*5)
# def factorial(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#     return num
# val=int(input("enter only positive values"))
# f = factorial(val)
# print(f)

"""
(9)returning multiple values from a function:
return sum,sub
   output
   the sum is :150
   the subtraction is : 50
   
   type of arguments
        1.positional arguments
        2.keyword arguments
        3.default arguments
        4.variable length arguments
"""

# def sum_and_sub(a,b=50):
#     sum=a+b
#     sub=a-b
#     return 'the sum is:{}\nthe subtraction is:{}'.format(sum,sub)
#
# print(sum_and_sub(100,50))         #1.positional arguments
# print(sum_and_sub(a=100,b=50))     #2.keyword arguments
# print(sum_and_sub(100))            #3.default arguments
#
# def sum_sub(*num):
#     sum=num[0]+num[1]              #4.Variables Length Parameters (or) arguments
#     sub=num[0]-num[1]
#     return 'the sum is:{}\nthe subtraction is:{}'.format(sum,sub)
# print(sum_sub(100,50))

print("="*5,"(10)take a list and return a new list with unique elements of the first","="*5)
def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1,2,4,5,4,5,6,9,10]))



print("="*5,"(11) print given pascal's triangle","="*5)
# from math import factorial
#
#
# n = 5
# for i in range(n):
# 	for j in range(n-i+1):
#
# 		# for left spacing
# 		print(end=" ")
#
# 	for j in range(i+1):
#
# 		# nCr = n!/((n-r)!*r!)
# 		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#
# 	# for new line
# 	print()


# print("="*5,"(12) function to check whether a string is a palindrome or not ","="*5)
# def palindrome_or_not(str):
#     pal=str[::-1]
#     if str == pal:
#         print(str,"is a palindrome")
#     else:
#         print(str,"is not a palindrome")
#
# str=input("enter any string:")
# palindrome_or_not(str)


# print("="*5,"(13)check whether a number is in a given range","="*5)
#
# def range1(num):
#     if num in range(1,201):
#         print(num,"is in a given range")
#     else:
#         print(num,"is out of range")
#
# num=int(input("enter a number:"))
# range1(num)
