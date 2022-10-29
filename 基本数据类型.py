## python基本数据类型

# 1.标准数据类型
"Number,String,List,Tupl(元组)，Set(集合)，Dictionary(字典)"
a, b, c = 1, 2.1, True
print(type(a), type(b), type(c))  # 判断a,b,c的数据类型
# 也可以用isinstance来判断
isinstance(a, int)  # 返回值为True

# 2.删除单个或多个对象
del a, b, c
# 运算
2 / 4  # 除法，得到一个浮点数
2 // 4  # 除法，得到一个整数
17 % 3  # 取余
2 ** 2  # 乘方

# 3.字符串
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST")  # 连接字符串

# 3.list引索规则
list = [1, 2, 3, 4, 5, 6]
print(list[2])  # 输出为三
print(list[1:3])  # 从第二个数开始，到第三个数为止，可以理解为此时的右方框为开区间
print(list[:4])  # 从第四个数开始往前输出
print(list[1:3:2])  # 从第二个元素开始，每隔一个元素输出一个，到第三个元素为止;python里最后一个数字是步长，但matlab里中间一个数字是步长

# 4.Tuple元组
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
tuple = ('abcd', 786, 2.23, 'round')
tinytuple = (123, 'rob')  # 次元组
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# 5.Set集合
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}  # 非空集合
print(sites)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites:
    print('runoob 在集合中')
else:
    print('runoob 不在 集合中')
# set可以进行集合运算
a = set('anflsjfnflsk')
b = set('asfjoisfjs')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

# 6.Dictionary字典
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 7.python数据类型转换
x=36
int(x)
float(x)# 转换为浮点数
str(x) # 转换为字符串

