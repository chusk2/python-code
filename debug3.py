# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ar.sort()
    #ar = [1, 1, 2, 2, 3, 6]
    counter = 0
    for index,value in enumerate(ar) :
        for i in ar[index+1:] :
            # check wether i < j and is divisble by 3
            if (value<i) :
                # check 3 divisibility
                # if the sum of all its digits is divisble
                # by 3, then the number is a multiple of 3
                ## split the digits transforming number into string
                digits =list(str(value+i))
                # convert again each digit into integer
                digits = [int(i) for i in digits]
                print(digits)
                # check if divisible by 3
                if sum(digits) % 3 == 0 :
                    counter += 1
    return counter
ar = [1, 1, 2, 2, 3, 6]
print(divisibleSumPairs(6,3,ar))