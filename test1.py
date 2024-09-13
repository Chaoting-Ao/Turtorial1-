import random

# 生成1到100之间的随机数
secret_number = random.randint(1, 100)

print("欢迎来到猜数字游戏!")
print("我已经想好了一个1到100之间的数字。")

# 初始化猜测次数
guess_count = 0

while True:
    guess = input("请猜一个数字: ")
    
    # 确保输入是有效的数字
    if not guess.isdigit():
        print("请输入一个有效的数字!")
        continue
    
    guess = int(guess)
    guess_count += 1
    
    if guess < secret_number:
        print("太小了!再猜大一点。")
    elif guess > secret_number:
        print("太大了!再猜小一点。")
    else:
        print(f"恭喜你,猜对了!答案就是 {secret_number}。")
        print(f"你总共猜了 {guess_count} 次。")
        break

print("游戏结束,谢谢参与!")
