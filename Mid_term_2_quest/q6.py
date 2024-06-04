# 7. Print the valid parentheses with the value of n

def generate_parentheses(n):
    result = []
    generate_all_combinations(result, "", n, n)
    return result

def generate_all_combinations(result, current, open_remain, close_remain):
    if open_remain == 0 and close_remain == 0:
        result.append(current)
        return
    if open_remain > 0:
        generate_all_combinations(result, current + "(", open_remain - 1, close_remain)
    if close_remain > open_remain:
        generate_all_combinations(result, current + ")", open_remain, close_remain - 1)

# Example usage
n = 3
result = generate_parentheses(n)
print("Valid parentheses combinations for n =", n, ":", result)
