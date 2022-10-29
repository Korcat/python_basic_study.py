## 集合

# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)

# 1.添加/移除元素
# s.add(x)，s.upate({})
num = {1, 2, 3}
num.add(4)
print(num)
num.update({5, 6})
print(num)
# s.remove(x)/s.discard(x)
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
thisset.remove("Facebook")  # 不存在会发生错误
thisset.discard("Taobao")
thisset.discard("Facebook")  # 不会发生错误

# 2.计算集合元素个数
len(num)

# 3.清空集合
num.clear()
