# max_v and min_vin a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers.
# The code should run in O(n) time. Do not use Python's inbuilt functions to find min_vand max_v.
#
# Bonus Challenge: Is it possible to find the max_v and min_vin a single traversal?
#
def get_min_max(ints):
    """
    Return a tuple(min, max_v) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints)==0:
        return (None,None)
    min_v= ints[0]
    max_v = ints[0]
    for i in range(1,len(ints)):
        if ints[i] < min_v:
            min_v= ints[i]
        if ints[i] > max_v:
            max_v = ints[i]
    return (min_v,max_v)
#=============================================================================
def test_get_min_max(arr):
    res= get_min_max(arr)
    print(f"\nThe min = {res[0]}, and the max = {res[1]}, in the array = {arr}")
    if arr:
        print ("** Pass" if ((min(arr), max(arr)) == res) else "XX Fail")
#=============================================================================

## Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

test_get_min_max(l)

arr = None
test_get_min_max(arr)

arr = []
test_get_min_max(arr)

arr = [-8]
test_get_min_max(arr)

arr = [23, 17, 82, 90, 100, 101]
test_get_min_max(arr)

arr = [23, 17, 3, 0, -2, -6, -14, 82, 90, 100, 101]
test_get_min_max(arr)

print("")
