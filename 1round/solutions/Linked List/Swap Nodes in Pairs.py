# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first = head
        cur = head.next
        others = head.next.next
        # first.next = others
        cur.next = first # process the fist pair, then recrusively process the rest
        first.next = self.swapPairs(others)
        return cur # return to new head
