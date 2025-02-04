def _calculate_prime_numbers(number):
    if number < 2:
        return []

    primes = []
    for num in range(2, number + 1):  # Iterate up to 'number'
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):  
            if num % divisor == 0:
                is_prime = False
                break  # No need to check further, it's not a prime
        
        if is_prime:
            primes.append(num)

    return primes

print(_calculate_prime_numbers(37))  
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
