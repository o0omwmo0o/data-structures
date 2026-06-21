
# -*- coding: utf-8 -*-
"""
第八次作业（模仿版）
功能：删除二叉搜索树根节点（递归实现）
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def print_tree(root, prefix="", is_left=True):
    if root:
        print(prefix + ("├── " if is_left else "└── ") + str(root.key))
        if root.left or root.right:
            print_tree(root.left, prefix + ("│   " if is_left else "    "), True)
            print_tree(root.right, prefix + ("│   " if is_left else "    "), False)

def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        p = root.right
        while p.left:
            p = p.left
        root.key = p.key
        root.right = delete(root.right, p.key)
    return root

values = [55, 35, 75, 25, 45, 65, 85]
root = None
for v in values:
    root = insert(root, v)

print("删除前BST：")
print_tree(root)

root = delete(root, 55)

print("\n删除根节点55后的BST：")
print_tree(root)

print("\n结论：")
print("删除有两个孩子的节点时，可选择右子树最小值替代，再删除该替代节点。")
