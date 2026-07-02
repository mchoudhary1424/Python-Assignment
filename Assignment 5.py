
# 1) Repeat a Tuple Three Times (*)

tup1 = (1, 2, 3)
repeated_tup = tup1 * 3

print("--- 1) Repeated Tuple ---")
print(f"Original: {tup1}")
print(f"Repeated: {repeated_tup}\n")



# 2) Join Three Separate Tuples (+)

ta = (10, 20)
tb = (30, 40)
tc = (50, 60)
joined_tup = ta + tb + tc

print("--- 2) Joined Tuples ---")
print(f"Combined Tuple: {joined_tup}\n")



# 3) Check Element Existence (in)

fruits = ("apple", "banana", "cherry")
target = "banana"

print("--- 3) Tuple Membership Check ---")
if target in fruits:
    print(f"Yes, '{target}' exists in the tuple.")
else:
    print(f"No, '{target}' does not exist in the tuple.")
print()



# 4) Manual Total, Max, and Min (No built-ins)

numbers_tup = (15, 42, 7, 89, 23, 5)

# Initialize variables using the first element
total = 0
highest = numbers_tup[0]
lowest = numbers_tup[0]

for num in numbers_tup:
    total += num
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print("--- 4) Manual Tuple Statistics ---")
print(f"Tuple: {numbers_tup}")
print(f"Total Sum:     {total}")
print(f"Highest Value: {highest}")
print(f"Lowest Value:  {lowest}\n")


# ==========================================
# 5) Filter Tuple (Values > 10)
# = : (3, 14, 7, 22, 9, 41, 18, 5)
# ==========================================
n = (3, 14, 7, 22, 9, 41, 18, 5)

# Using a generator/tuple comprehension to filter
filtered_list = []
for val in n:
    if val > 10:
        filtered_list.append(val)
filtered_tup = tuple(filtered_list)

print("--- 5) Filtered Tuple ---")
print(f"Original Tuple: {n}")
print(f"Values > 10:    {filtered_tup}\n")



# 6) Count Set Elements Manually (No len())

s = {"cat", "dog", "bird", "fish"}
set_count = 0

for item in s:
    set_count += 1

print("--- 6) Manual Set Length ---")
print(f"Set: {s}")
print(f"Number of elements: {set_count}\n")



# 7) Combine Two Sets (All Unique Elements)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
combined_set = set_a.union(set_b)  # or set_a | set_b

print("--- 7) Combined Sets (Union) ---")
print(f"Combined Unique: {combined_set}\n")



# 8) Find Common Elements (Intersection)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
common_elements = s1.intersection(s2)  # or s1 & s2

print("--- 8) Common Elements (Intersection) ---")
print(f"Common elements: {common_elements}\n")



# 9) Elements in either set but NOT both (Symmetric Difference)

# (Completed text from cutoff: "elements that are in either set but not both")
either_not_both = s1.symmetric_difference(s2)  # or s1 ^ s2

print("--- 9) Elements in Either But Not Both ---")
print(f"Symmetric Difference: {either_not_both}")
