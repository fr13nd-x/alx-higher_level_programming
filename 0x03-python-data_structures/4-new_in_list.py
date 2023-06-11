#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        newlist = my_list.copy()
        newlist[idx] = element
        return newlist
        return my_list
