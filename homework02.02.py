"""
集合（Set）操作类
核心特性：所有逻辑纯手动实现，不依赖Python内置集合/列表方法（如in关键字）
功能：手动实现查询、插入（去重）、删除功能
"""

class CustomSet:
    """自定义集合类，纯手动实现查询/插入/删除，无内置方法依赖"""
    def __init__(self):
        """初始化空集合（底层用列表存储，但不使用列表内置查询方法）"""
        self.elements = []

    # 自定义核心工具函数：手动查找元素索引（替代in关键字）
    def _find_index(self, value):
        """
        纯手动循环查找元素位置，替代in关键字
        :param value: 要查找的元素
        :return: 找到返回索引，未找到返回-1
        """
        for i in range(len(self.elements)):
            if self.elements[i] == value:
                return i
        return -1  # 未找到返回-1

    def insert(self, value):
        """
        手动实现插入（自动去重）：先查是否存在，不存在则插入
        不使用in关键字，纯循环判断
        """
        # 调用自定义查找函数，判断是否存在
        if self._find_index(value) == -1:
            self.elements.append(value)

    def contains(self, value):
        """
        手动实现查询：替代in关键字，纯循环判断元素是否存在
        :return: 存在返回True，不存在返回False
        """
        return self._find_index(value) != -1

    def delete(self, value):
        """
        手动实现删除：先查索引，存在则删除，不存在不操作
        不使用列表remove()方法（底层仍用pop，但核心查找逻辑手动）
        """
        index = self._find_index(value)
        if index != -1:
            self.elements.pop(index)  # 仅用pop做删除，查找逻辑完全手动

    def __str__(self):
        """简洁展示集合内容"""
        return str(self.elements)


# ------------------- 实例化+手动输入初始集合（纯手动逻辑） -------------------
if __name__ == "__main__":
    # 1. 实例化空集合
    my_set = CustomSet()

    # 2. 手动输入初始集合元素
    print("===== 手动输入初始集合元素 =====")
    while True:
        input_str = input("请输入初始集合元素（空格分隔，直接回车则为空集合）：")
        if input_str.strip() == "":
            break
        try:
            initial_elements = [int(num) for num in input_str.split()]
            # 调用自定义insert方法（纯手动去重）
            for elem in initial_elements:
                my_set.insert(elem)
            break
        except ValueError:
            print("输入错误！请仅输入数字，用空格分隔。")

    # 3. 输出初始集合（纯手动去重结果）
    print("\n初始集合（手动去重后）：", my_set)
'''
以下可修改
'''
    # 4. 插入新元素（手动去重）
    my_set.insert(20)
    print("插入20后集合：", my_set)
    my_set.insert(20)  # 重复插入，手动去重无效果
    print("重复插入20后集合（无变化）：", my_set)

    # 5. 查询元素（纯手动循环判断）
    print("集合中是否存在20（手动查询）：", my_set.contains(20))
    print("集合中是否存在30（手动查询）：", my_set.contains(30))

    # 6. 删除元素（纯手动查找后删除）
    my_set.delete(20)
    print("删除20后集合：", my_set)
    my_set.delete(30)  # 删除不存在元素，无效果
    print("删除30后集合（无变化）：", my_set)

