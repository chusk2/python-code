¨¨¨¨
Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by .

Example

ar = [1,2,3,4,5,6]
k = 5

Three pairs meet the criteria: [1,4], [2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs

Input Format

The first line contains  space-separated integers,  and .
The second line contains  space-separated integers, each a value of .

Constraints
2 <= n <= 100
1 <= k <= 100
1 <= ar[i] <= 100

Sample Input

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
¨¨¨¨
from random import randint as rnd

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ar.sort()
    #ar = [1, 1, 2, 2, 3, 6]
    counter = 0
    for index,value in enumerate(ar) :
        for i in ar[index+1:] :
            # check wether i < j and is divisble by 3
            if (value<i) and (value+ i)%3 == 0 :
                counter += 1
    return counter
n = rnd(2,101)
dic = {k:ar for k,ar in zip([rnd(1,101) for i in range(n)],[ [rnd(1,101) for i in range(n)] ] ) }
print(dic)
for i,j in dic.items() :
    print(i,j)
