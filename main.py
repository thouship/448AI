def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False  # Not a prime number
        else:
            return True  # It is a prime number
    else:
        return False  # Not a prime number

# Loop to test numbers from 3 to 100 (inclusive)
for num in range(3, 101):
    if is_prime(num):
        print(num, "is a prime number")
