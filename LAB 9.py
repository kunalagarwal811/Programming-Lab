#1#

'''nums = list(map(int, input().split()))
even = []
odd = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)'''

#2#

'''words = input().split()
long_words = []
for word in words:
  if len(word) > 3:
    long_words.append(word)
print(long_words)'''

#3#

'''balls = input().split()
total = 0
wickets = 0
boundaries = 0
overruns = 0
runs = []
ballcount = 0
for ball in balls:
    ballcount += 1
    if ball == "W":
        wickets += 1
    else:
        value = int(ball)
        total += value
        overruns += value
        if value == 4 or value == 6:
            boundaries += 1
    if ballcount % 6 == 0:
        runs.append(overruns)
        overruns = 0
if ballcount % 6 != 0:
    runs.append(overruns)
print("Total Runs:", total)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", runs)'''

#4#

'''nums = list(map(int, input().split()))
largest = nums[0]
smallest = nums[0]
for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)'''

#5#

'''words = input().split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)'''

#6#

'''menu = input().split()
prices = list(map(int, input().split()))
ordered = input().split()
total = 0
for i in range(len(menu)):
    qty = ordered.count(menu[i])
    if qty > 0:
        cost = qty * prices[i]
        print(menu[i], "x", qty, "=", cost)
        total += cost
print("Total:", total)'''

#7#

'''words = input().split()
ans = ""
for word in words:
    ans += word[::-1] + " "
print(ans.strip())'''

#8#

'''s = input()
digits = []
total = 0
for ch in s:
    if ch.isdigit():
        digits.append(int(ch))
        total += int(ch)
print(digits)
print("Sum:", total)'''

#9#

'''n = int(input())
used = {}
i = 0
while i < n:
    names = input().lower().split()
    first = names[0]
    last = names[1]
    key = first + "." + last
    if key in used:
        used[key] += 1
        email = key + str(used[key]) + "@jklu.edu.in"
    else:
        used[key] = 1
        email = key + "@jklu.edu.in"
    print(email)
    i += 1'''

#10#

'''nums = list(map(int, input().split()))
ans = []
zeros = 0
for num in nums:
    if num == 0:
        zeros += 1
    else:
        ans.append(num)
for i in range(zeros):
    ans.append(0)
print(ans)'''