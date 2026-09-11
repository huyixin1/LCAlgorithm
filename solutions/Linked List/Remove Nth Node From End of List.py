# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        n_k1 = self.fromEnd(dummy, n+1) # put in virtual head to prevent empty list
        n_k1.next = n_k1.next.next # but the n node next pointer still there
        return dummy.next

    def fromEnd(self, head, n):
        # return the n th node from end
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next # so let p1 and p2 differ by n steps
        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2
