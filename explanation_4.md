Problem 4: Dutch National Flag Problem:
**********************************************************
Problem Statement:
=================
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Solution:
=========
Traverse the array with 2 pointers, one for the zero next position and the other for the two next position.
While traversing the array, there are 3 cases:
  1) Case 1: when arr[i]=0, then we need to put a zero value on the <zero_next_pos_index> after saving the value at <zero_next_pos_index> position in the arr[i]. Then advance both the <zero_next_pos_index> and the iterator.
   We are sure that the gap values between arr[zero_next_pos] and arr[i] are all equal to 1 if there are any 1's in the array otherwise the iterator will always equal to zero_next_pos_index.
   2) Case 2: when arr[i] = 1, just advance the iterator.
   3) Case 3: when arr[i] = 2, first we save the value in the <two_next_pos_index> to the iterator position, then put 2 on the <two_next_pos_index>, then decrease <two_next_pos_index> by 1.

Time complexity:
=================
Since all the algorithm takes is a single traversal, then the time complexity is O(n), where n is the array size.

Space complexity:
=================
Space complexity is O(1), because we sort in place.
