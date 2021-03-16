'''Consider the following algorithm to generate a sequence of numbers. Start with an
integer n.If n is even, divide by 2. If n is odd, multiply by 3 and add 1.
Repeat this process with the new value of n, terminating when n = 1. For example,
the following sequence of numbers will be generated for n =
22: 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1'''


from random import randint as rnd

n = rnd(1,100)
print(n, end = ' ')
while n != 1 :
    if n % 2 == 0 :
        n = n // 2
    elif n % 2 != 0 :
         n = 3 * n + 1
    print(n, end=' ')

