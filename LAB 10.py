#1#

'''nums = tuple(map(int, input().split()))
v = int(input())
print("Tuple:", nums)
print("Length:", len(nums))
print("Count of", v, ":", nums.count(v))
print("First index of", v, ":", nums.index(v))'''

#2#

'''def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count
s = input()
print("Vowels:", count_vowels(s))'''

#3#

'''votes = input().split()
counts = {}
winner = votes[0]
for name in votes:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
    if counts[name] > counts[winner]:
        winner = name
for name in counts:
    print(name + ":", counts[name])
print("Winner:", winner)'''

#4#

'''word = input()
counts = {}
for ch in word:
    if ch not in counts:
        counts[ch] = 1
    else:
        counts[ch] += 1
print(counts)'''

#5#

'''def simple_interest(p, r, t=1):
    return p * r * t / 100
p = float(input())
r = float(input())
print("1 year:", simple_interest(p, r))
print("3 years:", simple_interest(p, r, 3))'''

#6#

'''def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
n = int(input())
grades = {}
for i in range(n):
    data = input().split()
    name = data[0]
    marks = int(data[1])
    grade = get_grade(marks)
    print(name + ":", grade)
    if grade not in grades:
        grades[grade] = 1
    else:
        grades[grade] += 1
print("Grade count:")
print(grades)'''

#7#

'''nums = tuple(map(int, input().split()))
even = ()
for num in nums:
    if num % 2 == 0:
        even += (num,)
print(even)'''

#8#

'''n = int(input())
capitals = {}
for i in range(n):
    data = input().split()
    capitals[data[0]] = data[1]
country = input()
if country in capitals:
    print(capitals[country])
else:
    print("Not found")'''

#9#

'''n = int(input())
stock = {}
for i in range(n):
    data = input().split()
    stock[data[0]] = int(data[1])
q = int(input())
for i in range(q):
    data = input().split()
    action = data[0]
    item = data[1]
    qty = int(data[2])
    if action == "SELL":
        if stock[item] >= qty:
            stock[item] -= qty
        else:
            print("Insufficient stock:", item)
    elif action == "ADD":
        if item in stock:
            stock[item] += qty
        else:
            stock[item] = qty
for item in stock:
    print(item, stock[item])'''

#10#

'''def stats(nums):
    small = nums[0]
    large = nums[0]
    total = 0
    for num in nums:
        if num < small:
            small = num
        if num > large:
            large = num
        total += num
    avg = total / len(nums)
    return (small, large, avg)
nums = list(map(int, input().split()))
print(stats(nums))'''