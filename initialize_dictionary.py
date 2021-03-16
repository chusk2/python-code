employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

dic = {name:{} for name in employees}

for name in employees :
    for k,v in defaults.items() :
        dic[name].setdefault(k,v)

dic['John']['designation'] = 'Senior Developer'
dic['John']['salary'] = 15000

for key,value in dic.items() :
    print(f'{key:<10} - \tPosition: {value["designation"]:<15}\tWage: ${value["salary"]:>8.2f}')