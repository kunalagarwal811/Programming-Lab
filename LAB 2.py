#Lab 2#

#1#
# num = int(input("Enter a number: ")) 
# if num % 5 == 0:
#     print("Hi")
# else:
#     print("Bye")
    
#2#
# x = float(input("Enter the First parallel side: "))
# y = float(input("Enter second parallel side: "))
# h = float(input("Enter height: "))
# area = 0.5 * (x + y) * h
# print("Area of trapezoid =", area)


#3#
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height ** 2)
# print("BMI =", round(bmi, 2))
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Slightly overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("Clinically obese")
    
#4#
# ch = input("Enter an alphabet: ")
# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Consonant")
    
#5#
# initial = 2.19e14
# final = 4.68e14
# growth = ((final - initial) / initial) * 100
# print("Percentage of growth =", round(growth), "%")

#6#
# months = int(input("Enter number of months: "))
# years = months // 12
# remaining_months = months % 12
# print("Years =", years)
# print("Months =", remaining_months)

#7#
# color = input("Enter color (Blue/Red): ")
# mode = input("Enter mode (Steady/Flashing): ")

# if color == "Blue" and mode == "Steady":
#     print("Clear view")
# elif color == "Blue" and mode == "Flashing":
#     print("Clouds due")
# elif color == "Red" and mode == "Steady":
#     print("Rain ahead")
# elif color == "Red" and mode == "Flashing":
#     print("Snow instead")
# else:
#     print("Invalid input")
    
#8#
# cost = float(input("Enter total cost: "))
# revenue = float(input("Enter total revenue: "))
# if cost == revenue:
#     print("Break even")
# elif revenue > cost:
#     print("Profit =", revenue - cost)
# else:
#     print("Loss =", cost - revenue)
    
#9#
# widgets = int(input("Enter number of widgets: "))
# if widgets >= 100:
#     cost = widgets * 0.20
# else:
#     cost = widgets * 0.25
# print("Total cost = $", format(cost, ".2f"))

#10#
# pounds = float(input("Enter number of pounds: "))
# cash = float(input("Enter cash tendered: "))
# cost = pounds * 2.50
# if cash >= cost:
#     change = cash - cost
#     print("Change = $", format(change, ".2f"))
# else:
#     owe = cost - cash
#     print("You owe $", format(owe, ".2f"), "more.")
    
#11#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c
# print("Largest =", largest)

#12#
# basic = float(input("Enter basic salary: "))
# hra = 0.20 * basic
# ta = 0.05 * basic
# da = 0.10 * basic
# gross_salary = basic + hra + ta + da
# print("HRA =", hra)
# print("TA =", ta)
# print("DA =", da)
# print("Gross Salary =", gross_salary)

#13#
# basic = float(input("Enter basic salary: "))
# hra = 0.20 * basic
# ta = 0.05 * basic
# da = 0.10 * basic
# gross_salary = basic + hra + ta + da
# if gross_salary < 300000:
#     tax_rate = 0
# elif gross_salary <= 1000000:
#     tax_rate = 10
# elif gross_salary <= 2500000:
#     tax_rate = 20
# else:
#     tax_rate = 30
# tax = gross_salary * tax_rate / 100
# print("Gross Salary =", gross_salary)
# print("Tax Rate =", tax_rate, "%")
# print("Income Tax =", tax)

#14#
# income = float(input("Enter taxable income: "))
# if income <= 20000:
#     tax = 0.02 * income
# elif income <= 50000:
#     tax = 400 + 0.025 * (income - 20000)
# else:
#     tax = 1150 + 0.035 * (income - 50000)
# print("Tax =", tax)