Problem 1: Finding the Square Root of an Integer analysis:
**********************************************************
Problem Statement:
=================
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))

Solution:
=========
Use the recursive binary search to find the square root.
Calculate the mid^2 then if it is equal to the number return the mid, otherwise if it is greater than the number then search in the left half, else search in the right half.
**The stopping condition:
	if start^2 > Number, this case happened when the last middle is the floor value we search for.
	Such as in case n=27, after some iterations the mid=5 and 25 < 27 so the next iteration with start=6 and end=7 with this invalid range for square_root(27). So we need to return the last mid from previous iteration which is = (start-1)

Time complexity:
=================
Every time we cut the half of the input till we find the square root if it has an integer value or get the floor of it.
 So the maximum calling stack = Log(n), and the time complexity in each recursive call is O(1) then:
The Time complexity is O(log(n))

Space complexity:
=================
Space complexity = maximum depth of the generated recursion tree  * the space of each function call of recursive algorithm.
Space complexity = O(Log(n)) depth * O(1) space

Space complexity is O(log(n))
