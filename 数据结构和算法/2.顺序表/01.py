"""
python中list和tuple两种类型采用了顺序表的实现技术
1.tuple是不可变类型，即不变顺序表，因此不支持改变其内部结构的任何操作
2.list中的元素可以修改，采用分离式技术实现的动态顺序表
"""

t1 = (1, 2, 3, 4, 5)
print(t1)

# 下面操作不能进行
# t1[2] = 33
# print(t1)

l1 = [1, 2, 3, 4, 5]
print(l1)

l1[2] = 33
print(l1)