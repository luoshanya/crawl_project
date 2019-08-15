__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 7:58'

def heap_sort(lst):
    def sift_down(start, end):
        """最大值调整"""
        root = start
        print('root %d start %d and %d'%(root,start,end))
        while True:
            child = 2 * root + 1
            print("chile index: %d"%child)

            # 终止条件，孩子的索引值超过数组最大长度
            if child > end:
                break
            print('lst child value:%d'%lst[child])

            # 确定最大的孩子节点的索引值
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
                print(child)

            # 孩子节点最大值和根节点交换
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break
    print("===================创建最大堆========================")
    # 创建最大堆
    print(range((len(lst) - 2) // 2,-1,-1))
    for start in range((len(lst) - 2) // 2,-1,-1):
        print('----------Loop start %d'%start)
        sift_down(start,len(lst)-1)
        print(lst)

    print('==============排序过程===========================')
    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        # 首尾交换
        lst[0], lst[end] = lst[end], lst[0]
        # 剩余得重新排序
        sift_down(0,end - 1)
        # print(lst)

    return lst

alist = [22,33,4,4,56,7,78,55,0]
print('==========================')
print(heap_sort(alist))
print('==========================')