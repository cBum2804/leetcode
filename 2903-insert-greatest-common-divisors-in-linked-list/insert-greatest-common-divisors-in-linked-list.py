# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head

        while curr:
            GCD = math.gcd(curr.val, prev.val)
            gNode = ListNode(GCD)
            prev.next = gNode
            gNode.next = curr
            prev = curr
            curr = curr.next
            
        return head