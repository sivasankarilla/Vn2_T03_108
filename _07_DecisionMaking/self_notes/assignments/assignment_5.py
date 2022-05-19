"""
Q5.Accept the number of days from the user and calculate the charge for library according to following :

  Till five days : Rs 2/day
  six to ten days: Rs 3/day
  11 to 15 days  : Rs 4/day
  After 15 days  : Rs 5/day
"""
a = int(input("enter the how many days completed to barrow the book from library : "))
if a > 15:
    b=a*5
    print("your charge is:",b)
if a <= 15 and a >=11:
    b=a*4
    print("your charge is:",b)
if a <= 10 and a >= 6:
    b=a*3
    print("your charge is:",b)
if a <= 5:
     b=a*2
     print("your charge is:",b)

