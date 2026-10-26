#1#

'''s = input()
vowels = "aeiouAEIOU"
v = 0
c = 0
d = 0
sp = 0
other = 0
for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1
    else:
        other += 1
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)
print("Others:", other)'''

#2#

'''s = input()
ans = ""
for i in range(len(s)):
    if i % 2 == 0:
        ans += s[i].upper()
    else:
        ans += s[i].lower()
print(ans)'''

#3#

'''password = input()
upper = 0
lower = 0
digit = 0
special = 0
for ch in password:
    if ch.isupper():
        upper = 1
    elif ch.islower():
        lower = 1
    elif ch.isdigit():
        digit = 1
    elif ch != " ":
        special = 1
kinds = upper + lower + digit + special
if len(password) < 8 or kinds == 1:
    print("WEAK")
elif kinds == 4:
    print("STRONG")
else:
    print("MODERATE")'''
    
#4#

'''s = input()
target = input()
count = 0
positions = ""
i = 0
for ch in s:
    if ch == target:
        count += 1
        if positions != "":
            positions += " "
        positions += str(i)
    i += 1
print("Count:", count)
if count == 0:
    print("Positions: -1")
else:
    print("Positions:", positions)'''
    
#5#

'''s = input()
wordlen = 0
output = ""
i = 0
while i < len(s):
    if s[i] != " ":
        wordlen += 1
    else:
        if wordlen > 0:
            if output != "":
                output += " "
            output += str(wordlen)
            wordlen = 0
    i += 1
if wordlen > 0:
    if output != "":
        output += " "
    output += str(wordlen)
print(output)'''

#6#

'''plate = input()
valid = True
if len(plate) != 10 or plate[:2] != "RJ":
    valid = False
else:
    for i in range(10):
        ch = plate[i]
        if i == 0 or i == 1 or i == 4 or i == 5:
            if not ch.isupper() or not ch.isalpha():
                valid = False
        else:
            if not ch.isdigit():
                valid = False
print(valid)'''

#7#

'''s = input()
changes = 0
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        changes += 1
    left += 1
    right -= 1
print("Changes needed:", changes)'''

#8#

'''s = input()
seen = ""
ans = ""
for ch in s:
    if ch not in seen:
        seen += ch
        ans += ch
print(ans)'''

#9#

'''message = input()
k = int(input())
ans = ""
for ch in message:
    if ch == " ":
        ans += " "
    else:
        ans += chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
print(ans)'''

#10#

'''s = input()
if len(s) == 0:
    print("- 0")
else:
    bestchar = s[0]
    bestcount = 1
    currentchar = s[0]
    currentcount = 1
    for i in range(1, len(s)):
        if s[i] == currentchar:
            currentcount += 1
        else:
            if currentcount > bestcount:
                bestcount = currentcount
                bestchar = currentchar
            currentchar = s[i]
            currentcount = 1
    if currentcount > bestcount:
        bestcount = currentcount
        bestchar = currentchar
    print(bestchar, bestcount)'''