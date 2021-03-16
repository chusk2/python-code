def sort_words(s) :
    s = s.split()
    ### lambda s : s.lower() --> anonymous function that takes s as argument
    ### and operates over s
    ### key argument to set the sorting criterium
    s.sort( key = lambda s : s.lower() )
    sorted_s = ' '.join(s)

    return sorted_s