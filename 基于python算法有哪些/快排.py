__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 7:26'

# 快速排列
def quick_sort(lists,left,right):
    # 递归过程中，发现left和right一致时，停止递归，直接返回列表
    if left >= right:
        return lists
    # 定义游标
    low = left
    high = right

    # 去参考标志，最左边的元素
    key = lists[low]
    print(key)
    while low < high:
        # print(lists[high])
        # 从最右侧向左，依次和标志元素对比，如果右侧的元素大于标志元素
        while low < high and lists[high] >= key:
            # 右侧减一
            high -= 1
        # 否则low赋high值 那么因为low比high要大 所以lists[high]需要互换lists[low]
        lists[low] = lists[high]
        print(lists[low])
        # 从最左侧向右，依次和标志元素对比，如果左侧的元素小于标志元素
        while low < high and lists[low] <= key:
            low += 1
        # 否则high赋low值
        lists[high] = lists[low]
        print(lists[high])
    # 最后high赋给low值
    lists[high] = key
    print(lists[high])

    # 处理左侧元素
    quick_sort(lists,left,low-1)
    quick_sort(lists,low + 1, right)
    return lists

alist = [1,33,4,55,6,7,88]
print(quick_sort(alist,0,6))
