expression = '3+(2+5)+(23*4+4)+2-3*(32*4/2)+5'


## clean whitespaces elements
expression = [i for i in expression if i != '']
print(expression)

## locate the parenthesis
open_items = [ '(' , '[' , '{' ]
close_items =[ ')' , ']' , '}' ]

positions =[]

for i in range(len(expression)) :
    if expression[i] in open_items :
        positions.append( i ) # add the position of a opening parenthesis
    elif expression[i] in close_items :
        positions.append(  - i ) # add the position of a closing parenthesis
print(positions)

## delimita los paréntesis
stack =[]
block_slices =[]
for i in positions :
    if i >= 0 :
        stack.append(i)
    elif i < 0 :
        stack.append( -i)
        # add a tuple with the start,finish positions of the parenthesis
        block_slices.append( tuple(stack[-2:]) ) 
        # remove the last tuple from the stack
        stack[-2:] = []
print(block_slices)

for start,end in block_slices :
    math =''
    for i in expression[start+1:end] :
        math += i
    print(math)


    


















# # Python3 code to Check for  
# # balanced parentheses in an expression 
# open_list = ["[","{","("] 
# close_list = ["]","}",")"] 
  
# # Function to check parentheses 
# def check(exp): 
#     slice = [] 
#     for i in exp: 
#         if i in open_list: 
#             slice.append( exp.index(i) ) 
#         elif i in close_list: 
#             slice.append(close_list.index(i) 
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])): 
#                 stack.pop() 
#             else: 
#                 return "Unbalanced"
#     if len(stack) == 0: 
#         return "Balanced"
#     else: 
#         return "Unbalanced"
  
  
# # Driver code 
# string = "{[]{()}}"
# print(string,"-", check(string)) 
  
# string = "[{}{})(]"
# print(string,"-", check(string)) 
  
# string = "((()"
# print(string,"-",check(string)) 
