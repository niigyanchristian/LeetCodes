# SOLUTION 1
def countPrimes_1(n):
    count = 0
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime =  False
        if is_prime:
            count += 1
    return count


# SOLUTION 2
def countPrimes_2(n):
    if n <= 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    count = sum(is_prime)
    return count



# Example usage:
result_1 = countPrimes_1(10)
result_2 = countPrimes_2(10)
print(result_1,result_2)