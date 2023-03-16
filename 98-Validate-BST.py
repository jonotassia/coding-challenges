from functools import cache

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My solution
from functools import cache

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        if root.left:
            if self.min_value(root.left) >= root.val:
                return False
            elif self.max_value(root.left) >= root.val:
                return False
            elif not self.isValidBST(root.left):
                return False

        if root.right:
            if self.max_value(root.right) <= root.val:
                return False
            elif self.min_value(root.right) <= root.val:
                return False
            elif not self.isValidBST(root.right):
                return False

        return True

    @cache
    def max_value(self, root) -> int:
        if not root.right or root.val > root.right.val:
            return root.val

        return self.max_value(root.right)

    @cache
    def min_value(self, root) -> int:
        if not root.left or root.val < root.left.val:
            return root.val

        return self.min_value(root.left)

# Better solution
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#
#         def validate(node, low=-math.inf, high=math.inf):
#             # Empty trees are valid BSTs.
#             if not node:
#                 return True
#             # The current node's value must be between low and high.
#             if node.val <= low or node.val >= high:
#                 return False
#
#             # The left and right subtree must also be valid.
#             return (validate(node.right, node.val, high) and
#                    validate(node.left, low, node.val))
#
#         return validate(root)
