"""
mediumDiscussion Solutions 
Binary Search Tree LCA

Have the function BinarySearchTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements: the first element will be a binary search tree with all unique values in a preorder traversal array, the second and third elements will be two different values, and your goal is to find the lowest common ancestor of these two values. For example: if strArr is ["[10, 5, 1, 7, 40, 50]", "1", "7"] then this tree looks like the following:



For the input above, your program should return 5 because that is the value of the node that is the LCA of the two nodes with values 1 and 7. You can assume the two nodes you are searching for in the tree will exist somewhere in the tree.
Examples
Input: ["[10, 5, 1, 7, 40, 50]", "5", "10"]
Output: 10
Input: ["[3, 2, 1, 12, 4, 5, 13]", "5", "13"]
Output: 12
Tags
binary treesearchingGoogle
"""
strArr = ["[10, 5, 1, 7, 40, 50]", "1", "7"] # 5
strArr = ["[10, 5, 1, 7, 40, 50]", "5", "10"] # Output: 10
strArr = ["[3, 2, 1, 12, 4, 5, 13]", "5", "13"] # Output: 12

# def BinarySearchTreeLCA(strArr):
#     #
#     

# BinarySearchTreeLCA(strArr)

#### holding coderbyte for leetcode problem ####
#### still don't know how to create a BST given a preorder traversal array

#### Leetcode
"""
235. Lowest Common Ancestor of a Binary Search Tree
Medium
Topics
premium lock icon
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
2,295,323/3.2M
Acceptance Rate
70.7%
Topics
Tree
Depth-First Search
Binary Search Tree
Binary Tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# building the tree... (func copird from "DSA construct BT from level ord traversal")
def TreeFromLevelOrdArray (strArr):
    """
    docs here
    """
    from collections import deque
    if not strArr or len(strArr)==0 or strArr[0] == None: return None
    root = TreeNode(strArr[0])
    queue = deque([root])
    pointer = 1
    while queue and pointer< len(strArr):
        node = queue.popleft()
        if pointer<len(strArr) and strArr[pointer] is not None:
            node.left = TreeNode(strArr[pointer])
            queue.append(node.left)
        pointer +=1
        if pointer<len(strArr) and strArr[pointer] is not None: # safeguards when list has odd no. elems
            node.right = TreeNode(strArr[pointer])
            queue.append(node.right)
        pointer +=1

    if root: return root

# root = TreeFromLevelOrdArray(strArr)

root = TreeFromLevelOrdArray([6,2,8,0,4,7,9,None,None,3,5])# , 
p = TreeNode(2)
q = TreeNode(8)
# Output: 6

root = TreeFromLevelOrdArray([6,2,8,0,4,7,9,None,None,3,5])# , 
p = TreeNode(2)
q = TreeNode(4)
# Output: 2

root = TreeFromLevelOrdArray([2,1])# , 
p = TreeNode(2)
q = TreeNode(1)
# Output: 2

# root.right.left.right.val

# my solution first and then neet's solution from yt
# fails at either when the node is itself a descedent or when both p,q are children

# class Solution_my:
#     def lowestCommonAncestor_my(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         count = 0
#         def dfs(root):
#             nonlocal count
#             if root:
#                 dfs(root.left)
#                 if count ==2: return root.left
#                 dfs(root.right)
#                 if count ==2: return root#.right
#                 if root == p or root==q: count +=1
#                 if count ==2: return root
#         return dfs(root)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            x = node.val
            if node.val< p.val and node.val<q.val: return dfs(node.right)
            if node.val> p.val and node.val>q.val: return dfs(node.left)
            if (node.val-p.val) * (node.val-q.val) <=0: # turns out not really necessary
                return node
        return dfs(root)

# print(Solution().lowestCommonAncestor(root,p,q).val)

# practicing 
def lowestCommonAncestor_test(root, p, q):
    if not root:
        return 'None root'
    def dfs(node):
        if node.val == p.val or node.val == q.val or (p.val-node.val)* (q.val-node.val)<=0:
            return node
        elif p.val< node.val and q.val< node.val:
            dfs(node.left)
        else:
            dfs(node.right)
    
    return dfs(root)

print(lowestCommonAncestor_test(root,p,q).val)

(p.val-root.val)* (q.val-root.val)<=-1