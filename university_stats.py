universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def mean(values:list) -> int :
    return sum(values)/len(values)

def median(values:list) -> int :
    if len(values) % 2 == 0 :  # there is an even number of data
        mid_point = len(values)//2 
        median = values[mid_point] + values[mid_point+1]
    else :
        mid_point = (len(values) -1 )//2  # result must be int, not float
        median = values[mid_point]

def enrollment_stats(universities_data:list) -> list :
    '''Takes, as an input, a list of lists where 
    each individual list contains three elements:
    
    (a) the name of a university
    (b) the total number of enrolled students
    (c) the annual tuition fees.
    
    Example:
    universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849] ]

    enrollment_stats() returns two lists: 
    1) list containing all of the student enrollment values
    2) list containing all of the tuition fees.'''

    num_students = []
    tuition_fees = []

    for university in universities_data :
        num_students.append(university[1])
        tuition_fees.append(university[2])
    
    total_students = sum(num_students)
    total_tuition = sum(tuition_fees)

    mean_students = mean(num_students)
    median_students = median(num_students)

    mean_tuition = mean(tuition_fees)
    median_students = median(tuition_fees)

    print('*'*40)
    
    print(f'\nTotal students:{total_students}:,>10')
    print(f'Total tuition:${total_tuition}:,>10')

    print(f'Students mean:{mean_students}:,.2f>10')
    print(f'Students median:{median_students}:,.2f>10')

    print(f'Tuition mean:${mean_tuition}:,.2f>10')
    print(f'Tuition median:${median_students}:,.2f>10')

    print('\n'+'*'*40)

enrollment_stats(universities)
'''
******************************
Total students: 77,285
Total tuition: $ 271,905

Student mean: 11,040.71
Student median: 10,566

Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************
'''

