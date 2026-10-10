#Lab 4#

#1#
# salary = float(input("Enter salary: "))
# years = int(input("Enter year service: "))
# if years > 5:
#     bonus = salary * 5 / 100
#     print("Bonus amount:", bonus)
# else:
#     print("No bonus")
    
#2#
# password = input("Enter password: ")
# if password == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# else:
#     print("Wrong password!")
    
#3# 
# shape = input("Enter shape: ")
# if shape == "square":
#     side = float(input("Enter side: "))
#     area = side * side
#     print(f"The area of square is {area:.2f}")
# elif shape == "rectangle":
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     area = length * width
#     print(f"The area of rectangle is {area:.2f}")
# elif shape == "circle":
#     radius = float(input("Enter radius: "))
#     area = 3.14159 * radius * radius
#     print(f"The area of circle is {area:.2f}")
# elif shape == "triangle":
#     base = float(input("Enter base: "))
#     height = float(input("Enter height: "))
#     area = base * height / 2
#     print(f"The area of triangle is {area:.2f}")
# else:
#     print("Invalid shape")
    
    
#4#
# hours = int(input("Enter hours "))
# minutes = int(input("Enter minutes "))
# minutes = minutes + 15
# if minutes >= 60:
#     minutes = minutes - 60
#     hours = hours + 1 
# if hours == 24:
#     hours = 0    
# if minutes < 10:
#     print(hours, ":0", minutes)
# else:
#     print(hours, ":", minutes)
     

#5#
# n = float(input("Enter distance in kilometers: "))
# period = input("Enter period of day (day or night): ")
# if period == "day":
#     taxi_price = 33.58 + (n * 37.89)
# else:
#     taxi_price = 33.58 + (n * 43.17)
# cheapest_price = taxi_price
# vehicle = "Taxi"
# if n >= 20:
#     bus_price = n * 4.32
#     if bus_price < cheapest_price:
#         cheapest_price = bus_price
#         vehicle = "Bus"
# if n >= 100:
#     train_price = n * 2.88
#     if train_price < cheapest_price:
#         cheapest_price = train_price
#         vehicle = "Train"
# print(f"Cheapest transport: {vehicle}")
# print(f"Price: {cheapest_price:.2f} INR")
    

#6#
# holidays = int(input("Enter number of holidays: "))
# workdays = 365 - holidays
# total_play_minutes = (workdays * 63) + (holidays * 127)
# norm = 30000
# if total_play_minutes <= norm:
#     diff = norm - total_play_minutes
#     hours = diff // 60
#     minutes = diff % 60 
#     print("Tom sleeps well")
#     print(f"{hours} hours and {minutes} minutes less for play")
# else:
#     diff = total_play_minutes - norm
#     hours = diff // 60
#     minutes = diff % 60
#     print("Tom will run away")
#     print(f"{hours} hours and {minutes} minutes more for play")

#7#
# budget = float(input("Enter budget in BGN: "))
# season = input("Enter season (summer or winter): ")
# destination = ""
# accommodation = ""
# spent_amount = 0.0
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer" or season == "Summer":
#         accommodation = "Camp"
#         spent_amount = budget * 0.30
#     else:
#         accommodation = "Hotel"
#         spent_amount = budget * 0.70

# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer" or season == "Summer":
#         accommodation = "Camp"
#         spent_amount = budget * 0.40
#     else:
#         accommodation = "Hotel"
#         spent_amount = budget * 0.80
# else:
#     destination = "Europe"
#     accommodation = "Hotel"
#     spent_amount = budget * 0.90
# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {spent_amount:.2f}")


#8#
# for number in range(1, 1001):
#     if number % 10 == 6:
#         print(number)


#9#
# n = int(input("Enter n "))
# total = 0 
# for i in range(n):
#     num = int(input("Enter Number "))
#     total_sum = total + num
#     print("Sum =", total)


#10#
# n = int(input("Enter n "))
# for i in range(1, 21):
#     print(n, "x", i, "=", n * i)