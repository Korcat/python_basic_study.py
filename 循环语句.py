## 循环语句

#for和while循环

# 1.while循环
#   一般格式：
# while 判断条件(condition)：
#     执行语句(statements)……
#    while循环使用else语句
# 例：
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
#   简单语句：如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
flag = 1
while (flag): print('欢迎访问菜鸟教程!')
print("Good bye!")

# 2.for语句
#   一般格式：
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)
# break语句使用
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
# range函数
for i in range(5):
    print(i)
for i in range(5, 9):
    print(i)

list=[1,2,3,4]
for x in list:
    print(x,end='\n')


