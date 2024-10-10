#2024年度秋学期＿金曜日3限社会情報実践02
#FizzBuzzプログラム
#3の倍数の時はFizz、5の倍数の時はBuzz、両方の時はFizz Buzzを出力
print("整数を入力")
n = int(input())
for s in range(n):
    if(s%3 == 0 | s%5 == 0):
        print(s,"Fizz Buzz")
    elif(s%5 == 0):
        print(s,"Buzz")
    elif(s%5 == 0):
        print(s,"Buzz")
    else:
        print(s)