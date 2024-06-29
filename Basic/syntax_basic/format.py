# 字符串格式化
# %d \ %s \ %f 站位 %（value, value2,value3）传值
# {} 来占位，用.format(value,value2,value3) 传值

name = 'Daniel'
age = 31
money = 1.5

print('我是%s来自%d收入%.2f' % (name, age, money))
print('{}是我{}{}'.format(name, age, money))
