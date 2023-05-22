#13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

lis = [1,2,3,4,5]
def fn():
    return x**2

res = map(fn,lis)
print(res)

res = [i for i in res if i >10]
print(res)