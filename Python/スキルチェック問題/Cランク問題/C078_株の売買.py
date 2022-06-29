# あなたは、株の売買でのお金儲けを考えています。
# N 日の間、1 日に一度株価をチェックし、以下のルールに従い売買をします。
# 
# ・株価が c_1 円以下の場合、1 株買う
# ・株価が c_2 円以上の場合、持ち株「を」すべて売る
# ・株価が c_1 円、c_2 円の間の場合は、何もしない
# ・N 日目には、上記を行わず持ち株をすべて売る
# 
# N 日目に持ち株をすべて売ったあとでの損益を出力してください。
# ただし、入力例 2 のように損益がマイナスになる場合があることに注意してください。

num = input().split(' ')
profit = 0
hold = 0
for i in range(int(num[0])):
    price = int(input())
    if i+1 == int(num[0]):
        profit += price * hold
        hold = 0
    elif price <= int(num[1]):
        profit -= price
        hold += 1
    elif price >= int(num[2]):
        profit += price * hold
        hold = 0

print(profit)