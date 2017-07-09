# In this kata you will create a function that takes a list of
# non-negative integers and strings and returns a new list with
# the strings filtered out.
# filter_list([1,2,'a','b']) == [1,2]

def filter_list(l):
    list = []
    for item in l:
        if item.isalnum :
            list.append(item)
    
    return list


print(filter_list([1,2,'a','b']))