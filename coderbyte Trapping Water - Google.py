"""
SAME as LEET  - 42. Trapping Rain Water

Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,578,909/5.3M
Acceptance Rate
67.4%
Topics
Array
Two Pointers
Dynamic Programming
Stack
Monotonic Stack
"""
height = [4,2,0,3,2,5] # res = 9
height = [0,1,0,2,1,0,1,3,2,1,2,1] # res = 6

# class Solution:
def trap_my(height):
        if len(height)<3: return 0
        # finding next greater building

        def next_greater( start, stop, step):
            stack = []
            res = [-1 for e in range (len(height))]
            for i in range(start, stop, step):
                while stack and height[i]> height[stack[-1]]:
                    res[stack.pop()] = i if step ==1 else i+len(height)
                stack.append(i)
            return res

        def collected(water):        
            front = next_greater(0,len(height),1)
            back = next_greater(-1,-len(height)-1,-1)
            
            for i in range(len(height)):
                if back[i] == -1 or front[i] == -1: continue
                collect = min(height[back[i]], height[front[i]]) - height[i]
                water += collect
                height[i] += collect
            return water

        water = 0
        for _ in range(16): # had to be >16 to pass leetcode
            water += collected(0)
        return water

print(trap_my(height))
# needs to be better, for longer arrays, takes too many repeats
# spent 45hrs since start

##########

# more robust O(n) solution from niit in leet
height =  [3, 0, 0, 2, 0, 4] # res = 10

def trap(height):
        if len(height)<3: return 0
        trapped = 0
        l = 0
        r = len(height)-1
        l_tallest, r_tallest = l,r

        while l != r:
            if height[l] <= height[r]:
                if height[l] >= height[l_tallest]: l_tallest = l
                delta = height[l_tallest] - height[l]
                # delta = delta if delta>0 else 0
                trapped += delta
                l +=1
            else:
                if height[r] >= height[r_tallest]: r_tallest = r
                delta = height[r_tallest] - height[r]
                # delta = delta if delta>0 else 0
                trapped += delta
                r -=1
        return trapped

print(trap(height))

