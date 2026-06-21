#=========================作业2-查找元素==================================
from typing import Iterable, Any, Optional

class FindItem:
    """
    在列表中查找指定元素
    核心逻辑：遍历列表，逐个比对元素，返回匹配的索引或元素本身
    """
    def __init__(self, iterable: Iterable[Any]):
        """
        :param iterable: 可迭代对象，要在其中查找元素的列表/可迭代对象
        """
        self.iterable = list(iterable)  # 转换为列表存储，统一操作

    def find_index(self, target: Any) -> int:
        """
        查找指定元素第一次出现的索引位置

        :param target: 要查找的目标元素
        :return: 目标元素的索引
        :raises ValueError: 如果元素不存在于列表中，抛出值异常
        """
        # 遍历列表，逐个比对元素
        for i in range(len(self.iterable)):
            if self.iterable[i] == target:
                return i

        # 若遍历结束仍未找到，抛出异常
        raise ValueError(f"元素 {target!r} 不在列表中！")

    def find_all_indices(self, target: Any) -> list[int]:
        """
        查找指定元素所有出现的索引位置

        :param target: 要查找的目标元素
        :return: 包含所有匹配索引的列表，若无匹配则返回空列表
        """
        # 收集所有匹配位置的索引
        indices = []
        for i in range(len(self.iterable)):
            if self.iterable[i] == target:
                indices.append(i)
        return indices

    def contains(self, target: Any) -> bool:
        """
        判断列表中是否包含指定元素

        :param target: 要查找的目标元素
        :return: 若包含则返回 True，否则返回 False
        """
        # 逐个比对，找到即返回 True
        for item in self.iterable:
            if item == target:
                return True
        return False

# ------------------- 使用示例 -------------------
if __name__ == "__main__":
    # 示例1：查找元素第一次出现的索引
    finder1 = FindItem([10, 20, 30, 20, 40])
    result1 = finder1.find_index(20)
    print("示例1 - 查找元素20的索引：", result1)  # 输出：1

    # 示例2：查找元素所有出现的索引
    finder2 = FindItem(["a", "b", "a", "c", "a"])
    result2 = finder2.find_all_indices("a")
    print("示例2 - 查找元素'a'的所有索引：", result2)  # 输出：[0, 2, 4]

    # 示例3：判断列表是否包含某元素
    finder3 = FindItem([1, 2, 3])
    result3 = finder3.contains(2)
    print("示例3 - 列表是否包含2：", result3)  # 输出：True

    # 示例4：查找不存在的元素（触发异常）
    finder4 = FindItem([1, 2, 3])
    try:
        result4 = finder4.find_index(99)
    except ValueError as e:
        print("示例4 - 查找不存在的元素：", e)  # 输出：元素 99 不在列表中！



#=========================作业3-反转列表==================================
from typing import Iterable, Any

class ReverseList:
    """
    反转列表中元素的顺序
    核心逻辑：使用双指针，从列表两端向中间交换元素
    """
    def __init__(self, iterable: Iterable[Any]):
        """
        :param iterable: 可迭代对象，要反转的列表/可迭代对象
        """
        self.iterable = list(iterable)  # 转换为列表存储，统一操作

    def reverse(self) -> list[Any]:
        """
        反转列表中元素的顺序

        :return: 反转后的新列表
        """
        # 核心逻辑：双指针法，从两端向中间逐个交换
        left = 0
        right = len(self.iterable) - 1

        while left < right:
            # 交换左右指针指向的元素
            self.iterable[left], self.iterable[right] = self.iterable[right], self.iterable[left]
            left += 1
            right -= 1

        return self.iterable

# ------------------- 使用示例 -------------------
if __name__ == "__main__":
    # 示例1：反转奇数个元素的列表
    reverser1 = ReverseList([1, 2, 3, 4, 5])
    result1 = reverser1.reverse()
    print("示例1 - 反转奇数长度列表：", result1)  # 输出：[5, 4, 3, 2, 1]

    # 示例2：反转偶数个元素的列表
    reverser2 = ReverseList(["a", "b", "c", "d"])
    result2 = reverser2.reverse()
    print("示例2 - 反转偶数长度列表：", result2)  # 输出：['d', 'c', 'b', 'a']

    # 示例3：反转单个元素的列表
    reverser3 = ReverseList([100])
    result3 = reverser3.reverse()
    print("示例3 - 反转单元素列表：", result3)  # 输出：[100]

    # 示例4：反转空列表
    reverser4 = ReverseList([])
    result4 = reverser4.reverse()
    print("示例4 - 反转空列表：", result4)  # 输出：[]
