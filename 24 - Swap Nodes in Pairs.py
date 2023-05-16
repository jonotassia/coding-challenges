from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    prev = ListNode(0, head)
    curr = prev
    next_node = curr.next

    counter = 0

    while next_node.next:
        curr = next_node
        next_node = next_node.next

        if counter % 2 == 0:
            prev.next, next_node.next, curr.next = next_node, curr, next_node.next

            if counter == 0:
                head = next_node

            curr, next_node = next_node, curr

        prev = curr

        counter += 1

    return head


head = ListNode(1, ListNode(2, ListNode(3)))

swapPairs(head)
