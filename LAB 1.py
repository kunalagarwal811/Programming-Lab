#Lab 1#

#1#
# print("Hello JKLU!")
# print("I am learning Python.")

#2#
# name = input("Enter student's name: ")
# branch = input("Enter branch: ")
# print("Welcome", name, "to", branch, "branch!")

#3#
# length = float(input("Enter length (in metres): "))
# width = float(input("Enter width (in metres): "))
# area = length * width
# print("Area of the rectangular plot =", area, "square metres")

#4#
# length = float(input("Enter length (in feet): "))
# width = float(input("Enter width (in feet): "))
# # Convert feet to metres
# length_m = length * 0.3048
# width_m = width * 0.3048
# area = length_m * width_m
# print("Area of the rectangular plot =", area, "square metres")

#5#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# if x <= 0 or y <= 0:
#     print("Invalid Input")
# elif y % x == 0:
#     print("y is divisible by x")
# else:
#     print("y is not divisible by x")

#6#
# num = int(input("Enter an integer: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#7#
# import math
# radius = float(input("Enter the radius of the circle (1-100): "))
# if radius < 1 or radius > 100:
#     print("Invalid Input")
# else:
#     area = math.pi * radius ** 2
#     print("Area of the circle =", area)

#8#
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# kelvin = celsius + 273.15
# print("Temperature in Fahrenheit =", fahrenheit)
# print("Temperature in Kelvin =", kelvin)

#9#
# seconds = int(input("Enter number of seconds (1-86400): "))
# if seconds < 1 or seconds > 86400:
#     print("Invalid Input")
# else:
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     secs = seconds % 60
#     print(f"{hours:02d}:{minutes:02d}:{secs:02d}")

#10#
# total_classes = int(input("Enter total number of classes: "))
# attended_classes = int(input("Enter number of classes attended: "))
# if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
#     print("Invalid Input")
# else:
#     attendance = (attended_classes / total_classes) * 100
#     print("Attendance Percentage =", attendance, "%")
#     if attendance >= 75:
#         print("Eligible")
#     else:
#         print("Not Eligible")