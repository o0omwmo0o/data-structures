class SortedArrayDeletion:
    """有序数组删除类（遍历版+手动移动元素）
    支持：
    1. 传入初始数字列表并使用冒泡排序排序
    2. 删除元素时手动移动后续元素，不使用内置pop/remove函数
    3. 实时获取/打印有序数组
    """
    def __init__(self, initial_list=None):
        """
        初始化有序数组
        :param initial_list: 可选，初始数字列表（会用冒泡排序排序）
        """
        if initial_list is None:
            self.array = []
        else:
            # 复制列表+冒泡排序初始化
            self.array = self.bubble_sort(initial_list.copy())

    def bubble_sort(self, arr):
        """冒泡排序：将乱序数组转为升序"""
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def find_delete_position(self, value):
        """逐次遍历查找value应删除的位置，若不存在返回-1"""
        for i in range(len(self.array)):
            if self.array[i] == value:
                return i
            if self.array[i] > value:
                return -1  # 数组有序，后面的元素更大，不可能找到了
        return -1

    def delete(self, value):
        """
        手动实现元素移动+删除，不使用内置pop/remove函数
        :param value: 要删除的数字
        :return: 是否删除成功（True/False）
        """
        # 1. 查找删除位置
        delete_pos = self.find_delete_position(value)
        if delete_pos == -1:
            return False  # 元素不存在

        # 2. 手动将删除位置后的元素向前移动一位
        # 从删除位置的下一位开始正序移动，覆盖要删除的元素
        for i in range(delete_pos + 1, len(self.array)):
            self.array[i - 1] = self.array[i]

        # 3. 移除末尾多余的重复元素（因为前面的元素都前移了，末尾重复了）
        # 手动实现pop效果：通过切片去掉最后一个元素
        self.array = self.array[:len(self.array) - 1]

        return True

    def get_array(self):
        """获取当前的有序数组"""
        return self.array

    def __str__(self):
        """打印对象时直接显示有序数组"""
        return str(self.array)


# ------------------- 交互式测试逻辑（可直接运行） -------------------
if __name__ == "__main__":
    print("===== 有序数组删除工具（手动移动元素版） =====")

    # 第一步：输入初始数组
    while True:
        input_str = input("\n请输入初始数字（空格分隔，直接回车则为空数组）：")
        if input_str.strip() == "":
            initial_nums = []
            break
        try:
            initial_nums = [int(num) for num in input_str.split()]
            break
        except ValueError:
            print("输入错误！请仅输入数字，用空格分隔。")

    # 实例化有序数组对象
    sorted_arr = SortedArrayDeletion(initial_list=initial_nums)
    print(f"\n初始数组（已用冒泡排序排序）：{sorted_arr}")
    print(f"初始数组长度：{len(sorted_arr.get_array())}")

    # 第二步：循环删除元素
    print("\n===== 开始删除元素 =====")
    while True:
        del_num_input = input("\n请输入要删除的数字（输入 q 退出）：")
        if del_num_input.lower() == "q":
            print("\n===== 退出程序 =====")
            print(f"最终有序数组：{sorted_arr}")
            print(f"最终数组长度：{len(sorted_arr.get_array())}")
            break

        try:
            del_num = int(del_num_input)
            success = sorted_arr.delete(del_num)
            if success:
                print(f"删除 {del_num} 后，有序数组：{sorted_arr}")
            else:
                print(f"数组中不存在 {del_num}，未进行删除操作。")
            print(f"当前数组长度：{len(sorted_arr.get_array())}")
        except ValueError:
            print("输入错误！请输入有效的整数，或输入 q 退出。")
