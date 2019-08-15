__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 6:26'

# 冒号排序
def bubble_sort(lists):
    # 获取列表的长度 因为遍历的时候从0开始 所以这里需要减一
    count = len(lists)-1
    # 这个循环代表的是 我们需要算多少次 如果列表数的6 那么第一个对比到最后一个就需要进行5次对比
    # 如果顺序是(,0)就是一个倒序的迭代 那么后面必须加一个数 不然没有输出 -1代表每循环一次减一
    for index in range(count,0,-1):
        print(index)
        # 第一个和第n+1个一次对比
        for sub_index in range(index):
            # 大的元素冒上去
            if lists[sub_index] > lists[sub_index+1]:
                lists[sub_index],lists[sub_index+1] = lists[sub_index+1],lists[sub_index]
    return lists

alist = [10,2,4,3,44,1]
# print(len(alist))
print(bubble_sort(alist))