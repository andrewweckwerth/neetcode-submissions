# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        # visisted = set([root])
        ret = []
        while(queue):

            level_size = len(queue)
            ret.append(queue[-1].val)
            for i in range(level_size):
                node = queue.popleft()
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)

        return ret

        #very easy problem: literally just a breadth first search where you take the rightmost element at every level (queue[-1].val)
        #note for binary search there there are no cycles, so you don't need to even track visited



        