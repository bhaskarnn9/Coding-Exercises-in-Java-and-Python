from os import system
from anytree.exporter import DotExporter
from anytree import Node


class Traversal:
    @staticmethod
    def preorder(root):
        if root is None:
            return []
        output = []
        stack = [root]  # follows LIFO

        while stack:
            node = stack.pop()  # pick up last-in element
            output.append(node.name)

            if node.right_ptr:
                stack.append(node.right_ptr)

            if node.left_ptr:
                stack.append(node.left_ptr)

        return output


root = Node(10)

level_1_child_left = Node(34, parent=root)
level_1_child_right = Node(89, parent=root)
level_2_child_left = Node(77, parent=level_1_child_left)
level_2_child_right = Node(96, parent=level_1_child_left)
level_3_child_left = Node(99, parent=level_2_child_right)
level_3_child_right = Node(100, parent=level_2_child_right)

DotExporter(root).to_picture("ceo.png")
system("open ceo.png")


# T = Traversal()
# print(T.preorder(nod))
