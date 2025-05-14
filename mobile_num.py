import random

def generate_unique_mobile_numbers(n):
    numbers = set()
    while len(numbers) < n:
        first_digit = str(random.choice([6, 7, 8, 9]))
        other_digits = ''.join(random.choices("0123456789", k=9))
        number = first_digit + other_digits
        numbers.add(number)
    return list(numbers)

# Generate 2000 unique numbers
mobile_numbers = generate_unique_mobile_numbers(100000)

# Save to a .txt file
with open("indian_unique_mobile_numbers.txt", "w") as file:
    for num in mobile_numbers:
        file.write(num + "\n")

print("✅ 2000 unique mobile numbers saved to 'indian_unique_mobile_numbers.txt'")
