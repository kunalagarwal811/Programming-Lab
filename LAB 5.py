#Lab 5#

#1#

# X=int(input())
# Y=int(input())
# N=int(input())
# count=0
# for i in range (X,Y):
#     if i%N!=0:
#         print(i,end=' ')
#         count+=1
# print("\n",count)


#2#

#1st Method#

# n = int(input("Enter positive integer "))
# mul = 1
# while n>0:
#     digit = n%10
#     mul = mul*digit
#     n=n//10
# print(mul)

#2nd Method#

# a=int(input())
# b=0
# c=None
# while a>0:
#     b=a%10
#     if c is None:
#         c=b
#     else:
#         c=c*b
#     a=a//10
# print(c)

#3#

# n=int(input())
# large=0
# small=0
# bill=int(input())
# while bill != -999:
#     if bill>n:
#         large+=1
#     else:
#         small+=1
#     bill=int(input())
# print(large)
# print(small)


#4#

# n=int(input("Enter n "))
# p=int(input("Enter p "))
# if n<=0 and p<=0:
#     print("Invalid input")
# else:
#     result = 1
# while p>0:
#     result*=n
#     p-=1
# print(result)


#5#

# a=int(input())
# b=int(input())
# d=0
# while a>0:
#     c=a%10
#     d=d*10+c
#     a=a//10
# if d==b:
#     print("Numbers are reverse of each other")
# else:
#     print("Numbers are not reverse")


#6#

# n=int(input("Enter number: "))
# power=1
# for i in range(n):
#     if i == n-1:
#         print(power)
#     else:
#         print(power, end=" ")
#     power*=2


#7#

# n=int(input())
# c=0
# for i in range(1,int((n/2)+1)):
#     if n%i==0:
#         c=c+i
#     else:
#         continue
# if c==n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")


#8#

# n=int(input())
# for i in range(1,n+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


#9#

# a=int(input("enter your number:"))
# D=int(input("enter a digit:"))
# if 0<=D<=9:
#     pass
# else:
#     print("invalid digit")
#     D=int(input("enter a digit:"))
# count=0
# while a>0:
#     b=a%10
#     a=a//10
#     if b==D:
#         count+=1
#     else:
#         continue
# print("Number of times digit is repeated:",count)


#10#

# a=int(input())
# b=0
# count=0
# for i in range(1,a):
#     if a%i==0:
#         print(i)
#         count+=1
# if count==1:
#     print("It's a Prime Number")
# else:
#     print("It's not a Prime Number")



'''Extra Questions'''


#Lab 5(5)#

#1#

# x = int(input("Enter x "))
# y = int(input("Enter y "))
# n = int(input("Enter n "))
# print(f"Numbers between {x} and {y}")
# for  k in range (x+1 , y+1):
#     if k %n==0:
#         print(k)
        
#2#

# num = input("Enter positive number ")
# digit_sum = 0
# for digit in num:
#     digit_sum += int(digit)
# print(f"Sum of digits: {digit_sum} ")


#3#

# N = int(input("Enter positive integer N "))
# divisible = 0
# not_divisible = 0
# num = int(input("Enter a number "))
# while num != -999:
#     if num % N == 0:
#         divisible += 1
#     else:
#         not_divisible += 1
#     num = int(input("Enter a number "))
# print(f"Count of numbers divisible by {N}: {divisible}")
# print(f"Count of numbers not divisible by {N}: {not_divisible}")


#4#

# n = int(input("Enter a positive integer: "))
# if n < 0:
#     print("Invalid input")
# else:
#     factorial = 1
#     i = 1
#     while i <= n:
#         factorial = factorial * i
#         i = i + 1
# print("Factorial =", factorial)


#5#

# N = int(input("Enter a positive integer: "))
# ori = N
# rev = 0
# while N > 0:
#     digit = N % 10
#     rev = rev * 10 + digit
#     N = N // 10
# if ori == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#6#

# N = int(input("Enter N: "))
# a = 1
# b = 1
# i = 1
# while i <= N:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i = i + 1
    

#7#

# n = int(input("Enter an integer "))
# if n <= 1:
#     print("Invalid input")
# else:
#     i = 2
#     prime = True

#     while i * i <= n:
#         if n % i == 0:
#             prime = False
#         i = i + 1
#     if prime:
#         print("Prime")
#     else:
#         print("Not Prime")


#8#

# sentence = input("Enter a sentence: ")
# capital = 0
# small = 0
# digits = 0
# special = 0
# i = 0
# while i < len(sentence):
#     ch = sentence[i]
#     if ch >= 'A' and ch <= 'Z':
#         capital = capital + 1
#     elif ch >= 'a' and ch <= 'z':
#         small = small + 1
#     elif ch >= '0' and ch <= '9':
#         digits = digits + 1
#     else:
#         special = special + 1
#     i = i + 1
# print("Capital letters =", capital)
# print("Small letters =", small)
# print("Digits =", digits)
# print("Special characters =", special)