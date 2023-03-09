# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2022/12/27 10:53

# class Test(object):
#     def __init__(self):
#         print("lock")
#
#     def __del__(self):
#         print("unlock")
#
#
# def fun_a():
#     t = Test()
#     print("in fun_a")
#     raise Exception("error")
#
#
# def fun_b():
#     try:
#         fun_a()
#     except Exception:
#         return False
#     return True
#
#
# def fun_c():
#     fun_b()
#     print("finish")
#
#
# fun_c()

# s = "a"
#
#
# def A(x):
#     def B():
#         print(s)
#
#     if (x == 2):
#         s = "b"
#     B()
#
#
# A(1)
x = 0.1
y = 0.2
if (x + y) == 0.3:
    print("True")
else:
    print("False")