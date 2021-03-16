defaults = {"designation": 'Application Developer', "salary": 8000}
employees = ['Kelly', 'Emma', 'John']

employees = {}.fromkeys(employees)
print(employees)

for key,value in employees.items() :
    employees[key] = {}

    for k,v in defaults.items():
        employees[key].setdefault(k,v)

for key,value in employees.items() :
    print(f'{key} : {value}')

with open('file' , 'w+' , encoding='utf-8') as f :
    for i in range(1,11) :
        f.write('This is the line number: ' + str(i) + '\n' )
        # important to add \n break line because otherwise, it will write one letter after another.

with open('file' , 'r') as f :
    content = f.readlines()
    for line in content :
        print(line)