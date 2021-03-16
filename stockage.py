#!/usr/bin/env python3

# Create a dictionary with the following fields

fields=['ID','Name','Price','Models']

product=dict.fromkeys(fields)

product_list= [
    ['RB00111' , 'Rayban Sunglasses' , 112.98 , ['black', 'tortoise'] ],
    ['DWC0317' , 'Drone with Camera' , 72.95, ['white' , 'black'] ],
    ['MTS0540' , 'T-Shirt' , 2.95 , ['small', 'medium', 'large'] ],
    ['ECD2989' , 'Echo Dot' , 29.99 , [] ]
    ]

# create a list of pairs of [key,value] to populate the stockage dict
items_for_stockage = []

for item in product_list :
    stockage_item = list ( zip (fields,item) )
    items_for_stockage.append(stockage_item)

for j in items_for_stockage :
    print(j)

stockage = {}
for item in items_for_stockage :
    stockage.update ( { item[0][1] : { key:value for key,value in item } } )
    
print(f'{product_list[0]:<9}')



# Create a database with all the items in product_list
# Each item has a database entry in the form of dictionary with fields

    

## Now let's fill the data of every item in the stockage database
    
# for item in stockage.keys():
#     counter = 0
#     for field in item.keys() :
#         item[field] = product_list[counter]
#         counter +=1

# for i in range( len(stockage) ) :
#print( stockage )
    



