#1#

'''s = input("Enter string ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)'''

#2#

'''s = input("Enter sentence ")
i = len(s) - 1
count = 0
while i >= 0 and s[i] == " ":
    i = i - 1
while i >= 0 and s[i] != " ":
    count = count + 1
    i = i - 1
print(count)'''

#3(a)#

'''s = input("Enter sentence ")
word = input("Enter word ")
count = s.count(word)
if word in s:
    print("Word found")
    print("Occurrences:", count)
else:
    print("Word not found")
    print("Occurrences: 0")'''

#3(b)#

'''s = input("Enter a sentence: ")
word = input("Enter a word: ")
count = 0
i = 0
while i <= len(s) - len(word):
    j = 0
    while j < len(word) and s[i + j] == word[j]:
        j = j + 1
    if j == len(word):
        count = count + 1
        i = i + len(word)
    else:
        i = i + 1
if count > 0:
    print("Word found")
else:
    print("Word not found")
print("Occurrences:", count)'''

#4#

'''s = input("Enter sentence ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
for ch in alphabet:
    if ch in s.lower():
        count = count + 1
if count == 26:
    print("Pangram")
else:
    print("Not a pangram")'''

#5#

'''s = input("Enter a string: ")
e= int(input("shift:"))
total=" "
a="abcdefghijklmnopqrstuvwxyz"
for i in s:
    z = a.index(i)
    total= total+ a[(z+e)%26]
print(total)'''

#6#

'''count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
total = 0
while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    if num >= 1 and num <= 2:
        count1 += 1
    elif num >= 3 and num <= 4:
        count2 += 1
    elif num >= 5 and num <= 6:
        count3 += 1
    elif num >= 7 and num <= 8:
        count4 += 1
    elif num >= 9 and num <= 10:
        count5 += 1
    else:
        print("Enter number between 1 and 10")
        continue
    total += 1
if total > 0:
    p1 = count1 * 100 / total
    p2 = count2 * 100 / total
    p3 = count3 * 100 / total
    p4 = count4 * 100 / total
    p5 = count5 * 100 / total
    print("1 - 2:", "#" * count1, format(p1, ".2f"), "%")
    print("3 - 4:", "#" * count2, format(p2, ".2f"), "%")
    print("5 - 6:", "#" * count3, format(p3, ".2f"), "%")
    print("7 - 8:", "#" * count4, format(p4, ".2f"), "%")
    print("9 - 10:", "#" * count5, format(p5, ".2f"), "%")
else:
    print("No numbers entered")'''

#7#

'''s = input("Enter a string: ")
i = 0
j = len(s) - 1
flag = True
while i < j:
    if s[i] != s[j]:
        flag = False
    i = i + 1
    j = j - 1
if flag:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#8(i)#

'''numbers = input("Enter integers separated by spaces: ").split()
total = 0
for i in range(len(numbers)):
    total = total + int(numbers[i])
print("Sum:", total)'''

#8(ii)#

'''numbers = input("Enter integers separated by spaces: ").split()
product = 1
for i in range(len(numbers)):
    product = product * int(numbers[i])
print("Product:", product)'''

#8(iii)#

'''numbers = input("Enter integers separated by spaces: ").split()
smallest = int(numbers[0])
for i in range(1, len(numbers)):
    n = int(numbers[i])
    if n < smallest:
        smallest = n
print("Smallest element:", smallest)'''

#9#

'''numbers = input("Enter integers separated by spaces: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Descending order:", numbers)'''

#10#

'''s = input("Enter hyphen-separated words: ")
words = s.split("-")
for i in range(len(words)):
    for j in range(0, len(words) - i - 1):
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp
result = ""
for i in range(len(words)):
    if i > 0:
        result = result + "-"
    result = result + words[i]
print(result)'''

#11#

'''s = input("Enter paragraph ")
digits = 0
alphabets = 0
upper = 0
lower = 0
special = 0
for ch in s:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        alphabets = alphabets + 1
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    else:
        if ch != " ":
            special = special + 1
print("Digits:", digits)
print("Alphabets:", alphabets)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Special characters:", special)'''

#12#

'''s = input("Enter sentence ")
result = ""
for ch in s:
    found = False
    for x in result:
        if x == ch:
            found = True
    if not found:
        result = result + ch
print(result)'''