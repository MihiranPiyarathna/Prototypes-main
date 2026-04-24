"""
https://youtu.be/Z_c4byLrNBU
⭐️ Contents ⭐️
⌨️ (0:00:00) Array
⌨️ (0:03:11) String
⌨️ (0:04:56) Set
⌨️ (0:06:40) Control Flow & Looping
⌨️ (0:07:32) Big O Notation
⌨️ (0:10:02) Hashmap
⌨️ (0:15:54) Hashmap practice problems
⌨️ (0:18:52) Two Pointers
⌨️ (0:22:56) Two Pointers practice problems
⌨️ (0:26:48) Sliding Window
⌨️ (0:31:45) Sliding Window practice problems
⌨️ (0:37:39) Binary Search
⌨️ (0:39:28) Binary Search practice problems
⌨️ (0:48:28) Breadth-First Search (BFS) on Trees
⌨️ (0:50:36) BFS on Graphs
⌨️ (0:52:13) BFS practice problems
⌨️ (0:57:31) Depth-First Search (DFS)
⌨️ (0:59:01) DFS on Graphs
⌨️ (1:00:24) DFS practice problems
⌨️ (1:05:01) Backtracking
⌨️ (1:08:14) Backtracking practice problems
⌨️ (1:10:27) Priority Queue/heap
⌨️ (1:11:36) Priority Queue/heap practice problems
"""

########
# hash map ie. lists, dicts
# two sum

nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    c= (target - nums[i])
    if c in nums[i:]:
        print(i, nums.index(c) )

# can use two pointer meth which is O(n) but tackles all pairs -usually O(n^2)
"""
Example (Two Sum on a sorted list):
If you need to find a pair that sums to 10, you put one pointer at the start and one at the end.

If the sum is too high, move the right pointer left.

If the sum is too low, move the left pointer right.

Why it works: Because the list is sorted, moving a pointer "discards" thousands of pairs that you know won't work, so you don't have to visit them.
"""

########
# sliding window - static
########

# largest sum in subarrays of length k

nums = [1,2,3,7,4,1]
k=3

sums=0
left = 0
right = k
while right<=len(nums):
    sums = max(sum(nums[left:right]), sums)

    left +=1
    right +=1
print(sums)


########
# sliding window - dynamic
########

# longest substring wihtout repeating characters

str_ = "abccabdcabcc" 

def isunq(wnd_):
    if len(wnd) == 1:
        return True
    dict={}
    for e in wnd_:
        dict[e] = dict.get(e, 0) + 1
    if max(dict.values())>1:
        return False
    else:
        return True

cnt = 1
left = 0
right = 1

while right < len(str_):
    wnd = str_[left:right]
    
    if isunq(wnd):
        right +=1
        cnt = max(len(wnd), cnt)
        print(wnd)
    else:
        left +=1
print(cnt)


###########
# O(n) way from the DSA video
# https://youtu.be/Z_c4byLrNBU?t=2172
###########


###########
# BFS - Bredth first Search
###########

# BFS for Trees & BFS for graphs

# Leet problem - 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1985701294/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Node20 = TreeNode(20, TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), Node20)

# test # root = []

### answer in bfs - binary tree ###
from collections import deque # double ended queue # a high performance queue

q = deque([root])
biglist = []

while len(q)>0:
    n = len(q)
    new_level = []

    for _ in range(n):
        node = q.popleft()
        if node: new_level.append(node.val)
        
        if node.left is not None: q.append(node.left)
        if node.right is not None: q.append(node.right)

    biglist.append(new_level)
print(biglist)
# pass beats 100% mem 90.6% 


##########
# 733. Flood Fill - leetcode graph bfs
##########

def get_neighbors (coord, color):
    row,col = coord
    rowlen = len(image)
    collen = len(image[0])
    
    # neighbor patterns
    rowpattern = [-1,0,1,0]
    colpattern = [0,1,0,-1]
    for i in range(len(rowpattern)):
        neighbor_row = row + rowpattern[i]
        neighbor_col = col + colpattern[i]
        if 0 <= neighbor_row <rowlen and 0<= neighbor_col <collen:
            if image[neighbor_row][neighbor_col]==color:
                yield neighbor_row, neighbor_col

image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1 
color = 2

from collections import deque, defaultdict
q = deque([[sr,sc]])
visited=defaultdict(int)
prevclr = image[sr][sc]

# actual BFS part
while len(q)>0:
    node = q.popleft() # remove node
    [sr,sc] = node
    visited[(sr,sc)]=1 # remember node
    
    image[sr][sc] = color # process node
    for k in get_neighbors((sr,sc), prevclr):
        i,j = k
        if visited[(i,j)]<1:
            visited[(i,j)] +=1
            q.append([i,j])
# print(image)
# beats 0.77% in runtime 52% in mem
# this is because DFS is the best approach, I'll learn it now..


##########
# DFS - Depth First Search
##########

# 104. Maximum Depth of Binary Tree
# DFS - for tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right = right

Node20 = TreeNode(20,TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), Node20)

def get_children(root):
    if root is None:
        return None
    delta = ["right","left" ]
    for child in delta:
        yield getattr(root, child)

def dfs (root):
    for child in get_children(root):
        c = child.val if child is not None else None
        print(c)
        dfs(child)

dfs(root)