# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum.
# Return these two numbers. You can assume that all array elements are in the range [0, 9].
# The number of digits in both the numbers cannot differ by more than 1.
# You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
#
# for e.g. [1, 2, 3, 4, 5]
#
# The expected answer would be [531, 42].
# os such as these when there are more than one possible answers, return any one.

#The first solution depends on the fact: <<You can assume that all array elements are in the range [0, 9]>>.
#So if we create a dictionary holds the frequency of each number from 0 to 9 in O(n).
#Then loop on the numbers from 9 to 0 and form the 2 targeted numbers in loop takes O(9*len(input_list)) which approximately takes O(n).
def rearrange_digits_solution1(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) == 0:
        return [0,0]
    num_dict = {k:0 for k in range(10)}
    for num in input_list:
        num_dict[num] += 1
    output_nums = [0,0]
    last_added = 0
    for i in range(10,0,-1):
        if num_dict[i-1] > 0:
            for j in range(num_dict[i-1]):
                if last_added%2 == 0:
                    output_nums[0] = (output_nums[0]*10)+ (i-1)
                else:
                    output_nums[1] = (output_nums[1]*10)+ (i-1)
                last_added +=1
    return output_nums
#========================================================================================

#Using optimized sorting algorithms like merge sort to sort the array descending in O(n logn) first then loop over it to form the numbers.

def rearrange_digits_solution2(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) == 0:
        return [0,0]
    sorted_array = merge_sort_recursive_descending(input_list)
    output_nums = [0,0]
    last_added = 0
    for num in sorted_array:
        if last_added%2 == 0:
            output_nums[0] = (output_nums[0]*10)+ num
        else:
            output_nums[1] = (output_nums[1]*10)+ num
        last_added +=1
    return output_nums

def merge_sort_recursive_descending(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    mid_index = len(input_list)//2
    list1 = merge_sort_recursive_descending(input_list[0:mid_index])
    list2 = merge_sort_recursive_descending(input_list[mid_index:])
    merged_list = merge_descending(list1, list2)
    return merged_list

def merge_descending(list1, list2):
    merged_list = []
    left = 0
    right = 0
    while left < len(list1) and right < len(list2):
        if list1[left] > list2[right]:
            merged_list.append(list1[left])
            left += 1
        else:
            merged_list.append(list2[right])
            right += 1
    if left < len(list1):
        merged_list.extend(list1[left:])
    else:
        merged_list.extend(list2[right:])
    return merged_list

#========================================================================================
def test_function(test_case):
    print(f"\nArray = {test_case[0]} ")
    solution = test_case[1]
    #try solution 1
    output1 = rearrange_digits_solution1(test_case[0])
    print(f"\tSolution 1 = {output1} ")
    if sum(output1) == sum(solution):
        print("\tPass Solution 1")
    else:
        print("\tFail Solution 1")
    #try solution 2
    output2 = rearrange_digits_solution2(test_case[0])
    print(f"\tSolution 2 = {output2} ")
    if sum(output2) == sum(solution):
        print("\tPass Solution 2")
    else:
        print("\tFail Solution 2")

#========================================================================================

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 9, 9, 9, 9, 9,0], [999, 9990]])
test_function([None, [0,0]])
test_function([[], [0,0]])
test_function([[0,0], [0,0]])
test_function([[7, 1, 6, 2, 5, 3, 4], [7532,641]])
test_function([[6, 1, 5, 2, 4, 3], [631,542]])
test_function([[1,0], [1,0]])
