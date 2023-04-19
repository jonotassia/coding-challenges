# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        def dfs(dir: int, curr: TreeNode, zz_length: int):
            zz_length += 1

            # Check left side of parent
            if dir < 0:
                # Get length of left chain, adding zz_length since it is an ongoing chain
                zz_left = dfs(1, curr.right, zz_length) if curr.right else 0
                # Get length of new right chain
                zz_right = dfs(-1, curr.left, 0) if curr.left else 0

            # Check right side
            else:
                # As above
                zz_right = dfs(-1, curr.left, zz_length) if curr.left else 0
                zz_left = dfs(1, curr.right, 0) if curr.right else 0

            # return either previous longest chain or the new longest chain
            return max(zz_left, zz_right, zz_length)

        # Check for the longest chain on either left or right
        zz_left = dfs(-1, root.left, 0) if root.left else 0
        zz_right = dfs(1, root.right, 0) if root.right else 0

        # Return longest chain
        return max(zz_left, zz_right)