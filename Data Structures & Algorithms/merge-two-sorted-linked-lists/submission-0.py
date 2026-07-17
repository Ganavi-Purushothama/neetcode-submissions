# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Fake starting node.
        # Makes building the answer much easier.
        dummy = ListNode()

        # Tail always points to the LAST node
        # in our new merged list.
        tail = dummy

        # Keep going until one list becomes empty
        while list1 and list2:

            # If list1's value is smaller (or equal),
            # attach that node next.
            if list1.val <= list2.val:

                # Connect this node to our answer
                tail.next = list1

                # Move list1 forward
                # (We've already used this node.)
                list1 = list1.next

            else:

                # list2 is smaller
                # Attach it instead.
                tail.next = list2

                # Move list2 forward
                list2 = list2.next

            # Move tail to the node we just attached.
            # Tail should always stay at the END.
            tail = tail.next

        # One list is finished.
        # Attach whatever remains from the other list.

        if list1:
            tail.next = list1

        else:
            tail.next = list2

        # dummy is fake.
        # Actual answer starts after it.
        return dummy.next