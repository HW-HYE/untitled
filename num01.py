# import random
#
# number = random.randint(0, 100)
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")


# n = 100
#
# sum01 = 0
# counter = 1
# while counter <= n:
#     sum01 = sum01 + counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum01))


# import time

# num = 0
# var = 1
# while var == 1:  # 表达式永远为 true
#     # num = int(input("输入一个数字  :"))
#     # print("你输入的数字是: ", num)
#     time.sleep(2)
#     num += 1
#     print("Good bye!", num)


# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count += 1
# else:
#     print(count, " 大于或等于 5")


# flag = 1
# while flag:
#     print('欢迎访问菜鸟教程!')
# print("Good bye!")


# sites = ["Baidu", "Google", "Runoob", "Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("本次循环数据为： " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# num = 0
# for i in range(100):
#     if i == 88:
#         print("恭喜")
#         break
#     else:
#         num += 1
#         print("还没到规定数字%d" % (num))


# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])


# #  错误
# a = [range(10)]
# print(a)
#
# # 正确
# b = list(range(10))
# print(b)


# for letter in 'Runoob':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
#
# print("Good bye!")


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)


# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# # 计算面积函数
# def area(width, height):
#     return width * height


# def print_welcome(name):
#     print("Welcome", name)
#
#
# print_welcome("Runoob")
# # w = int(input("请输入宽度："))
# # h = int(input("请输入长度："))
# w = float(input("请输入宽度："))
# h = float(input("请输入长度："))
# print("width =", w, " height =", h, " area =", area(w, h))

print("111111")
print("111111")