# ある単語が与えられるので、母音を削除した結果の文字列を出力するプログラムを作成してください。
# なお、母音とは 「a, e, i, o, u」 のことを指しています。
# 
# 例えば入力例 1 の場合
# 
# tamago
# 
# a と o を削除し tmg として以下のように出力してください
# 
# tmg

# string型が既にcharの配列のためリストに変更する必要なし
strs = input()
abb = []

for x in strs:
    if x != "a" and  x != "e" and  x != "i" and x != "o" and  x != "u":
        abb.append(x)

print(''.join(abb))