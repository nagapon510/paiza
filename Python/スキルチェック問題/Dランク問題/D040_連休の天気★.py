# あなたは7日間の連休をもらいましたが、降水確率が 30% 以下ならば外に出掛ける事に決めました。
# 7日間の降水確率(%)が改行区切りで入力されるので、出掛ける日数の合計を出力してください。
# 
# 例えば
# 13
# 0
# 15
# 30
# 89
# 100
# 30
# と与えられた場合
# 5
# と出力するプログラムを作成してください。

HOLIDAYS = 7
CHANSE_OF_RAIN = 30

day = 0
for i in range(HOLIDAYS):
    num = int(input())
    if num <= CHANSE_OF_RAIN:
        day += 1

print(day)