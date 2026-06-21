
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def create_linked_list(data):
    if not data:
        return None
    head=ListNode(data[0])
    cur=head
    for x in data[1:]:
        cur.next=ListNode(x)
        cur=cur.next
    return head

def print_list(head):
    cur=head
    while cur:
        print(cur.val,end=" -> " if cur.next else "\n")
        cur=cur.next

def delete_node(head,target):
    dummy=ListNode(0)
    dummy.next=head
    prev=dummy
    cur=head
    while cur:
        if cur.val==target:
            prev.next=cur.next
            break
        prev=cur
        cur=cur.next
    return dummy.next

if __name__=="__main__":
    nums=[10,20,30,40,50]
    head=create_linked_list(nums)
    print("原链表：")
    print_list(head)
    value=int(input("请输入要删除的节点值："))
    head=delete_node(head,value)
    print("删除后的链表：")
    print_list(head)
