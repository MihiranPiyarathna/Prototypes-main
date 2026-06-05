"""
This isn't a question from Leetcode or Coderbyte
"""

strArr = [6, 2,8, 0,4,7,9, None,None,3,5]

strArr = [2,1]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    return root

root = TreeFromLevelOrdArray(strArr)

print(root.val)