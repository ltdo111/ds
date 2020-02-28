## 章节
* 递归
* 链表-天然的递归属性
* 递归运行机制
* 递归算法的调试 
* 更多和链表相关的知识

## 递归简介
### 重要性
```
区分初级程序员和高级程序员的分水岭
```

### 递归定义
```
1.本质上是将一个问题，转化为跟小的同一问题
```
#### 举个栗子🌰
递归求数组和:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/7 下午2:37
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Sum.py
# @Software: PyCharm
"""


class Sum:
    def __init__(self):
        pass

    def sum(self, arr):
        return self._cal_sum(arr, 0)

    def _cal_sum(self, arr, left):
        if left == len(arr):
            return 0
        return arr[left] + self._cal_sum(arr, left + 1)


if __name__ == '__main__':
    arr = [1, 2, 3]

    print(Sum().sum(arr))

```
**递归的核心**
```
1. 找到收敛域 -> 求解最基本问题
2. 让计算机帮你去做->把原问题转化为更小的问题
3. 把编写的递归函数当作被调用的子函数
```

## 链表-天然的递归属性





