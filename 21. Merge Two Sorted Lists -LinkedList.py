"""
21. Merge Two Sorted Lists
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ## create linkedlist1
        dummy = ListNode(0)
        tail = dummy
        for i in list1:
            tail.next = ListNode(i)
            tail = tail.next
        list1 = dummy.next
        
        ## create linkedlist2
        dummy = ListNode(0)
        tail = dummy
        for i in list2:
            tail.next = ListNode(i)
            tail = tail.next
        list2 = dummy.next
        
        ## result
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            l1,l2 = list1.val, list2.val
            tail.next = ListNode(min(l1,l2) )
            tail = tail.next
            if l1<l2:
                list1 = list1.next
            else:
                list2 = list2.next
        tail.next = list1 if list1 is not None else list2


        head = dummy.next
        while head:
            print(head.val)
            head = head.next


Solution().mergeTwoLists(list1,list2) # beats 100% 0ms for 209 testcases