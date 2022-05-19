"""
Q2. Accept the percentage from the user and display the grade according to the following criteria

   * Below 25 -->D
   *25 to 45 -->C
   *45 to 50 -->B
   *50 to 60 -->B+
   *60 to 80 -->A
   *Above 80 -->A+
"""
x = float(input("Enter the student percentage :"))
if x > 80:
    print("student grade is : A+")
elif 80<x and x>60:
    print("student grade is : A")
elif 60<x and x>50:
    print("student grade is : B+")
elif 50<x and x>45:
    print("student grade is : B")
elif 45<x and x>25:
    print("student grade is : C")
else:
     print("student grade is : D")


