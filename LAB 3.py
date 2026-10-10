#LAB 3#

#1#
# x1 = int(input("Enter x-coordinate of centre "))
# y1 = int(input("Enter y-coordinate of centre "))
# r = int(input("Enter Radius "))
# if r <= 0:
#     print("Invalid input: Radius must be greater than 0")
# else:
#     x2 = int(input("Enter x-coordinate of point "))
#     y2 = int(input("Enter y-coordinate of point "))
# distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
# radius_squared = r ** 2
# if distance_squared < radius_squared:
#     print("The point lies inside the circle.")
# elif distance_squared == radius_squared:
#     print("The point lies on the boundary of the circle.")
# else:
#     print("The point lies outside the circle.")

#2#
# # s = float(input("Enter the side of regular pentagon "))
# # tan_pi_5 = (5 - 2 * (5 ** 0.5)) ** 0.5
# # area = (5 * (s ** 2)) / (4 * tan_pi_5)
# # print("The area of the pentagon is {area:.4f}") 

# import math
# s = float(input("Enter the side of the pentagon: "))
# if s <= 0:
#     print("Invalid input: Side must be greater than 0")
# else:
#     # Formula for area of a regular pentagon
#     area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
#     print("Area of the pentagon =", area)
    
#3#
# a = float(input("Enter the first angle: "))
# b = float(input("Enter the second angle: "))
# c = float(input("Enter the third angle: "))
# if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
#     print("The angles cannot form a triangle.")
# else:
#     if a < 90 and b < 90 and c < 90:
#         print("The triangle is acute-angled.")
#     elif a == 90 or b == 90 or c == 90:
#         print("The triangle is right-angled.")
#     else:
#         print("The triangle is obtuse-angled.")
    
#4#
# n = int(input("Enter a 4-digit number: "))
# if n < 1000 or n > 9999:
#     print("Invalid input: Please enter a 4-digit number.")
# else:
#     first_digit = n // 1000
#     second_digit = (n // 100) % 10
#     third_digit = (n // 10) % 10
#     fourth_digit = n % 10
#     first_sum = first_digit + second_digit
#     last_sum = third_digit + fourth_digit
#     print("Sum of first two digits =", first_sum)
#     print("Sum of last two digits =", last_sum)
#     if first_sum == last_sum:
#         print("Both sums are equal.")
#     else:
#         print("Both sums are not equal.")
        

#5#
# n = int(input("Enter a 5-digit number: "))
# if n < 10000 or n > 99999:
#     print("Invalid input: Please enter a 5-digit number.")
# else:
#     d1 = n // 10000
#     d2 = (n // 1000) % 10
#     d3 = (n // 100) % 10
#     d4 = (n // 10) % 10
#     d5 = n % 10
#     # Check from left to right to get the first occurrence
#     if d1 >= d2 and d1 >= d3 and d1 >= d4 and d1 >= d5:
#         largest = d1
#         position = 1
#     elif d2 >= d3 and d2 >= d4 and d2 >= d5:
#         largest = d2
#         position = 2
#     elif d3 >= d4 and d3 >= d5:
#         largest = d3
#         position = 3
#     elif d4 >= d5:
#         largest = d4
#         position = 4
#     else:
#         largest = d5
#         position = 5
#     print("Largest digit =", largest)
#     print("Position from left =", position)
    
    
#6#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# a = a + b + c
# b = a - b - c
# c = a - b
# a = a - b - c
# print("After cyclic rotation:")
# print("a =", a)
# print("b =", b)
# print("c =", c)


#7#
# n = int(input("Enter a 3-digit number: "))
# if n < 100 or n > 999:
#     print("Invalid input: Please enter a 3-digit number.")
# else:
#     hundreds = n // 100
#     tens = (n // 10) % 10
#     units = n % 10
#     digit_sum = hundreds + tens + units
#     if n % digit_sum == 0:
#         print(n, "is a Harshad number.")
#     else:
#         print(n, "is not a Harshad number.")
        
        
# num = int(input("Enter a 3-digit Number "))
# a = num // 100
# b = (num // 10) % 10
# c = num % 10
# sum_digits = a + b + c
# if num % sum_digits == 0:
#     print("Harshad Number")
# else:
#     print("Not a Harshad Number")
    

#8#
# V = float(input("Enter the initial quantity of water (litres): "))
# N = int(input("Enter the number of days: "))
# if V < 0 or N < 0:
#     print("Invalid input")
# else:
#     quantity = 200 + (V - 200) * (0.95 ** N)
#     print("Quantity of water after", N, "days =", quantity, "litres")
    
    
#9#    
# a1 = float(input("Enter a1: "))
# b1 = float(input("Enter b1: "))
# c1 = float(input("Enter c1: "))
# a2 = float(input("Enter a2: "))
# b2 = float(input("Enter b2: "))
# c2 = float(input("Enter c2: "))
# D = a1 * b2 - a2 * b1
# if a1 == 0 and b1 == 0:
#     print("Invalid first line")
# elif a2 == 0 and b2 == 0:
#     print("Invalid second line")
# elif D != 0:
#     x = (c1 * b2 - c2 * b1) / D
#     y = (a1 * c2 - a2 * c1) / D
#     print("Point of intersection:")
#     print("x =", format(x, ".2f"))
#     print("y =", format(y, ".2f"))
# elif a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
#     print("The lines are coincident")
# else:
#     print("The lines are parallel")