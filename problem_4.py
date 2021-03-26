# Dutch National Flag Problem
# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
#  You're not allowed to use any sorting function that Python provides.
# Note: O(n) does not necessarily mean single-traversal.
# For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

#========================================================================================
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None or len(input_list) == 0 or len(input_list) == 1:
        return input_list
    i = 0
    zero_next_pos = 0
    two_next_pos = len(input_list)-1
    while i <= two_next_pos:
        if input_list[i] == 0:
            input_list[i] = input_list[zero_next_pos]
            input_list[zero_next_pos] = 0
            i += 1
            zero_next_pos += 1
        elif input_list[i] ==1:
            i += 1
        elif input_list[i] ==2:
            input_list[i] = input_list[two_next_pos]
            input_list[two_next_pos] = 2
            two_next_pos -= 1
    return input_list
    pass
#========================================================================================
def test_function(test_case):
    array_copy = []
    if test_case is not None:
        array_copy = test_case.copy()
    print(f"\nThe input array = {test_case}")
    sorted_array = sort_012(test_case)
    print(f"\tThe sorted array {sorted_array}")
    if test_case is None and sorted_array is None:
        print("\tPass")
    elif test_case is None and sorted_array is not None:
        print("\tXXXX Fail")
    elif test_case is not None and sorted_array == sorted(array_copy):
        print("\tPass")
    else:
        print("\tXXXX Fail")
#========================================================================================
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function(None)
test_function([])
test_function([0])
test_function([1])
test_function([2])
test_function([0,1])
test_function([1,0])
test_function([0,2])
test_function([2,0])
test_function([1,2])
test_function([2,1])
test_function([1,2,0])
test_function([2,0,1])
test_function([2,1,0])
test_function([0,0,2,0,0,1,1,0,0,0,0,1])
test_function([2,2,2,2,2,1,1,0,0,0,0,1])
