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


strArr = ["4", "3", "4"] # false
strArr = ["10", "2", "2", "#", "1", "1", "#"] # true

class Treenode:
    def __init__(self, left = None, right = None, val = '0'):
        self.left = left
        self.right = right
        val = val

# build the testcase
left = Treenode('#','1','2')
right = Treenode('#','1','2')
root = Treenode(left,right,'10')

# solution for a proper Tree class

def SymmetricTree(root):
    from collections import deque
    
    def isSymt(node):
        if not node or node.left or node.right or node.left.val != node.right.val:
            return False
        else:
            return True

    # bfs for traversal
    queue = deque()
    queue.append(root)
    while queue:
        if not isSymt(queue.popleft()): return False
    return True

SymmetricTree(root)
# fails since isSymt return false when met with a None