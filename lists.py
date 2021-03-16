def seq(lista) :

    # check lista lenght

    n = len(lista)
    sum = 0
    i = 0
    x = 0
    matrix=[]
    while sum < n :
        x += 1
        sum += x
    
    max_size = x # size of the first row of matrix
    sizes = [i for i in range(x,0,-1)] # list with lengths of rows
    if sum != n : # length not valid
        return []
    
    else : # valid lenght, create triangular matrix

        start = 0 # start position of slice
        for size in sizes :
            last_position = size
            matrix.append(lista[start:last_position])
            start += last_position
    
    return matrix

print(seq([1,2,3,4,5,6]))



