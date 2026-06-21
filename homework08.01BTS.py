# -*- coding: utf-8 -*-
"""
模仿版：二叉搜索树作业
"""

############题一##################
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

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

values = [45, 25, 65, 15, 35, 55, 75]
root = None
for value in values:
    root = insert(root, value)

print("二叉搜索树中序遍历结果：")
inorder(root)
print()
