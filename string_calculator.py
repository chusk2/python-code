expression_string ='-2 - 3 + 5 * 322 + 78 / -20'

# list of allowed signs in expression
allowed_signs = ['+','-','*','/']

def eval_expression(string) :
    """Takes a string expression and manipulates it to return a valid math expression.
       1st :   Remove whitespaces
       2nd :   Check if there are '+' or '-' signs 
               and change the numbers to positive or negative integers.
        3rd :   Return a list of integers mixed with multiplication, division and/or power operations.
    """
    # clean expression from whitespaces
    string=string.replace(' ','')
    # print(expression)

    number_str ='' # string with to fill up with numbers separated by whitespace
    expression = [] # list containing the numbers with its signs and operations

    # iterate using a counter to find out its position if it is a sign
    for i in string : 
        
        # add to number_str if element is a number
        if i.isnumeric() :
            number_str += i
        else :
            # when coming up with a sign or operation sign
            # 1st : empty number_str only if has some content
            #       and convert it to integer
            # 2nd : add the sign to expression
            # 3rd : append integer 
            if number_str : 
                expression.append( int(number_str) )
            number_str =''
            expression.append(i)
        # if i = last element and there are no more signs or operations,
        # "else" has not been evaluated.
        # Therefore, number_str has not been appended to list.
        # Solve this by just adding the content of number_str to expression
        if i == string[-1] :
            expression.append( int(number_str) )

    ## result of previous block is a list of integers and signs ('+','-','*','/','^')

    # Let us clean the expression from '+' or '-' signs
    # by converting the numbers to positive or negative integers

    expression_clean =[] # list without addition or substractions
    position = 0 # I use a counter to work with indexes and slices from expression list
    while position < len(expression) : # repeat cleaning until last element of expression is reached
        
        # if come up with a '+', merge the sign and following number into a positive integer
        if expression[position] == '+' :
            expression_clean.append( expression[position+1] )
            position += 2 # skip to positions to reach next sign or number
        # if come up with a '-', merge the sign and following number into a negative integer
        elif expression[position] == '-' :
            expression_clean.append( - expression[position+1] )
            position += 2 # skip to positions to reach next sign or number
        # just add the number or '*','/' sign and skip only 1 position
        else :
            expression_clean.append( expression[position] )
            position += 1 

    # substitute the expression by its first cleaned version
    expression = expression_clean

    ## result of previous block is a list of positive and negative integers and signs ('*','/','^')

    ## This block works out the multiplications, divisions and powers

    # continue while there are multiplications of divisions within the expression
    while ('*' in expression) or ('/' in expression or '^' in expression) :
        
        # check if a multiplication or division must be calculated
        if '*' in expression:
            position = expression.index('*') # find the position of the first multiplication
            operation = '*'
        elif '/' in expression :
            position = expression.index('/') # find the position of the first division
            operation = '/'
        else : # only remaining option is operation is power (^)
            position = expression.index('^') # find the position of the first division
            operation = 'power'
        
        previous  = expression[position - 1] # take previous number to * or /
        following = expression[position + 1] # take following number to * or /
        # start and finish positions of the slice that will be substituted with result of operation
        start  = position - 1
        finish = position + 2 # it must include +1 position because slices do not include finish position
        
        ## Checking sign of previous number       
        # If previous number is positive, it is ok
        if expression[position -2] == '+' :
            start -= 1 # expand the start of the slice to include the sign
        # If previous number is negative, set it to negative integer 
        elif expression[position -2] == '-' :
            previous = - previous
            start -= 1 # expand the start of the slice to include the sign
        
        ## Checking sign of following number       
        # If previous number is positive, it is ok
        if following == '+' :
            following = expression[position + 2] # take next element, which actually contains the number
            finish += 1 # expand the start of the slice to include the sign
        # If previous number is negative, set it to negative integer
        elif following == '-' :
            following = - expression[position + 2] # take next element, which actually contains the number
            finish += 1 # expand the start of the slice to include the sign
        
        # substitute the previous and following number,
        # both with their signs, by the result of the multiplication or division
        # use list slicing to change elements in the expression
        if operation == '*' :
            expression[ start : finish ] = [ previous * following ]
        elif operation == '/' :
            expression[ start : finish ] = [ previous / following ]
        # if not * nor / , operation must be power (^)
        else :
            expression[ start : finish ] = [ previous ** following ]
        
        # check if one more iteration is needed to work out
        # a multiplication or a division
        #multiply = '*' or '/' in expression
    # the result is obtained summing up all the elements in expression
    print(expression)
    return sum(expression)

def extract_blocks(expression) :

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

    expressions_list =[]
    for start,end in block_slices :
        math =''
        for i in expression[start+1:end] :
            math += i
        expressions_list.append(math)
    
    return expressions_list

## Ask for an expression to be evaluated

ask_again = True
while ask_again :
    print('\nEnter a valid math expression. Only * , /, ^, + and - signs are allowed.')
    expression_string = input('\nMath expression: ')
    # check the validity of the given expression
    ask_again = False
    for i in expression_string :
        if i.isdigit() or ( i in ['(',')','+','-','*','/','^'] ) :
            continue
        else :    
            print('Invalid expression. Try again.')
            ask_again = True
            break

expressions_list = extract_blocks (expression_string)

results =[]

for block in expressions_list :
    results.append( eval_expression(expression_string) )

print(f'The evaluated expression was: {expression_string}.\nIts result is: {result}')