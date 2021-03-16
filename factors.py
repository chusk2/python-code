def getTotalX(a, b):
    """
    Given two arrays of integers.
    For an integer n to be selected, must meet two conditions:
    
    1. All the elements of 1st array MUST BE FACTORS of n
    2. n MUST BE A FACTOR of every element in the 2nd array
    """
           
    #a.sort(reverse = True )
    #b.sort(reverse = True )
    
    # the maximum common factor of b must be
    # between the factors of the minimun value of b
    
    min_value_b = min(b)
    
    # get the factors of the minimum value in b
    factors_b =[]
    
    for n in range(1,min_value_b+1) :
        if min_value_b % n == 0 :
            factors_b.append(n)
    
    ### 1st selection process ###
       
    # the selected integers from this selection progress
    # will be stored in "first_pass" list
    first_pass = []
    
    # check if the factors inside factors_b
    # are also factors of the rest of elements in b
    for factor in factors_b :
        
        # Unless it is not a common factor, add it to 1st pass list
        add_factor = True
        
        for i in b :
            # factor is not factor of an element in b
            if i % factor != 0 :
                # do not add it to first pass list
                add_factor = False
                # do not keep on checking this factor
                break
        # if passed all test, go ahead and add it
        if add_factor :
            first_pass.append(factor)
    
    ## End of 1st selection process ##
    
    ### 2nd selection process ###
       
    # the selected integers from this selection progress
    # will be stored in "second_pass" list
    second_pass = []
    
    # check if all the elements of a are factors
    # of every element inside first_pass list
    for factor in first_pass :
        
        # add factor to successful list unless factor
        # does not pass all the tests
        add_integer = True
        
        # factor must be tested against all elements in a
        for i in a :
            # if there is an element of a
            # which is not a factor of "factor" from first_pass list
            # do not add it to second_pass list
            if factor % i != 0 :
                add_integer = False
                break
        # if factor passed all tests, add it to second_pass list
        if add_integer :
            second_pass.append(factor)
    ### End of 2nd selection process ###
            
    return len(second_pass)

print(getTotalX([2,4], [16,32,96]) )
# Input
# [2,4]
# [16,32,96]
# Output: 3
# three elements
        