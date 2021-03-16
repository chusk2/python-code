list = []
ops = []
N = 12
#N = int(input())
# for i in range(N) :
#     string = input().split()
#     # array with all the operations
#     ops.append(string)
ops = ['insert 0 5','insert 1 10','insert 0 6','print','remove 6','append 9','append 1','sort','print','pop','reverse','print']
for j in ops :
    j = j.split()   
    operation = j[0]
        
    if len(j) == 2 :
        e = int(j[1])
    elif len(j) == 3 :
        i = int(j[1])
        e = int(j[2])
            
    if operation == 'insert' :
        list.insert(i,e)
    elif operation == 'print' :
        print(list)
    elif operation == 'remove' :
        list.remove(e)
    elif operation == 'append' :
        list.append(e)
    elif operation == 'sort' :
        list.sort()
    elif operation == 'pop' :
        list.pop()
    elif operation == 'reverse' :
        list.reverse()
