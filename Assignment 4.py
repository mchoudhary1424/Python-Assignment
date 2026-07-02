
#  List Analysis (15 Numbers)

numbers = [12, 45, 7, 23, 56, 89, 34, 2, 90, 67, 11, 4, 78, 53, 22]

# Calculate sum, average, max, and min
total_sum = sum(numbers)
mean = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

# Count even and odd numbers
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("--- 1) List Analysis Results ---")
print(f"List: {numbers}")
print(f"Total Sum: {total_sum}")
print(f"Arithmetic Mean: {mean:.2f}")
print(f"Largest Value: {largest}")
print(f"Smallest Value: {smallest}")
print(f"Even Numbers Count: {even_count}")
print(f"Odd Numbers Count: {odd_count}\n")



# Accessing Elements in a Nested List

nested_list = [10, 11, 102, [1, 2], [3, 4, 5], [6, 7]]

# The sub-list [3, 4, 5] is at index 4. The number 5 is at index 2 inside that sub-list.
accessed_value = nested_list[4][2]

print("--- 2) Access Nested List ---")
print(f"Accessed Value: {accessed_value}\n")



#  Check If Value Exists in a List

inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target = "Tablet"

print("--- 3) Inventory Check ---")
if target in inventory:
    print(f"Success: {target} is currently in stock.")
else:
    print(f"Notice: {target} is missing from the inventory.")
print()



#  Delete Every Instance of a Specific Value

original_list = [5, 20, 15, 20, 25, 50, 20]
item_to_remove = 20

# Use a loop to remove the item as long as it exists in the list
while item_to_remove in original_list:
    original_list.remove(item_to_remove)

print("--- 4) Remove Items ---")
print(f"Cleaned List: {original_list}\n")



 # Dictionary Mapping From Two Lists

keys = ["name", "age", "city"]
values = ["ABC", 25, "Jaipur"]

# Map lists using the zip function paired with dict()
mapped_dict = dict(zip(keys, values))

print("--- 5) Mapped Dictionary ---")
print(f"Resulting Dictionary: {mapped_dict}\n")


#  Retrieve Value From Nested Dictionary

person = {
    "name": "ABC", 
    "address": {
        "city": "Jaipur"
    }
}

# Access the nested key chain
retrieved_city = person["address"]["city"]

print("--- 6) Nested Dictionary Retrieval ---")
print(f"Retrieved City: {retrieved_city}")
