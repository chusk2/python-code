"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

#### To do: there is only one number different to 0 -> return that number
def find_outlier(integers):
    ### check whether they are odd or even numbers ###
    type =''
    # counter of times an integers
    # has been checked
    odds = 0
    evens = 0
    numbers_different_to_zero = [i for i in integers if i!=0]
    if len(numbers_different_to_zero) == 1 :
        return numbers_different_to_zero[0]
    for i in integers :
        if odds == 2 or evens == 2 :
            break
        if i == 0 :
            continue
        elif i % 2 == 0 :
            evens += 1
        else :
            odds += 1
    if odds == 2 :
        type = 'odds'
    elif evens == 2 :
        type = 'evens'
    
    ### return the outlier ###
    outlier = None
    for i in integers :
        if i != 0 :
            if type == 'odds' and (i % 2) == 0 :
                outlier = i
                break
            elif type == 'evens' and (i % 2) != 0 :
                outlier = i
                break
    if not outlier and 0 in integers :
        return 0
    else : return outlier
#print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 6, 8, 10, 0]))