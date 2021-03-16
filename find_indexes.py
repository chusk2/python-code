lista = [ [ [1,2,3], 2, [1,3] ], [1,2,3] ] 

indexes=[]
def search_values(l=lista,item=2) :
    for element in l :
        if isinstance(element, list) :  ## check if element is an anidated list
            search_values(element,item)
        else :
            if element == item :
                indexes.append([l.index(element)])
    return indexes

print(search_values())

if __name__ == "__main__":
    pass