# Finding the Square Root of an Integer
# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
#
# For example if the given number is 16, then the answer would be 4.
#
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
#
# The expected time complexity is O(log(n))
#
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print(f"Invalid Input <{number}>: Can not accept negative numbers !!")
        return None
    elif number == 0 or number == 1:
        return number
    else:
        return sqrt_binary_search(number,1,number)

def sqrt_binary_search(number, start, end):
    if (start*start) > number:
        return start-1
    mid = ((end-start)//2)+start
    mid_pow_2 = mid*mid
    if mid_pow_2 == number:
        return mid
    elif mid_pow_2 > number:
        return sqrt_binary_search(number,start, mid-1)
    else:
        return sqrt_binary_search(number,mid+1, end)

#==============================================================================
def test_sqrt():
    print("\n***********************************************")
    for num in range(-1,105,1):
        ans = sqrt(num)
        print(f"The number = {num} , the sqrt = {ans}")
    print("\n")
#==============================================================================
print("\n")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

test_sqrt()
