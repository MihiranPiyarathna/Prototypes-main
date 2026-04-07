"""
2. Add Two Numbers
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,905,822/14.3M
Acceptance Rate
48.2%
Topics
"""
# Linked list face vals only
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

# transform a List to a LinkedList
def LinkedList(l2):
    head = ListNode(l2[0])
    current = head
    i=0
    while i< len(l2)-1:
        current.next = ListNode(l2[i+1])
        i +=1
        current = current.next

    return head

l1= LinkedList(l1)
l2= LinkedList(l2)
##
carry = False
dummy = ListNode(99)
tail = dummy

while l1 or l2:
    if not l1:
        # print("l1", l1.val)
        l1 = ListNode(0)

    if not l2:
        # print("l2", l2.val)
        l2 = ListNode(0)

    c = l1.val+l2.val
    l1= l1.next
    l2= l2.next

    if carry:
        c +=1 
    else:
        pass
    # print("c ", c)

    carry = False
    
    if c>=10:
        c= c-10
        carry = True

    tail.next = ListNode(c)
    tail  = tail.next
    # print( "tail", tail.val)

if carry:
    tail.next = ListNode(1)

head = dummy.next
##
while head:
    print(head.val)
    head = head.next
# beats 13.35%

# fastest (from leet)
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "",""
        cur = l1
        while cur:
            num1+=str(cur.val)
            cur=cur.next

        cur = l2
        while cur:
            num2+=str(cur.val)
            cur=cur.next
        
        num3 = int(num1[::-1])+int(num2[::-1])
        num3 = str(num3)[::-1]

        new_head = ListNode(int(num3[0]), None)
        cur = new_head

        for i in range (1, len(num3)):
            cur.next = ListNode(int(num3[i]))
            cur = cur.next
        return new_head
"""