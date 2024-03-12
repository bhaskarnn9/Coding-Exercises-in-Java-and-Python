# import anytree
# from anytree import Node
# from anytree.exporter import DotExporter
# from os import system
#
#
# class TreeNode:
#     def __init__(self, node):
#         self.label = node
#         self.left = None
#         self.right = None
#
#
# class AnyTree:  # nlr
#     def tree_traversal_inorder(self, in_put: TreeNode):
#         output = []
#         stack = [in_put]
#         while stack:
#             node = stack.pop()
#             result = self.helper(in_put)
#             output.append(result)
#             return output
#
#     @staticmethod
#     def helper(in_put: TreeNode):
#         if in_put is not None:
#             if in_put.left:
#                 return in_put.label
#             if in_put.right:
#                 return in_put.right
#
#
# root = TreeNode(10)
# child_1 = root.left(5)
# child_2 = root.right(15)
# child_1_1 = child_1.left(4)
# child_1_2 = child_1.right(11)
#
# a = AnyTree()
# a.tree_traversal_inorder(root)


class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

n = Node()
# n.PrintTree(root)
print(root.PrintTree(root))