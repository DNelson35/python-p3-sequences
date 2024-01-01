#!/usr/bin/env python3

def print_fibonacci(length):
    my_arr = []
    i = 0
    j = 1
    while len(my_arr) < length:
        if len(my_arr) > 0:
            my_arr.append(j + i)
            i = my_arr[-2]
            j = my_arr[-1]
        else:
            my_arr.append(i)
    
    print(my_arr)

        

print_fibonacci(9)

# other possible solution
# def print_fibonacci(length):
#    if length == 0:
#        return []
#    elif length == 1:
#        return [0]
   
#    my_arr = [0, 1]
#    while len(my_arr) < length:
#        my_arr.append(sum(my_arr[-2:]))
#    print(my_arr)
