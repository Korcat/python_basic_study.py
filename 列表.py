## 列表

# 1.在索引中，0是初始位，-1是末位
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])

# 2.列表拼接
list1 = [1, 2, 3, 4, 5]
list1 += [666, 999]
print(list1)

# 3.嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

# 4.列表比较
# 导入operator模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print('operator.eq(a,b):', operator.eq(a, b))
print('operator.eq(c,b):', operator.eq(c, b))
