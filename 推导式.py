## 推导式

# 1.列表list推导式
# 格式：
# [表达式 for 变量 in 列表]
# [out_exp_res for out_exp in input_list]
# 或者
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [na.upper() for na in names if len(na)>3] #upper表示大写
print(new_names)
number = [i for i in range(30) if i % 3 == 0]
print(number)

# 2.字典推导式
# 格式：
# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }
# 使用字符串创建字典
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)
# 使用数字创建字典
numdict={x:x**2 for x in (4,5,6)} #以三个数字为健，三个数字平方的值为值创建字典
print(numdict)

# 3.集合推导式
# 格式：
# { expression for item in Sequence }
# 或
# { expression for item in Sequence if conditional }
strset = {x for x in 'afjvnnavaveo' if x not in 'abc'}
print(str)
numset = {y ** 2 for y in (1, 2, 3)}
print(numset)
