#猜數字遊戲
import random
r = random.randint(1,100)

input('====猜數字遊戲====')


while True:
    gussesnumber = int(input('請輸入1~100的整數:'))
    if gussesnumber == r:
        print('終於猜對了!!恭喜你!!')
        break
    elif gussesnumber > r:
        print('你猜錯了!!你輸入的數字比較大!!')
    else:
        print('你猜錯了!!你輸入的數字比較小!!')