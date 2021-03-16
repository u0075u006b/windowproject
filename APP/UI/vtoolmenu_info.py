class MENU_INFO():
    __menu_info__ = {
                "数据管理": ["远程数据库","本地数据库","数据文件"],
                "数据查看": ["日线数据","tick数据"],
                "模拟测试": ["算法1", "算法2", "算法3"],
                }

# print(MENU_INFO.__menu_info__)
l1 = [1,2]

l2 = 0

if bool(l1) and bool(l2):
    a = [l1,l2]
    print(a)
elif bool(l1):
    a = [l1,None]
    print(a)
    print(a[1])
else:
    print('all flase')


# print(list(MENU_INFO.__menu_info__.keys())[0])
# print(MENU_INFO.__menu_info__[list(MENU_INFO.__menu_info__.keys())[0]])
# print(MENU_INFO.__menu_info__[MENU_INFO.__menu_info__])
# print(MENU_INFO.__menu_info__[1])
# print(MENU_INFO.__menu_info__[2])

