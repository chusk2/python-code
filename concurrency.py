phrase=input('Type a word or phrase to count its letters: ')
letter = input('Choose a letter to count its concurrence in the given phrase: ')

positions =[ ]

for i,j in enumerate(phrase): # enumerate the list phrase in two lists: i for indexes and j for items in list phrase
    
    if j == letter :
        
        positions.append(i) # if there's a concurrence, add its position index to positions list

if len(positions) == 0 :
    
    print(f'La letra \"{ letter }\" no se encuentra en la frase.')

elif len(positions) == 1 :
    
    print(f'La frase contiene solo una vez la letra \"{letter}\" y está colocada en la posición { positions[0] }.')

else :
    
    print(f'La frase contiene { len(positions)  } veces la letra \"{letter}\" y están colocadas en las posiciones:', end=' ')
    for i in positions :
        
        if i == positions[-2] :
            print(i, end=' ')
        
        elif i == positions[-1] :
            print (f'y {i}.')
        
        else :
            print( i, end=', ')