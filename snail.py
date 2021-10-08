snail._map =[ list(range(1,7)),
        list(range(7,13)),
        list(range(13,19)),
        list(range(19,25)),
        list(range(25,31)),
        list(range(31,37),
             )
        ]
n = 9
snail_map=[]
start = 1
end = n+1
for row in range(n):
    snail_map.append(list(range(start,end)))
    start = end
    end += n

for i in snail_map:
    print(i)
    

n = len(snail_map[0])
list1 = []
length = n
for i in range(n//2):
    # horizontal forwards
    for index in range(i,length):
        # snail._map[row][column]
        list1.append(snail_map[i][index])
    # vertical downwards - range(start,stop,step)
    for index in range(i+1,length):
        list1.append(snail_map[index][length-1])
    # horizontal backwards
    for index in range(length-2,i-1,-1):
        list1.append(snail_map[length-1][index])
    # vertical upwards
    for index in range(length-2,i,-1):
        list1.append(snail_map[index][i])
    length -= 1

return list1

print(list1)