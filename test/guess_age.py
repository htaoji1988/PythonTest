age = 18
count = True
while count:

    for i in range(3):
        guess_age = int(input('你猜我的年龄是多大:'))
        if guess_age < age:
            print('猜小了，往大里猜')
        elif guess_age > age:
            print('猜大了，往小里猜')
        else:
            print('恭喜你，猜对了')
            exit()
    else:
        ans = input('错误次数过多，是否继续:Y/n -->:')
        if ans == 'Y' or ans == 'y':
            continue
        elif ans == 'N' or ans == 'n':
            count = False
        else:
            print('输入错误，导致直接退出')
            count = False
