"""
arr = arr of numbers
find the output from the largest contiguos subarray

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
arr= [1, -2, 0, 3] # 3
arr= [-1, 2, -1, 3] # 4
arr = [1]
arr = [-1,-2]
arr= [3, -1, -1, 4, 3, -1] # 8 from [3, -1, -1, 4, 3]

###############
# kadane's algorithm
###############

# https://coderbyte.com/video/max-subarray-solution # solution from coderbyte
# kadane one to one code from gpt
def maxSubArray_web(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        print(i)
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

print( maxSubArray_web(arr)) # 1 # correct

# coderbyte concept 
def maxSubArray(arr):

        a=0
        b=0
        arrLen=len(arr)
        for i in range (arrLen):
                if sum(arr[a:i+1]) <= arr[i]:
                        a = i
                        b = i+1
                elif sum(arr[a:i+1]) > sum(arr[a:b]):
                        b = i+1
                        
        return sum(arr[a:b])# arr[a:b]

print(maxSubArray(arr))
# fails when all numbers are negative
# this is because I didn't keep track of the global sum