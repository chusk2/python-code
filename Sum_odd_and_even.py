from random import randint

nums = [randint(1,100) for i in range(20) ]

evens = [ i for i in nums if i%2 == 0]
odds = [ i for i in nums if i%2 != 0]
print(nums)
print(f'The sum of the even numbers is {sum(evens)}')
print(f'The sum of the odds numbers is {sum(odds)}')

