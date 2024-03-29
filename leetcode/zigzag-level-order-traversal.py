# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        result=[]
        if(root):
            queue.append(root)
        while(queue):
            size=len(queue)
            level=[]
            
            for i in range(size):
                node=queue.pop(0)

                level.append(node.val)
                

                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)

            if(len(result)%2!=0):        
                level.reverse()
            result.append(level)
            
        return result