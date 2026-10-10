#Lab 6#

'''1'''

# print("             Addition Table")
# print("      1  2  3  4  5  6  7  8  9")
# print("      -----------------------------")
# for i in range(1, 10):
#     print(i, "|", end=" ")
#     for j in range(1, 10):
#         print(f"{i + j:2}", end=" ")
#     print()


'''2'''

# N = int(input())
# slot = N
# while slot <= 1000:
#     if slot % 4 == 0:
#         slot += N
#         continue
#     print(slot, end=" ")
#     slot += N


'''3'''

##a##

# N = int(input("Enter N: "))
# i = 1
# while i <= N:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

##b##

# N = int(input("Enter N: "))
# i = N
# while i >= 1:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i -= 1

##c##

# N = int(input("Enter N: "))
# i = 1
# while i <= N:
#     # Print spaces
#     space = 1
#     while space <= N - i:
#         print("  ", end="")
#         space += 1
#     j = 1
#     while j <= i:
#         print("* ", end="")
#         j += 1
#     print()
#     i += 1


'''4'''

# num = int(input("Enter a positive integer: "))
# original = num
# octal = ""
# while num > 0:
#     remainder = num % 8
#     octal = str(remainder) + octal
#     num = num // 8
# print("Octal equivalent:", octal)
# print("Using oct():", oct(original)[2:])
# if octal == oct(original)[2:]:
#     print("Result matches")
# else:
#     print("Result does not match")


'''5'''

# N = int(input())
# winning = 0
# runner_up = 0
# i = 1
# while i <= N:
#     distance = int(input())
#     if distance > winning:
#         runner_up = winning
#         winning = distance
#     elif distance > runner_up and distance < winning:
#         runner_up = distance
#     i += 1
# print(winning)
# print(runner_up)


'''6'''

# N = int(input("Enter N: "))
# num = 1
# while num <= N:
#     temp = num
#     digits = 0
#     while temp > 0:
#         digits += 1
#         temp = temp // 10
#     temp = num
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp = temp // 10
#     if total == num:
#         print(num, end=" ")
#     num += 1


'''7'''
# N = 1
# while N <= 15:
#     square = N * N
#     cube = N * N * N
#     square_root = N ** 0.5
#     print(N, "\t", square, "\t", cube, "\t", format(square_root, ".4f"))   
#     N = N + 1


'''8'''

# N = int(input("Enter N: "))
# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(" ", end=" ")
#     for j in range(i):
#         print(i, end=" ")


'''9'''

# N = int(input("Enter N: "))
# num = 1
# for i in range(1, N + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()


'''10'''

# n = 5 
# for i in range(1, n + 1):            
#     print(" " * (n - i) + "* " * i) 
# for i in range(n - 1, 0, -1):             
#     print(" " * (n - i) + "* " * i)