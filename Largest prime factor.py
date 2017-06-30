# coding = utf-8

num = 600851475143
large_prime = 2
while large_prime < num:
    while num % large_prime == 0:
        num = num / large_prime
    large_prime += 1
if num == 1:
    print large_prime - 1
else:
    print large_prime
