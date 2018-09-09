"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-23
@author:Mr.Zhang
@file:面试中经常遇到的一个大坑.PY
@ide:PyCharm
@time:2018-07-23 11:14:10
"""
def keng(i,result=[]):
    #id():显示对象的内存地址
    #一个对象对应的内存地址是唯一的。
    print('没添加数据之前的列表的内存地址是：%s'%id(result))
    for x in range(i):
        result.append(x*x)
    print('添加完数据之后的列表的内存地址是:%s'%id(result))
    return result

res=keng(3)
print(res)
res1=keng(3)
print(res1)
res2=keng(3,[1,2,3])
print(res2)

