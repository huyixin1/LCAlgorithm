# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if not head: return head
            pre, cur = None, head
            while cur:
                succ =  cur.next
                cur.next = pre
                pre = cur
                cur = succ
            return pre
        slow, fast = head, head
        while fast and fast.next: # we have the second cond cuz fast moves 2 steps
            slow = slow.next
            fast = fast.next.next
        if fast: # if there are odd items in linked list then slow move one more
            slow = slow.next
        
        left, right =head,  reverse(slow) # from the middle
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


        