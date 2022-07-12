# 今日は PAIZA 6 というくじの当選番号の公表日です。
# 
# PAIZA 6 の購入者は 1 から 100 までの好きな数字を 6 つ選びます。
# 抽選では同様に 6 つの当選番号が発表され、購入したくじの数字と一致していた数字の数に応じて賞金が当たります。
# 
# あなたは、先日 N 枚のくじを購入しました。
# プログラマーであるあなたは、N 枚の宝くじそれぞれについて、 当選番号と一致した数字の数について調べるプログラムを書くことにしました。
# 
# ここで、くじの購入例を見てみましょう。
# 
# 上の N = 3 の例では、当選番号と一致した数字は赤で表されており、 上から順に、3 個、1 個、0 個となっています。
# なお、例から分かる通り、くじの数字は昇べきの順に並んでいるとは限りません。

winnums = input().split(' ')
n = int(input())

for i in range(n):
    ordernums = input().split(' ')
    print(len([ordernum for ordernum in ordernums if ordernum in winnums]))