#猜數字遊戲
import random

input('====猜數字遊戲====')

r = random.randint(1,100)
count = 0
while True:
    count += 1  # count = count + 1
    num = int(input('請輸入1~100的整數:'))
    if num == r:
        print('終於猜對了!!恭喜你!!')
        print('這是你猜的第',count,'次')
        break
    elif num > r:
        print('你猜錯了!!你輸入的數字比較大!!')
    elif num < r:
        print('你猜錯了!!你輸入的數字比較小!!')
    print('這是你猜的第',count,'次')