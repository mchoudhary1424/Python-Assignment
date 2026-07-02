
# 1. Maximum of Three Numbers

def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c



# 2. Get Distinct Elements from a List

def get_unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list



# 3. Multiply All Numbers in a List

def multiply_list_elements(lst):
    if not lst:
        return 0
    result = 1
    for num in lst:
        result *= num
    return result



# 4. Calculate Factorial of a Number

def calculate_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



# 5. Reverse a String

def reverse_string(text):
    return text[::-1]



# 6. Check Range (Between 10 and 50)

def is_in_range_10_50(num):
    return 10 <= num <= 50



# 7. Filter and Print Even Numbers

def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print(f"Even Numbers: {even_numbers}")
    return even_numbers



# 8. Check if a Number is Prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 9. Count Upper and Lower Case Letters

def count_case_letters(text):
    counts = {"upper": 0, "lower": 0}
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
    return counts


# Quick Demonstration of the Functions

if __name__ == "__main__":
    print("1. Max of (12, 45, 19):", find_max_of_three(12, 45, 19))
    print("2. Unique items of [1,2,2,3,4,4,5]:", get_unique_elements([1,2,2,3,4,4,5]))
    print("3. Product of [2, 3, 4]:", multiply_list_elements([2, 3, 4]))
    print("4. Factorial of 5:", calculate_factorial(5))
    print("5. Reverse of 'Python':", reverse_string("Python"))
    print("6. Is 35 between 10 and 50?:", is_in_range_10_50(35))
    print("7. ", end="")
    print_even_numbers([1, 2, 3, 4, 5, 6])
    print("8. Is 17 prime?:", is_prime(17))
    print("9. Case count of 'Hello World!':", count_case_letters("Hello World!"))
