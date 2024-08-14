# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
