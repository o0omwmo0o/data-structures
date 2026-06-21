# 模仿版：二叉树先序遍历

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None
    node = TreeNode(arr[index])
    node.left = build_tree(arr, 2 * index + 1)
    node.right = build_tree(arr, 2 * index + 2)
    return node

def preorder(node):
    if node is None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

arr = [8, 4, 12, 2, 6, 10, 14]
root = build_tree(arr)

print("二叉树先序遍历结果：")
preorder(root)
print()
