from itertools import permutations
import time

def solve_cryptarithmetic(word1, word2, word3, result):
    # Get all unique characters
    chars = set(word1 + word2 + word3 + result)
    if len(chars) > 10:
        return None, "Too many unique characters"
    
    # Optimization 1: Identify first letters for leading zero check
    first_letters = {word1[0], word2[0], word3[0], result[0]}
    
    # Optimization 2: Pre-calculate positions and coefficients
    def calculate_coefficient(word):
        return {char: sum(10**(len(word)-i-1) for i, c in enumerate(word) if c == char) 
                for char in set(word)}
    
    coef1 = calculate_coefficient(word1)
    coef2 = calculate_coefficient(word2)
    coef3 = calculate_coefficient(word3)
    coef_result = calculate_coefficient(result)
    
    # Optimization 3: Sort characters by frequency and position importance
    char_importance = {}
    for char in chars:
        score = 0
        if char in first_letters:
            score += 1000
        score += sum([
            coef1.get(char, 0),
            coef2.get(char, 0),
            coef3.get(char, 0),
            coef_result.get(char, 0)
        ])
        char_importance[char] = score
    
    chars_ordered = sorted(chars, key=lambda x: char_importance[x], reverse=True)
    
    def evaluate(mapping):
        # Optimization 4: Direct calculation using pre-computed coefficients
        num1 = sum(mapping[char] * coef for char, coef in coef1.items())
        num2 = sum(mapping[char] * coef for char, coef in coef2.items())
        num3 = sum(mapping[char] * coef for char, coef in coef3.items())
        num_result = sum(mapping[char] * coef for char, coef in coef_result.items())
        return num1 + num2 + num3 == num_result
    
    def solve_recursive(index=0, used_digits=set(), mapping={}):
        if index == len(chars_ordered):
            return mapping if evaluate(mapping) else None
            
        char = chars_ordered[index]
        # Optimization 5: Smart digit selection based on character importance
        digits = range(1, 10) if char in first_letters else range(10)
        
        for digit in digits:
            if digit not in used_digits:
                mapping[char] = digit
                used_digits.add(digit)
                result = solve_recursive(index + 1, used_digits, mapping)
                if result:
                    return result
                used_digits.remove(digit)
                del mapping[char]
        return None

    # Start solving
    solution = solve_recursive()
    if solution:
        # Calculate result number
        result_num = sum(solution[char] * coef for char, coef in coef_result.items())
        return solution, result_num
    return None, "No solution found"

# Test the solver
start_time = time.time()
solution, result = solve_cryptarithmetic("alaska", "kansas", "nevada", "states")
execution_time = time.time() - start_time

print(f"Solution: {solution}")
print(f"Result: {result}")
print(f"Execution time: {execution_time:.4f} seconds")