#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1. Note: n and p will always be given as strictly positive integers.

def dig_pow(n, p):
    digit_powers_sum = sum(int(digit) ** (i + p) for i, digit in enumerate(str(n)))
    k, remainder = divmod(digit_powers_sum, n)
    return k if remainder == 0 else -1

n = int(input("Enter a positive integer n: "))
p = int(input("Enter a positive integer p: "))

result = dig_pow(n, p)
if result != -1:
    print(f"The value of k is {result}.")
else:
    print("No value of k exists.")

#best practice code
# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)):
#      s += pow(int(c),p+i)
#   return s/n if s%n==0 else -1