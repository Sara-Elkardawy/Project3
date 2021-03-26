Problem 2: Search in a Rotated Sorted Array:
**********************************************************
Problem Statement:
=================
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


Solution:
=========
Use the recursive binary search to find the target with some modifications.
First we calculate the mid_index, and check if the mid value == target then return the mid_index.
Otherwise we check if the number in the left half or right half by recognizing which side is sorted and check if the number is in the range of the sorted partition. There is also a case in which both partitions are sorted, this happens when the middle value is the min value or max value of the array.
We recurse on the left half if the left half is sorted and the target value in its range OR the right half is sorted and the target value not in its range. Otherwise we check the right partition.

Time complexity:
=================
Every time we cut the half of the input till we find the target value or return -1 if not found.
 So the maximum calling stack = Log(n), and the time complexity in each recursive call is O(1) then:
Then the Time complexity is O(log(n))

Space complexity:
=================
Space complexity = maximum depth of the generated recursion tree  * the space of each function call of recursive algorithm.
Space complexity = O(Log(n)) depth * O(1) space

Space complexity is O(log(n))
