# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        pos = {value: i for i, value in enumerate(inorder)}
        pre_idx = 0

        def dfs(left_bound, right_bound):
            nonlocal pre_idx

            if left_bound > right_bound:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = pos[root_val]

            root.left = dfs(left_bound, mid - 1)
            root.right = dfs(mid + 1, right_bound)

            return root
        return dfs(0, len(inorder)-1)
        