# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create a deque which consists of tuples, with the node at index 1 and the index in the tree in index 2
        node_list = deque([(root, 1)])
        max_width: int = 1

        while node_list:
            # Each time the loop restarts, calculate the size of the new level (if all nodes in level are not the same)
            if node_list[0][1] != node_list[-1][1]:
                max_width = max(max_width, 1 + node_list[-1][1] - node_list[0][-1])

            # Loop through all children on the next level.
            # Since we are using the value of their indices, we do not need to account for null values
            for i in range(len(node_list)):
                node, index = node_list.popleft()

                if node.left:
                    # The left nodes will always be 2 times the current index
                    node_list.append((node.left, 2 * index))

                if node.right:
                    # The left nodes will always be 2 times the current index + 1
                    node_list.append((node.right, 2 * index + 1))

        return max_width

"""
Valuable lessons learned: 
- When doing BFS, it is generally more efficient to use a loop with a queue, though it can be done with recursion
- In order to account for the null values in between two nodes without miss representing outer nulls, we append a tuple 
  indicating the index and the node to the queue rather than just the node itself
  - This is possible because we know that a binary tree has 2^n nodes, where n is depth
  - As such, the value of a node's children will always be 2 times their index + or - one depending on left or right
"""