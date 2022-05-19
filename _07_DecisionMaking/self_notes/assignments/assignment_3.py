"""
Q3. A company decided to give bonus to employee according to following criteria:

     Time period of service             Bonus

     more than 10 years                  10%

     >=6 and <=10                        8%

     Less than 6 years                   5%

     Ask user for their salary and years of service and print the net bonus amount
"""
salary = float(input("enter the salary of employee:"))
year = float(input("enter the how many year of service:"))
if year > 10:
    net = (salary/100)*10
    print("total net salary:",salary+net)
if (year >= 6 and year <= 10):
    net = (salary/100)*8
    print("total net salary:",salary+net)
 if (year<6):
        net = (salary / 100)*5
        print("total net salary:",salary+net)

