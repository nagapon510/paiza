# あなたは、高速道路の管理運営を仕事にしています。
# そこで、運転者に道路がどの程度渋滞しているかを知らせるシステムを作ることにしました。
# 
# ある道路の車の数と、各車の車間距離が与えられるので、車間距離が M メートル以下の場合を渋滞と定義したとき、渋滞の区間が合計で何メートルあるか求めるプログラムを作成してください。
# なお、車の車体の長さは無視して計算してください。 

n, m = map(int, input().split(' '))
traffic = 0

for i in range(n-1):
    distance = int(input())
    if distance <= m:
        traffic += distance

print(traffic)