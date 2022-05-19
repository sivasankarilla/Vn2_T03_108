'''
String:
------
1.Group of characters.
2.String represents ",",','.  Ex:'shankar'."shankar".
3.String is immutable.----> values con not  be change.
4.String keyword str.
5.String perform CRUD (Create-Retrive-Update-Delete)operations.
6.String allows duplicate values.
Ex:(name = "shankar",name = "satish",name = "shankar").
7.String store hash mechanism (means its depends upon hashkey  table)
8.String perform indexing and slicing.
'''
#
# a = "Hello"
# print(a)
# print("===Multiline Strings======")
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# print('====Strings are Arrays====')
# a0 = "Hello, World!"
# print(a0[1])
# for x1 in "banana":
#   print(x1)
# # for x2 in "banana": #one line
#     print(x2,end="")
#
# a1 = "shankar"
# print(len(a1)) #string length len()
#
# txt = "The best things in life are free!"
# print("free" in txt) # membership operator
# print("=======Slicing======")
# b = "Hello, World!"
# print(b[2:5])
# print(b[:5]) #start with zero indexing position
# print(b[2:]) #end with final indexing position
# print("====String Concatenation======")
# a2 = "Hello"
# b2 = "World"
# c2 = a2 + b2
# print(c2)
# c2 = a2 + " " + b2
# print(c2)
# print("=====String Format====")
# age = 24
# txt = "My name is shankar, and I am {}"
# print(txt.format(age))
#
# quantity = 3 # 0 indexing position
# itemno = 567 # 1 indexing position
# price = 49.95 #2 indexing position
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
#

# print("===== (1) length of the string=====")
# length_of_the_string="siva shankar"
# x=len(length_of_the_string)
# print(x)

#IN function(1.1) second method

# def length(a):
#     x=len(a)
#     print(x)
# a = input("enter the any string:")
# length(a)


#IN if condition(1.2)third method
# a=input("enter the any string:")
# l=len(a)
# if l == len(a):
#     print(l)

# #In loop(1.3)fourth method
# a=input("enter the any string:")
# count=0
# for i in a:
#     i=len(i)
#     count = count+i
# print(count)






# print("====(2)count the characters in string====")
# char="prabin kumar mahapatre"
# count1=char.count("a")
# print(count1)

# #In function(2.1)
# def char1(a):
#     count2 = a.count("a")
#     print(count2)
# a=input("enter any string:")
# char1(a)


# #In loop(2.3)
# a=input("enter any character:")
# count=""
# for i in a:
#     count=count+str(i)
# print(count)



# print("=====(3)string slicing====")
# slic="siva shankar"
# slicing1=slic[5:14]
# print(slicing1)


# #in function(3.1)
# def slicing_of_string(slicing):
#     slicing1=slicing[0:5]
#     print(slicing1)
# slic=input("enter any string:")
# slicing_of_string(slic)


# #in loop(3.2)
# slicing=input("enter any character:")
# full_string=""
# for i in slicing:
#     full_string=full_string+str(i)
# string=full_string
# slicing1=slicing[0:5]
# print(slicing1)

#IN if condition

if









print("=====(4)Replace first occurance character======")
replace1="no one can better than you"
print("The original string is : " + str(replace1))
n = '@'
res = replace1[1:].replace(replace1[0], n)
print("Replaced String : " + str(res))

#
print("======(5)swapping chars in string=====")

#
# swap characters in string
# def swap(string):
#     return string[-1:] + string[1:-1] + string[:1]
#
#
# # take string from user
# str1 = input("Please Enter String : ")
#
# print(swap(str1))
#
#
# # swap characters in string
# def swap(str):
#     if len(str) <= 1:
#         return str
#
#     mid = str[1:len(str) - 1]
#     return str[len(str) - 1] + mid + str[0]
#
#
# # take string from user
# str1 = input("Please Enter String : ")
#
# print(swap(str1))
# print("======(6)append chars in string=====")
# x="siva"
# y="shankar"
# space=" "
# print(x+space+y)

# print("======(7)substring replacement=====")
#
# input = 'helloABworld'
# pattern = 'AB'
# replaceWith = 'C'
# x=input.replace(pattern, replaceWith)
# print(x)

# print("=====(8)length of longest string=====")
# names=['pradeep','shankar','prabin','chitu','mani']
# print(max(names,key=len))

print("=====(9)nth index character from string====")






# print("====(10)first last chars swapping====")
# def swap(swapp):
#     swapped_string=swapp[-1] + swapp[1:-1] + swapp[0]
#     print(swapped_string)
# swap("shankar")
#
# print("=====(11)remove odd index values=====")
# no_index = ("shankar")
# odd_index =no_index[0::2]
# print(odd_index)

# print("====(12)count words in a string=====")
# string2="my name is siva shankar i am from anaparthi"
# result = len(string2.split())
#
# print("There are " + str(result) + " words.")
#
# print("=====(13)Upper lower case of a string====")
# text="Shankar"
# print(text.upper())
# print(text.lower())


print("========(14)sort unique words alphanumerically=======")


# def sort(lst):
#     lst = [str(i) for i in lst]
#     lst.sort()
#     lst = [int(i) if i.isdigit() else i for i in lst]
#     return lst
#
#
# # Driver code
# lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
#
# print(sort(lst))


print("=========(15)create html from string=======")



print("========(16)insert string in middle of speical chars========")



print("=======(17)4copies of last 2 chars======")



print('========(18)length of first 3 chars=====')





# print("=====(19)last part of string====")
# text1="shankar"
# last_part_of_string =text1[-1]
# print(last_part_of_string)



# print("=====(20)reverse a string if it's length is a multiple of 4======")
# str=input("enter any 4 multiple string:")
# if len(str) % 4 == 0:
#     rev=str[::-1]
#     print(rev)
# else:
#     print("your enter the string is not multiple of 4")




# print("===(21)convert given string to all uppercase====")
# text2=input('Enter any string value:')
# text3=text2.upper()
# print(text3)

print("======(22)program to sort a string lexicographically=====")


# print('====(23)program to remove a newline in python====')
# str1 = "\n KFC is the best chicken  \n"
# newstr = str1.strip()
# print(newstr)
#
# print("====(24)program to check whether a string start with=====")
#
# text4="stop dreaming start doing"
# text4.startswith("stop")



print("=======(25)program to create  a caesar encryption======")


print("======(26)display formatted text(width=50)as output=====")


print("======(27)remove existing indentation from all of the lines in a given text=====")


print("=====(28)to add a prefix text to all of the lines in string=====")



print("======(29)to set the indentation of the first line====")


# print("========(30)to print following floating numbers upto two decimal places===")
# x=25.25645
# y="{:.2f}".format(x)
# print(y)