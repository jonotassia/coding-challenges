# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr_node: ListNode = head
        next_node: ListNode = head.next

        # Set head's next node to null
        curr_node.next = None

        while next_node:
            temp = next_node.next
            next_node.next = curr_node

            curr_node = next_node
            next_node = temp

        return curr_node