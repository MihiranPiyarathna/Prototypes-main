"""
mediumDiscussion Solutions 
Symmetric Tree

Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, and determine if the tree is symmetric (a mirror image of itself). The array will be implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL nodes on any level of the tree will be represented with a #. For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] then this tree looks like the following:



For the input above, your program should return the string true because the binary tree is symmetric.
Examples
Input: ["4", "3", "4"]
Output: false
Input: ["10", "2", "2", "#", "1", "1", "#"]
Output: true
Tags
arraybinary treesearchingheapGoogleFacebook
"""
# from heapq import heappop, heappush
# from collections import deque
# above needed when traversing a real Tree. not needed in a str tree.

strArr = ["4", "3", "4"] # false
strArr = ["10", "2", "2", "#", "1", "1", "#"] # true

# didn't know technique, found from solutions: https://youtu.be/ywAZyIjRmoo?t=55

def SymmetricTree_theoryfromweb(strArr):

    def is_mirror(left, right, p):
        # if not left and not right: return True
        if left>=n and right>= n: return True
        return strArr[left]== strArr[right] and is_mirror(left+2**p, right+2**(p+1), p+1) and is_mirror(left+1+2**p, right-1+2**(p+1), p+1)

    # how to traverse - power of 2
    strArr = strArr[1:]
    p= 1
    n= len(strArr)
    return is_mirror(0,1,1)


SymmetricTree_theoryfromweb(strArr)
# pass ; only traversal forulae is mine. theory from web 

##########
# coderbyte solution
##########


def SymmetricTree(strArr):

  # code goes here
  start, end = 1, 2
  level = 2
  while end < len(strArr):
    temp = strArr[start:end+1]
    if temp != temp[::-1]: return 'false'
    start = end+1
    level = level*2
    end += level
  return 'true'  
  

# keep this function call here 
print(SymmetricTree(input()))

##########