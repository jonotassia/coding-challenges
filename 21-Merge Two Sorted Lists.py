class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    # Initialize a current node which is blank. The sorted_list head will point to the second node of this list
    curr = ListNode()
    sorted_head = curr

    # Loop through each list, moving the list with the next smallest element forward by one and linking to curr
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # Add on the final value from whichever list was not exhausted
    curr.next = list1 if list1 else list2

    return sorted_head.next


def mergeTwoListsRec(self, list1: ListNode, list2: ListNode) -> ListNode:
    # Check if either list is blank. If one list is blank, append the remainder of the next list
    if not list1:
        return list2

    if not list2:
        return list1

    # Initialize a current node which is blank. The sorted_list head will point to the second node of this list
    curr = ListNode()

    # Move recursively through each list, moving the list with the next smallest element forward by one and linking to curr
    if list1.val < list2.val:
        curr = list1
        curr.next = self.mergeTwoListsRec(list1.next, list2)
    else:
        curr = list2
        curr.next = self.mergeTwoListsRec(list1, list2.next)

    return curr

if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
