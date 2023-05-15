from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # The two pointers approach - swaps only value, not entire node
    left_node = head

    for i in range(1, k):
        left_node = left_node.next

    right_node = head
    curr = left_node

    while curr.next:
        curr = curr.next
        right_node = right_node.next

    left_node.val, right_node.val = right_node.val, left_node.val

    return head

    # Naive approach - Swaps entire node rather than just the value
    # curr, prev = head, head
    # find_queue: deque = deque()
    #
    # counter: int = 0
    #
    # if not curr.next:
    #     return head
    #
    # # Get length of list to flip value of K if needed
    # length: int = 0
    # while curr:
    #     length += 1
    #     curr = curr.next
    #
    # if k > length / 2:
    #     k = length - k + 1
    #
    # curr = head
    #
    # while curr:
    #     counter += 1
    #
    #     # Find node 1, then grab its previous, current, and next node
    #     if counter == k:
    #         prev_node1 = prev
    #         node1 = curr
    #         next_node1 = curr.next
    #
    #     # Use the queue to track k+1 distance from the end
    #     find_queue.append(curr)
    #
    #     if len(find_queue) > k + 1:
    #         find_queue.popleft()
    #
    #     prev = curr
    #     curr = curr.next
    #
    # if counter < 3:
    #     node1.next, next_node1.next = None, node1
    #     return next_node1
    #
    # if k == 1:
    #     prev_node2, node2 = find_queue.popleft(), find_queue.popleft()
    #     node1.next, prev_node2.next = None, node1
    #     node2.next = next_node1
    #     return node2
    #
    # # Find node 2's previous, current, and next node
    # prev_node2, node2, next_node2 = find_queue.popleft(), find_queue.popleft(), find_queue.popleft()
    #
    # # Swap previous nodes
    # if prev_node2 != node1:
    #     prev_node2.next = node1
    # prev_node1.next = node2
    #
    # # Swap next nodes
    # if next_node1 != node2:
    #     node2.next = next_node1
    # else:
    #     node2.next = node1
    # node1.next = next_node2
    #
    # return head


head = ListNode(1, ListNode(2))

swapNodes(head, 1)