""" 1.Accept the following from the user and calculate the percentage of class attended:

    a.  Total number of working days

    b.  Total number of days for absent

    After calculating percentage show that, if the percentage is less than 75, the student will not be able to sit exam.
"""
a = int(input('enter total number of working days :'))
b = int(input("enter total number of days absent :"))
c = a-b
print("total number of days present:",c)
d = (c/a)*100
if d >= 75:
    print("student will allow to exam")
else:
    print("student will not allow to exam")







