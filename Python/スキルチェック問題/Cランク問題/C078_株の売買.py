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

days, limit_buy, limit_sell = map(int, input().split(' '))
profit = 0
hold = 0

for i in range(days - 1):
    price = int(input())
    if price <= limit_buy:
        profit -= price
        hold += 1
    elif limit_sell <= price:
        profit += price * hold
        hold = 0

# 最終日処理を外出し
price = int(input())
profit += price * hold
hold = 0

print(profit)