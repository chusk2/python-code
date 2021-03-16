def migratoryBirds(arr):
    # select the unique id's in the arr
    id_list = list( set(arr) )
    # count how many times each id appears
    amounts = []
    for element in id_list :
        amounts.append(arr.count(element))
    # find the maximum of amounts
    max_amount = max(amounts)
    # the position of the max in amounts list
    # determines the position of the id in the id_list
    position_maximum_id = amounts.index(max_amount)
    # return the maximum id
    return id_list[position_maximum_id]

print(migratoryBirds([1,4,4,4,5,3]))