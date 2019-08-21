
import sys


# sys.path.append('C:\\Users\\赵望博\\Desktop\\python编程学习\\python\\第二阶段\\第十章\\a')
# print(sys.path)
#
#
# import time #优先导入内置模块， 重名无法导入自定义的模块
#
# from b import x1
# from spam import *
# print(money)
# change()

# import torch
# output = torch.rand(163200, 4)
# print(output.shape)
# a = output.reshape(1, -1, 4)
# print(a.shape)
#

# a, b = output.topk(2, dim=1, sorted=True)
# print(a)
# print(b)
# def foo(x, y, z, *args):
#     return 1
#     # print(x, y, z)
    # print(*args)
#     # print(args)
# foo(1, 2, 3, 4, 5, 6, 7)
# #
# # def foo(x, y, z, *args):
# #     print(x, y, z)
# #     print(args)
#
# foo(1, 2, 3, *[4, 5, 6, 7, 8])
# #
# def bar(x, y, z, **kargws):
#     print(x, y, z)
#     print(kargws)


# bar(1, 2, 3, **{'a': 1, 'b': 2})
#
# # def auth(name, pwd, **kwargs):
# #     print(name)
# #     print(pwd)
# #     print(kwargs)
#
# auth(name='Albert', pwd='123', group='group1')

import numpy as np
A = np.arange(16)
print(A)
print(A[: : -1])