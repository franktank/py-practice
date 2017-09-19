# If alphabet is characters a-z, map to prime number

# Hash approach
if (not a and b) or (a and not b):
    return False
a = 'a bc'
b = 'casdab'

char_counter = {}
for char in a:
    if char.isspace():
        continue
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1

for char in b:
    if char not in char_counter:
        print("Not anagram!")
    if char in char_counter:
        char_counter[char] -= 1
        if char_counter[char] == 0:
            del char_counter[char]

if not char_counter:
    print("Anagram!")
