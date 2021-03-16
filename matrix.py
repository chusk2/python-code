# _*_ coding: utf-8 _*_
d = 3
m = 2

matrix = [1,2,1,3,2]
counter = 0
end = m
for i in range(len(matrix) - m ) :

    if sum(matrix[i:end]) == d :
        counter += 1
    end += 1
        
print(counter)

