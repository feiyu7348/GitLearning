# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2022/12/8 19:31
# L = [1,2,3,4,5]
# for i in L:
#     print (i)
#     if (i == 2):
#         L.remove(i)


# GLOBAL_A = 0
#
# def fun_a():
#     return 1, 3
#
# def fun_b():
#     GLOBAL_A, b = fun_a()
#     print (GLOBAL_A, b)
#
# fun_b()
# print (GLOBAL_A)
# MAGIC = 'abc'
#
#
# def check(name):
#     return name[:3] == MAGIC
#
#
# print(check("1234"))
#
#
# def view_file(self, file_path: str) -> None:
#     try:
#         os.system('less -m %s' % file_path)
#     except Exception as e:
#         LOG.debug(e)
#         return
#
# class Test(object):
#     num=10
#
# if __name__ == '__main__':
#     obj1=Test()
#     obj2=Test()
#     obj1.num+=2
#     Test.num+=3
#     print (obj1.num, obj2.num, Test.num)
#
# def FinallyTest():
#     print ('start test---')
#     while True:
#         try:
#             print ("running---")
#             raise IndexError("r")
#         except NameError,e:
#             print ("NameError happen %s",e)
#             break
#         finally:
#             print ("finally executed")
#             break
# FinallyTest()

def check_ipv4(ip_str: str) -> bool:
    items = ip_str.split('.')
    if len(items) != 4:
        return False

    for num in items:
        if 0 <= int(num) <= 255:
            continue
        return False
    return True


print(check_ipv4("1.1.1.1"))


def view_dict(cmd: Dict[str, List[str]] = {}) -> None:
    # 将传入的Dict 按照规范写入文件
    # 然后根据规定格式从文件读取
    self.write_file(cmd)
    return self.read_file()
