# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None

        _list = ListNode()
        head = _list

        head1 = list1
        head2 = list2

        while head1 != None and head2 != None:
            val1 = head1.val
            val2 = head2.val
            if val1 < val2:
                _list.val = val1
                head1 = head1.next
            else:
                _list.val = val2
                head2 = head2.next

            if head1 != None or head2 != None:
                _list.next = ListNode()
                _list = _list.next

        if head1 != None:
            _list.val = head1.val
            _list.next = head1.next
        if head2 != None:
            _list.val = head2.val
            _list.next = head2.next

        return head

        

            