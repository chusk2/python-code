#A = [1,2,3,5,4]
#A=[1, 3, 4, 2]
#A=[3,1,2]
#A=[1,6,5,2,4,3]
A=[1, 6, 5, 2 ,3, 4]
##### TO FIX: FIRST ELEMENT IS NOT ALWAYS 1!!!!! ######


def larrysArray(A) :
    # a copy to store sorted array
    A_sorted = A
    first_index_triplet = 0
    triplet = A_sorted[first_index_triplet : first_index_triplet + 3]
    next_value = min(triplet)
    # in an array of n numbers there are n-2 possible triplets
    for i in range(len(A)-2) :
        # select a triplet (a,b,c)
        triplet = A_sorted[first_index_triplet : first_index_triplet + 3]
        # check if next desired value is in selected triplet
        if next_value in triplet :
            
            # check if triplet is already sorted
            if triplet != sorted(triplet) :
                break
            # try, rotating the triplet, to get
            # a sorted triplet whithin 3 attemps at most
            for i in range(3) :
                # rotate
                first_item = triplet.pop(0)
                triplet.append(first_item)
                # if achieved the sorted triplet, stop rotating
                if triplet == sorted(triplet) :
                    break
            
            if triplet == sorted(triplet) :
                # replace the old triplet with the sorted one
                A_sorted[first_index_triplet : first_index_triplet + 3] = triplet
            # if it was not possible to sort the triplet
            # within 3 rotation attemps, then it is not a larry's Array
            # return NO
            else :
                return 'NO'
            
            # print the current array
            print(A_sorted)
            # search for the next value in progression
            next_value += 1
            # shift the index for next triplet in array
            first_index_triplet += 1
    return 'YES'
print(larrysArray(A))

  



