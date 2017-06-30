# coding = utf-8

primes = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}


def num_prime(n, prime):
    num = 0
    while n % prime == 0:
        num += 1
        n /= prime
    return num


for i in range(1, 21):
    for each_prime in primes:
        if primes[each_prime] < num_prime(i, each_prime):
            primes[each_prime] = num_prime(i, each_prime)
multi = 1
for i in primes:
    multi *= i ** primes[i]
print multi
