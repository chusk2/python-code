from random import randint as rnd

def sum_dices() :
    dice1 = rnd(1,6)
    dice2 = rnd(1,6)
    return dice1+dice2



#### THEORETICAL RESULTS ####

# create a list with the possible results of the sum of two dices roll
possible_results=[] 

for i in range(1,7) :
    for j in range(1,7) :
        possible_results.append(i+j)

# remove the repeated values using a set and then transforming it again into a list
possible_results = list( set(possible_results) )

# create an array to keep the combinations that yield certain result
array = [[] for i in range( len(possible_results) ) ] 

# create a dictionary where every result shows its possible combinations
combinations = { k:v for (k,v) in zip(possible_results,array) } 

# let's fill the combinations dictionary
# its contents are key = sum of dices , value = combinations that yield that sum of dices

for f in range(1,7) :
    for c in range(1,7) :
        combinations[f+c].append((f,c))

# create a copy but this time the values are the probabilities of yielding that result
theoretical_probability = combinations.copy()

# count the number of combinations that yield that result and find its relative frequency
for key,value in theoretical_probability.items() :
    theoretical_probability[key]=len(theoretical_probability[key])/36

# show the theoretical probability of each result
print('#### THEORETICAL PROBABILITIES ####\n')
print('Value\tTheoretical Probability\tExperimental Probability')

# for k,v in theoretical_probability.items() :
#     print(f'{k}\t{v:>10.2%}')

#### EXPERIMENTAL RESULTS ####
    
# generate a list with the results of 1000 dices rolls
results = [sum_dices() for i in range(1000)]

# create a dictionary --> value of the sum : times it appears in the results 
experimental_probability = dict.fromkeys(possible_results)

for value in possible_results :
    times = results.count(value)
    experimental_probability[value] = times / 1000

prob_table = list ( zip (theoretical_probability.keys(), theoretical_probability.values(), experimental_probability.values() ) )
for k,v1,v2 in prob_table :
    print(f'{k}\t{v1:>23.2%}\t{v2:>23.2%}')


print(combinations)


