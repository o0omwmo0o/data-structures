import heapq

class KthLargest:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        elif num > self.heap[0]:
            heapq.heapreplace(self.heap, num)

    def findKthLargest(self):
        if len(self.heap) < self.k:
            return None
        return self.heap[0]

kl = KthLargest(3)

nums = [5, 2, 8, 1, 9, 6]
for x in nums:
    kl.add(x)
    print(f"加入 {x} 后，第3大的元素：{kl.findKthLargest()}")

'''
时间复杂度分析

add(num)
堆插入、替换操作最多执行一次，时间复杂度：O(logk)

findKthLargest()
直接读取堆顶元素，时间复杂度：O(1)

整体：处理 n 个元素，总时间复杂度 O(nlogk)，空间复杂度 O(k)。
'''
