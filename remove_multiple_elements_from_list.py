lst=[2, 5, 1, 2, 7, 5, 8, 8, 12, 3, 2,5,2,4,5,2]
print(lst)
# for i,j in enumerate(lst) : # for loop to find and remove all concurrences of an element within a list
#     if j == 2 :
#         lst.pop(i)
#         
# print(lst)

# function how_may returns the times "element" appears in list "lst"
# it takes a list and an element to look up within provided list
def how_many(lst,element) :

    positions = []
    times = 0
    
    if element in lst :
        for i,j in enumerate(lst) :
            if j == element :
                times += 1
                positions.append(i)
    return times, positions

# store in vars n and pos the return of the call of the how_many function
n,pos = how_many(lst,2)

print(f'El número 2 aparece { n } veces en la lista, en las posiciones {pos}.')

# sorted(list) returns a sorted copy of the list w/o changing the original list
#list.sort() sorts the original list and the changes are permanent
# Add reverse=True) as a parameter to sort in reverse order (works in both function ( sorted() ) and method (list.sort() )
 
n,pos = how_many(sorted(lst),2)

print(f'El número 2 aparece { n } veces en la lista, en las posiciones {pos} cuando la lista está ordenada.')
# reverse the elements of a list
lst.reverse()
print(lst)