from itertools import permutations
import time

word1 = "alaska"
word2 = "kansas"
word3 = "nevada"
answr = "states"

words = [word1, word2, word3, answr]
unique_chars = set(''.join(words))

if len(unique_chars) > 10:
    raise ValueError("Too many unique characters for a valid solution")

char_list = list(unique_chars)
angka = list(range(10))
char_to_num = {}

def is_valid_solution():
    num1 = int(''.join(str(char_to_num[char]) for char in word1))
    num2 = int(''.join(str(char_to_num[char]) for char in word2))
    num3 = int(''.join(str(char_to_num[char]) for char in word3))
    num4 = int(''.join(str(char_to_num[char]) for char in answr))
    return num1 + num2 + num3 == num4

def get_char_frequency():
    frequency = {}
    for word in words:
        for char in word:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

char_frequency = get_char_frequency()
sorted_chars = sorted(char_list, key=lambda x: -char_frequency[x])

def solve(index=0):
    if index == len(sorted_chars):
        if is_valid_solution():
            print(f"Solution found: {char_to_num}")
            num4 = int(''.join(str(char_to_num[char]) for char in answr))
            print(f"Answer is : {num4}")
            return True
        return False

    char = sorted_chars[index]
    for num in angka:
        if num in char_to_num.values():
            continue
        if num == 0 and char in [word[0] for word in words]:
            continue
        char_to_num[char] = num
        if solve(index + 1):
            return True
        del char_to_num[char]
    return False

timenow = time.time()
if not solve():
    print("No solution found")
print(f"Execution time: {time.time() - timenow:.2f} seconds")