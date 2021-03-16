from random import randint

def find_index(num,string) :
    indexes=[]
    i = -1
    while num in string[i+1:] :  # search in slice of string starting one position after last coincidence
        i = string.index(num,i+1) 
        indexes.append(i)
    return indexes

number_to_find = str(randint(1,9))

list_numbers = [randint(1,9) for i in range(30)]

list_numbers_str = [str(i) for i in list_numbers]
list_numbers_str = ''.join(list_numbers_str)

while not number_to_find in list_numbers_str :
    number_to_find = str(randint(1,9))

print (find_index(number_to_find,list_numbers_str) )



    
