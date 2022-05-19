"""
opps::
    1.python program to check leap year or not
"""

#
# class Year:
#
#     def leap(self):
#         if (year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0):
#             print(year, "is a leap year")
#         else:
#             print(year, "is a not leap year")
#
#
# year = int(input("enter the year:"))
# obj = Year()
# obj.leap()

"""
python program to check armstrong number
     153=1*1*1+5*5*5+3*3*3//153 is an armstrong number
"""

#
# class armstrong:
#
#     def arm(self,t):
#         sum=0
#         while t > 0:
#
#             digital = t % 10
#             sum += (digital ** 3)
#             t //=  10
#         if num == sum:
#             print(num, "is armstrong number")
#         else:
#             print(num, "is not a armstrong number")
#
# num=int(input("enter any number"))
# t=num
# val=armstrong()
# val.arm(t)

"""
3.python program to make a sample calculator
 ex: choice=input("enter choice(1/2/3/4):")
 1.add,2.sub,3.mul,4.div
"""
#
# class calculater:
#     def cal(self,a,b):
#         if c==1:
#             add=a+b
#             print(add)
#         elif c==2:
#             sub=a-b
#             print(sub)
#         elif c==3:
#             mul=a*b
#             print(mul)
#         if c==4:
#             div=a/b
#             print(div)
# a=int(input("enter first value:"))
# b=int(input("enter second value"))
# c=int(input('choice(1/2/3/4)'))
#
# obj=calculater()
# obj.cal(a,b)

"""
4.roman number to integer
    symbol      val
      I          1
      V          5
      x          10
      L          50
      C          100
      D          500
      M          1000
      
      ex1:
      input:num = "III"
      output:3
      
      ex2:
      input:num = "LVIII"
      Output:58
"""
# class Solution:
#    def solve(self, numeral):
#       d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#       ans = 0
#       n = len(numeral)
#       for (idx, c) in enumerate(numeral):
#          if idx < n - 1 and d[c] < d[numeral[idx + 1]]:
#             ans -= d[c]
#          else:
#             ans += d[c]
#       return ans
#
# ob = Solution()
# numeral = "MCLXVI"
# print(ob.solve(numeral))


# num=input("enter roman number")
# d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#
# for i in num:


# class Solution(object):
#    def longestPalindrome(self, s):
#       dp = [[False for i in range(len(s))] for i in range(len(s))]
#       for i in range(len(s)):
#          dp[i][i] = True
#       max_length = 1
#       start = 0
#       for l in range(2,len(s)+1):
#          for i in range(len(s)-l+1):
#             end = i+l
#             if l==2:
#                if s[i] == s[end-1]:
#                   dp[i][end-1]=True
#                   max_length = l
#                   start = i
#             else:
#                if s[i] == s[end-1] and dp[i+1][end-2]:
#                   dp[i][end-1]=True
#                   max_length = l
#                   start = i
#       return s[start:start+max_length]
# ob1 = Solution()
# print(ob1.longestPalindrome("ABBABBC"))