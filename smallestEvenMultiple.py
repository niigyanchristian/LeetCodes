def smallestEvenMultiple(n):
    result = n
    while True:
        if result % 2 == 0 and result % n == 0:
            return result
        result += n

# Example usage:
n = 5
print(smallestEvenMultiple(n))