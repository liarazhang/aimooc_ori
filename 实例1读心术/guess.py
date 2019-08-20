import random
import getopt
import sys


def human_guess():
    # 从 0 - 1000 中，产生一个随机数
    num = random.randint(0,1000)
    i = 0
    while 1:
        # 异常处理 - 输入非int型数据的时候
        try:
            # guess 接收 - 从键盘输入的数字的值
            guess = int(input('请输入数字 0~1000:'))

        except ValueError:
            print('请输入正确的数字 0~1000')
            continue
        i += 1
        # 如果 输入的猜测的数，比随机产生是随机数 num 大
        if guess > num:

            # 提示 猜大了
            print("猜大了:",guess)

        elif guess < num:
            print("猜小了:",guess)

        else:
            print("你猜对了！共猜了",i,'次')
            sys.exit(0)


def computer_guess():
    print('请在心里想一个0~1000范围内的数字')
    small = 0
    big = 1000
    guess = 500
    i = 0
    while 1:
        guess = int((big+small)/2)
        i += 1
        print('是这个数吗：'+str(guess)+'(B:大了,S:小了,C:正确)')
        char = input()
        if char == 'B':
            big = guess
        elif char == 'S':
            small = guess
        elif char == 'C':
            print('共猜了{0}次，得到正确结果{1}'.format(i,guess))
            sys.exit(0)
        else:
            print('请正确输入回答：(B:大了,S:小了,C:正确)')


def main():
    who_guess = input('请决定谁来猜数(C:电脑,H:玩家)：')
    if who_guess in 'Hh':
        human_guess()
    elif who_guess in 'Cc':
        computer_guess()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)