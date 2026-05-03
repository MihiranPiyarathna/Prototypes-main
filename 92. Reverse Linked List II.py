"""
92. Reverse Linked List II
Medium
Topics
premium lock icon
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    def printNode(self):
        import copy
        from copy import deepcopy
        Node = copy.deepcopy(self)
        while Node:
            print(Node.val)
            Node = Node.next

# del ListNode
# del Solution

li = [1,2,3,4,5]
dummy = ListNode()
tail = dummy
for val in li:
    tail.next = ListNode(val)
    tail = tail.next
head = dummy.next

head.printNode()

class Solution:
    def reverse(self, head):
        back = None
        curr = head
        while curr:
            front = curr.next if curr.next else None
            print(back, curr.val, front)
            curr.next = back
            back, curr = curr, front
        back.printNode()
    def reverseBetween(self, head, left: int, right: int):
        position = 1
        while head:
            print(position, head.val)
            if position< left: lastFNode = head 
            while left< position <=right:
                head_prime, curr = head, head
                lastFNode.next = head_prime
                front = curr.next
                curr.next = prev
                prev, curr = curr, front
                tail_prime.next = front
                position +=1
            tail_prime, prev = head, head
            head = head.next
            position +=1

Solution().reverseBetween(head,2,4)


# Solution().reverseBetween()
# left = 2
# right = 4