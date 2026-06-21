
class MyHashMap:
    """使用拉链法实现简单哈希表"""

    def __init__(self, capacity=11):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        bucket = self.table[self._index(key)]
        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket[i] = [key, value]
                return
        bucket.append([key, value])

    def search(self, key):
        bucket = self.table[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        bucket = self.table[self._index(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return True
        return False

    def exists(self, key):
        return self.search(key) is not None

    def reset(self):
        for i in range(self.capacity):
            self.table[i] = []

    def __repr__(self):
        text=[]
        for i,data in enumerate(self.table):
            text.append(f'Bucket {i}: {data}')
        return "\n".join(text)


def main():
    h=MyHashMap(7)
    for k,v in [("apple",10),("banana",20),("orange",30),("grape",40)]:
        h.insert(k,v)
    h.insert("apple",15)

    print("当前哈希表：")
    print(h)
    print("\napple =",h.search("apple"))
    print("banana =",h.search("banana"))
    print("peach =",h.search("peach"))

    print("\norange是否存在：",h.exists("orange"))
    print("peach是否存在：",h.exists("peach"))

    print("\n删除orange：",h.remove("orange"))
    print("删除peach：",h.remove("peach"))
    print(h)

    h.reset()
    print("\n清空之后：")
    print(h)

if __name__=="__main__":
    main()
