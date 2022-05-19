"""
Q1. write a program to print first 10 even numbers in reverse order.
"""
#for i in range(20,0,-2):
 #   print(i,end = ' ')

"""
Q2.write a program to print table of number accepted from user.
"""
#num=int(input("Enter the any number : "))
#n=int(input("enter any number multiplayer upto you want : "))
#for count in range(1,n+1):
 #   print(num ,"*" ,count ,"=" ,num*count)

"""
 Q3. write a program to display product of the digits of number accepted from the user
"""
#num = int(input("enter a number:"))
#product = 1
#while num != 0:
 #   rem = num % 10
  #  product = product * rem
   # num = num//10
#print(product)



"""
Q4. write a program to find the factorial of a number.
"""
#print("enter only positive number")
#num = int(input("enter the what factorial number you want: "))
#factorial=1
#if num < 0:
 #   print("you entered negitive,please enter positive number only")
#elif num == 0:
    #print("you entered zero, please enter positive number only")
#else:
   # for n in range(1,num+1):
#        factorial= factorial*n
#    print("the factorial of",num,"is",factorial)
"""
Q5. write a program to check whether a number is prime or not
"""
#num = int(input("enter a number: "))
#if num > 1:
#   for i in range(2,num):
#       if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#   else:
#       print(num,"is a prime number")

"""
Q6. write a program to display sum of odd numbers and even number that fall between 12 and 37
(including both numbers)
"""
#x = 0
#y = 0
#for i in range(12, 38):
 #   if (i % 2) == 0:
  #     x = x+i
  #  else:
#         y=y+i
#print("sum of odd numbers:",x)
#print("sum of odd numbers:",y)

"""
Q7. write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500
"""
#for i in range(100,501):
#    if (i % 11 == 0) and (i % 2 != 0):
#        print(i)

"""
Q8. write a program to print number from 1 to 20 except multiple of 2 & 3
"""
#for i in range(1,21):
   # if (i % 2 != 0) and (i % 3 != 0):
#        print(i)

"""
Q9. write a program that keep on accepting number from the user until user enter zero. 
display the sum and average of all the numbers  
"""
# sum=0.0
# i=0
# n=float(input("Enter a list of numbers, 0 to end input :"))
# while(n != 0):
#     sum=sum+n
#     i=i+1
# print("sum of the numbers is :",sum)
# print("average of number is :",(sum/i))
#
#
#

"""
Q10.write program to print the following pattern

1
1 2
1 2 3
1 2 3 4
"""
#for i in range(4):
 #   for j in range(i+1):
  #      print(j+1, end=" ")
   # print()

"""
Q11. 
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
#for i in range(5,0,-1):
 #   for j in range(1,i+1):
  #      print(i,end=" ")
   # print()

"""
* * * * *
* * * *
* * *
* *
*
"""
#for i in range(5,0,-1):
 #   for j in range(1,i+1):
  #      print("*", end=" ")
  #  print()
"""
A
B C
D E F
G H I J
K L M N O
"""
#n=5
#num=65
#for i in range(0,n):
#    for j in range(0,i+1):
#        ch=chr(num)
#        print(ch,end=" ")
#       num=num+1

#    print(" ")
