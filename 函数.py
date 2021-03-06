"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-23
@author:Mr.Zhang
@file:函数.PY
@ide:PyCharm
@time:2018-07-23 09:05:17
"""
#函数：为什么使用函数？因为没有函数的编程只是在单纯的写代码逻辑，如果想重用代码逻辑，只能够copy一份代码。但是一旦使用函数，就可以将一些相同的代码逻辑封装起来，这样可以提高代码的重复使用率，提升开发效率。

#第一步：声明一个函数，在函数里面写逻辑代码
#第二步：调用函数，执行编写的逻辑代码

# print('今天是周一')
# print('明天是周二')
# print('后天是周三')
#
# print('今天是周一')
# print('明天是周二')
# print('后天是周三')
#
# print('今天是周一')
# print('明天是周二')
# print('后天是周三')


#怎么声明一个函数？
#def 声明函数的关键字，shuchu,函数名(可以自定义的)，():用于定义函数的参数，如果没有内容就表示该函数没有参数。：下面的东西，要封装的代码逻辑。

#1.声明一个无返回值，无参数的函数
def shuchu():
    print('今天是周一')
    print('明天是周二')
    print('后天是周三')
#调用函数，函数名+括号
shuchu()
shuchu()
shuchu()

#2.声明一个有返回值，无参数的函数
#一个函数为什么要有返回值：因为一个函数想要最终的执行结果，后面的程序才能根据这个执行结果进行其他的操作。
def cheng():
    c = 10
    d = 20
    e = c*d
    return e
res=cheng()
print(res)
f = res * 10
print(f)

#3.声明一个无返回值，有参数的函数

#a,b叫做形式参数，简称形参
def chufa(a,b):
    c = a/b
    print(c)

#10,2.5称之为实际参数，简称实参。、实参想当于给a,b这两个形参赋值，a=10，b=2.5。
chufa(10,2.5)
chufa(10,4)

#4.有返回值，有参数的函数
def jian(a,b):
    c = a-b
    return c
res=jian(8,5)
print(res)
res1=res+10
print(res1)

#return关键字的作用。
#1.用于返回函数的执行结果。
#2.用于结束当前代码的执行。使用return关键结束代码执行的时候，return必须位于函数内部。区别于break。
def test():
    for x in range(1,11):
        if x==4:
            return
        else:
            print('======',x)

test()

def func2():
    for i in range(1,11):
        if i % 2 == 0:
            break
        #到第一个符合条件的情况下就停止。不输出符合条件的语句，并停止。
        print(i)
func2()






