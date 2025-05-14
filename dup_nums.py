# Read 2000-number file
with open("indian_2000_unique_mobile_numbers.txt", "r") as f1:
    numbers_2000 = set(line.strip() for line in f1)

# Read 100000-number file
with open("indian_100000_unique_mobile_numbers.txt", "r") as f2:
    numbers_100000 = set(line.strip() for line in f2)

# Find common numbers (present in both files)
common_numbers = numbers_2000.intersection(numbers_100000)

# Print all common numbers
print(f"✅ Total common numbers found: {len(common_numbers)}\n")
for number in sorted(common_numbers):
    print(number)
