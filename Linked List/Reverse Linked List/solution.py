# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        next = head.next
        head.next = None
        prev = head
        head = next

        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

          