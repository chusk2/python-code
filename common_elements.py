"""
List Overlap Comprehensions

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension."""

from random import randint

len1 = randint(1,15) # length of the first list
len2 = randint(1,15) # length of the second list

# create two lists of random numbers
a = [randint(1,20) for i in range(len1)]
b = [randint(1,20) for i in range(len2)]

common = [] # a list to content all the common elements

if len1 >= len2 :
    for element in b :
        if (element in a) and not (element in common) :
            common.append(element)
else :
    for element in a :
        if element in b and not element in common :
            common.append(element)

print(f'\nFirst list has {len1} elements: {a}')
print(f'Second list has {len2} elements: : {b}')
print(f'{len(common)} element(s) in common: {common}') if len(common) != 0 else print('There are no common elements.')
         
