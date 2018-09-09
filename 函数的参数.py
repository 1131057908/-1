"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-23
@author:Mr.Zhang
@file:函数的参数.PY
@ide:PyCharm
@time:2018-07-23 09:45:47
"""
#1.必备参数(位置参数):实参和形参的数量上必须要保持一致。
def sum(a,b):
    c = a+b
    print(c)
sum(1,2)

#2.命名关键字参数：通过定义关键字也获取实参的值，与形参的顺序无关。
def show(name,age):
    print('姓名是：%s-年龄是：%s'%(name,age))
show(age='20',name='张三')

#3.默认参数
#默认参数的使用场景:数据库连接，地址和端口号可以设置默认。账号密码登陆。
#使用默认参数的时候，如果给形参传递了实参，则形参会接收实参的值。如果没有给这个形参传递实参，则形参会采用默认值。
def show_one(user='zhangsan',password='123456'):
    print('账号是:%s'%user)
    print('密码是:%s'%password)

show_one()
show_one('lisi','678910')


#4：可变参数(不定长参数)，形参的数据会根据实参的数量的变化而变化。
#*args:接收N个位置参数，并且会把位置参数转换成元组的形式。
def show_two(*args):
    print(type(args))
    print(args)

show_two(1)
show_two(1,2,3)
show_two(1,2)
show_two(4,5,6,7,8)

#5：关键字参数
#**kwargs：把N个关键字参数，转换成了字典。
def show_three(**kwargs):
    print(type(kwargs))
    print(kwargs)
show_three(name='zhangsan',age='20',sex='男')



#尝试写一个函数：把以上所有参数填写进去
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。参数定的顺序一般是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def show_all(name,age=20,*args,mother,**kwargs):
    print('=====',name)
    print('=====',age)
    print('=====',args)
    print('=====',mother)
    print('=====',kwargs)
show_all('张三',34,*(10,20),mother='马化腾',**{'sex':'女','father':'马云'})


