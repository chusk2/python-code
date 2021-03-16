def func(*args) :
    sum = 0
    for i in args :
        sum += i
    print(f'La suma de los elementos es: {sum}')
    print(f'La media de los elementos es: { sum/len(args) }')