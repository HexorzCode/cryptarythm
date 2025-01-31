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

angka = list(range(10))
def hitung():
    for perm in permutations(angka, len(unique_chars)):
        char_to_num = dict(zip(unique_chars, perm))
        
        if any(char_to_num[word[0]] == 0 for word in words):
            continue
        
        num1 = int(''.join(str(char_to_num[char]) for char in word1))
        num2 = int(''.join(str(char_to_num[char]) for char in word2))
        num3 = int(''.join(str(char_to_num[char]) for char in word3))
        num4 = int(''.join(str(char_to_num[char]) for char in answr))
        if num1 + num2 + num3 == num4:
            print(f"Solution found: {char_to_num}")
            print(f"Answer is : {num4}")
            return True
    return False

timenow = time.time()
if not hitung():
    print("No solution found")
print(f"Execution time: {time.time() - timenow:.2f} seconds")
