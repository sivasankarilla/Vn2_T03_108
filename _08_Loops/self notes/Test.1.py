num=1
sum=0
i=1
n=int(input("Enter a list of numbers, 0 to end input :"))
while(n != 0):
    sum=sum+n
    i=i+1
print("sum of the numbers is :",sum)
print("average of number is :",(sum/i))
