"""
Q4. Accept the marked price from the user and calculate the Net amount as (Market price- Disscount) to pay according to following criteria:

    Marked price                         Discount
     >10000                                 20%
 >7000 and <=10000                          15%
     <=7000                                 10%
"""
X = float(input("enter the total market price :"))
if X > 10000:
   y = (X/100)*80
   print("your selling price :",y)
if X <= 10000 and X > 7000:
    y = (X/100)*85
    print("your selling price :",y)
if X <= 7000:
    y = (X/100)*90
    print("your selling price :",y)

