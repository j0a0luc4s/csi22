from math import sqrt

def primes():

    def check_prime(current, primes):
        sqrt_current = sqrt(current)
        for prime in primes:
            if sqrt_current < prime:
                return True
            if current % prime == 0:
                return False 
        return True

    primes = []
    current = 2
    while True:
        if check_prime(current, primes):
            primes.append(current)
            yield current
        current = current + 1
