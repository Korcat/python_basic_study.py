## 字典

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

# 1.创建字典
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
tinydict1 = {'abc': 456}
tinydict2 = {'abc': 123, 98.6: 37}

# 2.访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 3.删除字典元素
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典
