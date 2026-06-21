"""
链表节点删除示例
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = self.head
        cur = self.head.next

        while cur:
            if cur.data == value:
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next

        return False

    def display(self):
        cur = self.head
        values = []
        while cur:
            values.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(values) if values else "空链表")


def main():
    lst = LinkedList()

    for x in [10, 20, 30, 40, 50]:
        lst.append(x)

    print("删除前：")
    lst.display()

    lst.delete(30)

    print("删除30后：")
    lst.display()

    print("删除100：", lst.delete(100))


if __name__ == "__main__":
    main()
