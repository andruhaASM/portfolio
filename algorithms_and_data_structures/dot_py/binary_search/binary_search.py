"""Implement the binary search algorithm.
Binary search works only for the ordered lists.

Intuition behind the algorithm:
1. Get the element in the middle of the list.
2. Compare middle element with the element being searched.
If true, return the middle element. Otherwise,
discard one half (check if the element being searched is bigger
or smaller than the middle element).
3. Get the middle element of the other half and compare with the
element being searched. If found, return the central element.
If not, discard one half. Keep going until the last
element in the list.

For example, lets suppose you want to see if number 8
is in the list l = [1, 2, 3, 4, 5 ... 19].
1. Get the element in the middle. The list has 19 elements,
so the index of the element in the middle can be calculated as:
middle = (index_of_the_most_left + (len(l)-1))  // 2 that is 9.

2. Compare middle element with the element being searched:
8 == l[9] False (8 != 10)
8 > 10 - False.
Then discart the right half of the list (numbers from 10 to 19).
8 < 10 - True. Then split the left side in the middle and continue.

3. The left side is l_s = [1, 2, 4...9].
The middle element is len(l_s) // 2 = 5
4. Compare the middle element with the
element being searched l_s[5] == 8 False, because 6 != 8.
8 > 6 - True
8 < 6 - False
Since 8 > 6, discard the left hand side.
The right hand side is r_s = [7, 8, 9]
5. Get the middle element len(r_s) // 2 == 1
6. Compare the middle element with the element being
searched r_s[1] == 8 True.
Element found. Return the value.

If no element found, return None.
"""

def binary_search(
        data: list[int | float],
        item: int | float
) -> tuple[int | float, int]:
    """Search for item in a list of ints or floats.

    Args:
      data: The list of ints or floats to search item in.
      item: The item to be searched.
    Returns:
      A tuple, where the first element is the element to be searched
      and the second element is the index. If the element was not
      found, the function returns None instead of element index, e. g.
      (2, None).
    Raises:
      ValueError if the list is empty.
    """
    left = 0
    right = len(data) - 1

    if right < 0:
        raise ValueError("The list can not be empty!")
        

    if len(data) == 1 and data[0] == item:
        return (data[0], 0,)

    while left <= right:
        middle = (left + right) // 2
        guess = data[middle]
        if guess == item:
            return (guess, middle,)
        elif guess > item:
            right = middle - 1 
        else:
            left = middle + 1
    return (item, None,)
