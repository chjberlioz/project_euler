# coding = utf-8


def reverse_num(n):
    reverse_n = 0
    while n > 0:
        last_digit = n % 10
        reverse_n = reverse_n * 10 + last_digit
        n = (n - last_digit) / 10
    reverse_n += n
    return  reverse_n


def is_palindrome(n):
    if n == reverse_num(n):
        return True
    else:
        return False

largest_palindrome = 0
small_num = 999
while small_num >= 100:
    large_num = 999
    while large_num >= small_num:
        if is_palindrome(large_num * small_num):
            if large_num * small_num > largest_palindrome:
                largest_palindrome = large_num * small_num
                break
        large_num -= 1
    small_num -= 1
print largest_palindrome