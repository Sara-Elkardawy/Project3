Problem 3: Rearrange Array Elements:
**********************************************************
Problem Statement:
=================
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

#=======================================================================================
Solution 1: Using dictionary:
=============================
1. First create a dictionary which contains the frequencies of the numbers [0:9] in the array.
2. Given the assumption that all the array elements are in the range [0, 9], so loop over numbers in a descending order from 9 to 0 and get its frequency from the dictionary to create the output numbers.

Solution 1 Time complexity:
============================
1. The first step of creating the dictionary takes O(n), where n is the array size, by iterating over the array and increase the count of the number.
2. The second step outer loop repeats 10 times so it takes O(c), where c is a constant. But the inner loop takes order O(m1+m2+m3+....+m9) when mi refers to the count of each digit, and sum(Mi) = n. So the overall second step time complexity is O(c*n) ~= O(n)

Then the Time complexity is O(2n) ~= O(n)

Solution 1 Space complexity:
============================
Since this solution uses an extra data structure: dictionary.
Space complexity of a dictionary = O(2 * n ) , where n is the array size and 2 because we save both the number and its count.
But in this problem the dictionary size is 10 entries only so the space complexity is O(c) ~= O(1)
#=======================================================================================
#=======================================================================================
Solution 2: Using MergeSort:
=============================
1. First, sort the array in descending order using the merge sort algorithm. This step takes O(n Logn) time complexity.
2. Second, Loop over the sorted array and each time append the arr[i] to the alternating number. This step takes O(n).

Solution 2 Time complexity:
============================
Time complexity is O(n Log n) + O(n) = O(n+ nlogn) ~= O(nlogn)

Solution 2 Space complexity:
============================
Space complexity = maximum depth of the generated recursion tree  * the space of each function call of recursive algorithm.
Since each time we divide the array by 2, then the recursion depth  = Log(n). And each time we merge 2 arrays which scan (n) items, then the merge step takes O(n) space.
Assuming each recursive call releases the space after execution.
So the overall space complexity = O(Log(n)) depth * O(n) space
                               ~= O(n log n)
