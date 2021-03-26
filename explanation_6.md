Problem 6: Unsorted Integer Array min & max
**********************************************************
Problem Statement:
=================
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
Bonus Challenge: Is it possible to find the max and min in a single traversal?


Solution:
=========
Initialize 2 variables (min_v,max_v) with the value of arr[0].
Iterate over the array from index 1, and update the values of the 2 variable such that:
max_v = max(max_v, arr[i]) and min_v = min(min_v,arr[i])

Time complexity:
=================
Time complexity is O(n), where n is the array size, since finding the min, max should explore each element in the array.

Space complexity:
=================
Space complexity is O(1), since the 2 variables defined considered as a constant space and independent from the array size.
