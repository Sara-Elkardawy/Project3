# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if number is None:
        return -1
    if input_list is None or len(input_list) == 0:
        return -1
    return rotated_binary_search_recursive(input_list, number, 0, len(input_list)-1)

def rotated_binary_search_recursive(input_list, number, start_index, end_index):
    if start_index > end_index or (start_index == end_index and input_list[start_index] != number):
        return -1

    mid_index = ((end_index-start_index)//2) +start_index
    if input_list[mid_index] == number:
        return mid_index

    left_sorted = (input_list[start_index] <= input_list[mid_index-1])
    right_sorted = (input_list[mid_index+1] <= input_list[end_index])
    in_left_range = (input_list[start_index] <= number and number <= input_list[mid_index-1])
    in_range_right = (number >= input_list[mid_index+1] and number <= input_list[end_index])

    if (left_sorted and not in_left_range) and (right_sorted and not in_range_right):
        return -1
    elif (left_sorted and in_left_range) or (right_sorted and not in_range_right) :
        return rotated_binary_search_recursive(input_list, number, start_index, mid_index-1)
    else:
        return rotated_binary_search_recursive(input_list, number, mid_index+1, end_index)


#========================================================================================================
def linear_search(input_list, number):
    if number is None:
        return -1
    if input_list is None or len(input_list) == 0:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
#========================================================================================================
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    answer = rotated_array_search(input_list, number)
    print(f"\n Search for {number} in {input_list}\n *** Answer= {answer}")
    if linear_search(input_list, number) == answer:
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #first
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #last
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[16, 17, 18, 19, 100, 101, 102, 103, 104], 6]) # already sorted
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 15]) #not found
test_function([[23, 17, 82, 90, 100, 101], 15])
test_function([[23, 17, 82, 90, 100, 101], 17])
test_function([[23, 17, 82, 90, 100, 101], 23])
test_function([[23, 17, 82, 90, 100, 101], 102])
test_function([None, 5])
test_function([[1], 5])
test_function([[5], 5])
test_function([[23, 17, 3, 0, -2, -6, -14, 82, 90, 100, 101], -6])
test_function([[6, 7, 8, 1, 2, 3, 4], None])
test_function([[4,5,6,7,0,1,2],0])
test_function([[5,6], 5])
