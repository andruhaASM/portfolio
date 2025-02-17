"""
Intuition

my_list = [2, 3, 9, 0, -10, 5].

Assume we want to sort the my_list in ascending order.

The result would be [-10, 0, 2, 3, 5, 9].

How did you do that?
Pick a first element, say my_list[0] = 2

Go through the entire list and compare each element to the my_list[0],
e. g.
smallest_element = my_list[0]
smallest_index = 0
for i, element in eumerate(my_list):
    if element < smallest_element:
        # update smallest_element
        smallest_element = element
        smallest_index = i
return smallest_index

Repeat the same process for every element in my_list, mutating the
initial data by poping the element under position returned by
code above.

Since there are 2 nested loops, one for looping through the my_list
itself and other one for checking the smalles element, the
selection sort algorithm is O(n^2).
"""

def get_smallest_element(data):
    smallest_element = data[0] # you need to keep track of the
    # smallest element found up to the given index.
    # Each time you find a smaller element than the previous one
    # you have to update the index as well.
    smallest_index = 0
    for i, item in enumerate(data):
        if item < smallest_element:
            smallest_element = item
            smallest_index = i
    return smallest_index
    

def selection_sort(data: list):
    if len(data) == 1:
        return data
    if len(data) == 0:
        raise ValueError("Can not order the empty array.")
    ordered_array = []
    for _ in range(len(data)): # Needs to be this way, because the
        # data is mutating on each iteration.
        smallest_item_index = get_smallest_element(data)
        ordered_array.append(data.pop(smallest_item_index)) # data mutation.
    return ordered_array
    
