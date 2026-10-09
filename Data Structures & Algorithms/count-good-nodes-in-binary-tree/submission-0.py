# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, ma):
            nonlocal count
            
            if not node:
                return

            if node.val >= ma:
                count+=1
                ma = node.val
            
            dfs(node.left,ma)
            dfs(node.right,ma)
            # if node.left:
            #     if(node.left.val>ma):
            #         count+=1
            #     print("node", node.val ,"left", node.left.val, "ma", ma) 
            #     ma = max(ma, node.left.val )
            #     dfs(node.left, ma)
            # if node.right:
            #     if node.right.val>ma:
            #         count+=1
            #     print("node", node.val ,"right", node.right.val, "ma", ma)
            #     ma = max(ma, node.right.val )
            #     dfs(node.right, ma)

        dfs(root, root.val)

        return count

        