from typing import List


class TreeNode:
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


class Traversal:
    @staticmethod
    def preorder(root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        result = []

        stack.append((root, 'left'))
        while stack:
            n, zone = stack.pop()

            if zone == 'left':
                result.append(n.label)
                stack.append((n, 'middle'))
                if n.left_ptr:
                    stack.append((n.left_ptr, 'left'))
            elif zone == 'middle':
                stack.append((n, 'right'))
                if n.right_ptr:
                    stack.append((n.right_ptr, 'left'))
            # else zone == right, just pop which is already done above

        return result


in_put = TreeNode(10)

in_put.left_ptr = TreeNode(34)
in_put.right_ptr = TreeNode(89)
in_put.left_ptr.left_ptr = TreeNode(45)
in_put.left_ptr.right_ptr = TreeNode(50)

T = Traversal()
print(T.preorder(in_put))
