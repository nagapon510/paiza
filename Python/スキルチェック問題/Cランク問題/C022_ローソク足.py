# 変化し続ける株価の様子を知るために、始値、終値、高値、安値と呼ばれる 4 種類の株価がしばしば用いられます。
# 
# 1 日間の 4 種類の株価はそれぞれ次のように定められます。
# ・始値は 1 日の最初の株価
# ・終値は 1 日の最後の株価
# ・高値は 1 日の最大の株価
# ・安値は 1 日の最小の株価
# 
# さらに、n 日間の 4 種類の株価はそれぞれ次のように定められます。
# ・始値は 1 日目の始値
# ・終値は n 日目の終値
# ・高値は 1 日目から n 日目までの最大の高値
# ・安値は 1 日目から n 日目までの最小の安値
# 
# 表では、1 日間の 4 種類の株価を5日分示しています。
# 
# 5 日間の 4 種類の株価は、表中の赤字で書かれた株価が表しており、それぞれ、始値が 11、終値が 13、高値が 17、安値が 8 となります。
# 11 は 5 日間の始値の中で 1 日目の始値、終値は 5 日間の終値の中で 5 日目の終値、17 は 5 日間の高値の中で最大の高値、8 は 5 日間の安値の中で最小の安値となっています。
# 4 種類の株価が 1 日目から順に n 日間分与えられるので、n 日間の 4 種類の株価を求めるプログラムを作成してください。

n = int(input())
fourValues = []

for i in range(n):
    fourValues_str = input().split(' ')
    fourValues.append(list(map(int, fourValues_str)))

opening_price = fourValues[0][0]
closing_price = fourValues[len(fourValues)-1][1]
high_price = max([row[2] for row in fourValues])
low_price = min([row[3] for row in fourValues])

print(f"{opening_price} {closing_price} {high_price} {low_price}")