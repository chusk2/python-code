def dirReduc(arr):
    #### SOLVED USING RECURSION ####
    #check the hole array por nonsense pairs
    # use enumerate to additionally get the index of the evaluated direction
    for index,direction in enumerate(arr) :
        # if there are no more pairs to check or it is the last direction in array
        if len(arr) == 1 or index == len(arr)-1:
            break
        # check N-S couple
        if direction =='NORTH' and arr[index+1] == 'SOUTH' :
            # remove both North and South directions
            arr.pop(index)
            # once you remove one item, the next inherites previous index
            arr.pop(index)
            # check again the NEW array with the new items
            dirReduc(arr)
        # check S-N couple
        elif direction =='SOUTH' and arr[index+1] == 'NORTH' :
            arr.pop(index)
            arr.pop(index)
            dirReduc(arr)
        # check W-E couple
        elif direction =='WEST' and arr[index+1] == 'EAST' :
            arr.pop(index)
            arr.pop(index)
            dirReduc(arr)
        # check E-W couple
        elif direction =='EAST' and arr[index+1] == 'WEST' :
            arr.pop(index)
            arr.pop(index)
            dirReduc(arr)
    # return the simplified array of directions
    return arr

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))