"""
26. Remove Duplicates from Sorted Array
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

nums = [0,0,1,1,1,2,2,3,3,4]
_nums =[]
_nums.append(nums[0])
_old = nums[0]
k=1

for e in nums:
    if e!= _old: 
        _nums.append(e) 
        k+=1
        _old = e
nums.clear()
nums[:] = _nums[:]
# print( nums, k)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums or len(nums)==0 : return 0
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)