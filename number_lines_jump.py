"""
Number Line Jumps

https://www.hackerrank.com/challenges/kangaroo/problem

You are choreographing a circus show with various animals.
For one act, you are given two kangaroos on a number line ready to jump
in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time
as part of the show. 

### If it is possible, return YES, otherwise return NO. ### """


def kangaroo(x1, v1, x2, v2):
    meet = ''
    num = x1-x2
    denom = v2-v1
    if denom == 0 :
        if num == 0 :
            meet = 'YES'
        else :
            meet='NO'
        return meet
    
    t = num / denom
    # check if t is integer and not float
    str_time = str(t)
    
    if str_time[str_time.index('.'):] != '.0' :
        decimal = True
    else :
        decimal = False
    ### VERY IMPORTANT ###
    ### t = number of hops, must be an integer
    ### if both kangaroos meet at t = 0.7, the would fisically meet
    ### in the air, but actually not on the ground.
    ### number of hops (t) must be integer!!
    if t>= 0 and not decimal :
        meet = 'YES'
    else :
        meet = 'NO'
    
    return meet

#print(kangaroo(0,3,4,2))
#YES
#print(kangaroo(4181,3976,6312,988))
# NO