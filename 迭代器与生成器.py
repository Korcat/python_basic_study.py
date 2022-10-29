## 迭代器与生成器

import sys

list1 = [1, 2, 3, 4, 5]
it = iter(list1)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
