## python基础语法

print("hello,吴宇欣")
str='123456789'
print(str[0:-2]) #这里的‘-2’表示到倒数第三个数为止
print(str[1:6:1]) #这里的‘1’表示从第二个数开始
print(str * 2)
print(str + '你好，吴宇欣') #‘+’用于连接字符串
print('hello/nworld')
print(r'hello,world') #若字符串里有转义字符，则前面+r转义字符不发生转义

# 合法缩进
if True:
   print('ok')
else:
   print('no')
# 非法缩进
'''
if True:
    print('ok')
else:
  print('no')b=4,c=5;
'''


