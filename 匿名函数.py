"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-23
@author:Mr.Zhang
@file:匿名函数.PY
@ide:PyCharm
@time:2018-07-23 14:04:31
"""
#lambda(匿名函数的关键字)：Python中使用匿名lambda创建匿名函数，不能给函数设置函数名，和普通的函数相比，lambda相当于生成的是一个表达式。lambda语法相对简单，可以封装一些简单的逻辑。

#为什么要使用匿名函数:
#1.不需要定义函数名，节省内存中的变量的定义的空间
#2.可以使代码更加简洁。

#正常的使用函数来定义一个数字相加的函数。
def add(x,y):
    return x+y
res=add(10,20)
print(res)

#使用lambda来改造上面的数字相加的函数
#x,y:相当于普通函数的参数，： 分隔符，x+y相当于函数的返回值
res_lambda= lambda x,y:x+y
#通过res_lambda这个变量来执行lambda函数
res1=res_lambda(10,20)
print(res1)

#不添加参数的lambda函数
res2=lambda :print('这是一个没有参数的lambda函数！')
res2()

#lambda加上条件判断
def bijiao(x,y):
    if x>y:
        print('x和y中数字较大的是:%s'%x)
    else:
        print('x和y中数字较大的是%s' %y)

bijiao(2,3)

res3=lambda x,y:print('x和y中数字较大的是:%s'%x) if x>y else print('x和y中数字较大的是%s'%y)
res3(2,3)

#跟lambda函数设置默认参数

def panduan(name='张三'):
    if name=="张三":
        print('姓名是张三')
    else:
        print('姓名不是张三')
panduan()

res4=lambda name='张三':print('姓名是张三') if name=="张三" else print('姓名不是张三')
res4(name='李四')

