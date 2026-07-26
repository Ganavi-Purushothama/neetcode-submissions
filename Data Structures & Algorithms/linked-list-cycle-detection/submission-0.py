# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        runner=head

        while runner and runner.next: #safety check to see if sm exists after runner
            curr=curr.next
            runner=runner.next.next

            if curr==runner:
                return True
        return False

        