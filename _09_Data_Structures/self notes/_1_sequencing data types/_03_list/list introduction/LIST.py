"""
-->list are used to store multiple items in a single variable.

1.List is sequence datatype ------> To maintain certain order.
2.list mutable ------> values should be change
3.List is homogenous and Heterogenous data type.
Homogenous means ----> By using single data type Ex[integers,strings,float].
Heterogenous ----> By using Multiple datatype.
EX:[employee details: employee_id= 108,employee_name = "shankar",employee_height = 5.4].
4.List allows the duplicate values.
Ex:(name = "shankar",name = "satish",name = "shankar")
5.list represents [] -----> square brakets.
6.List store heap mechanisim.

"""

list_1=[]
print(type(list_1))


print("==========Homegeneous==========")
list1 = [1, 5, 6, 3, 4, 8, 6, 1]
print('Integers is list : ', list1)

list1 = [1.5, 3.2, 5.6, 4.8]
print('Float is list   : ', list1)

list1 = [True, False, True, False]
print('Boolean is list : ', list1)

list1 = ['hello', ' world', 'welcome', 'python']
print('Strings is list : ', list1)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lists   is list : ', list1)

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Tuples  is list : ', list1)

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Madhu'}]
print('Dict    is list : ', list1)

list1 = [{1, 2, 3}, {4, 5, 6}]
print('Set is list : ', list1)
print("===========Heterogenous===========")
list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
print("---Hetero-------", list1)

# 2.print(List allows duplicate elements
list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

# 3. Insertion order maintains
list1 = [1, 2, 3, 4, 5, 6]
print("Insertion order: ", list1)

print("===Multiline Strings======")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('====Strings are Arrays====')
a = "Hello, World!"
print(a[1])
