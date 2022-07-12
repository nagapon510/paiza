# あなたは本の表紙を作っています。
# 本の表紙は最大で10文字分の幅しかありません。
# 
# 表紙に印刷する文字列 S が与えられるので 10 文字ごとに改行して出力するプログラムを作成してください。
# 
# 例えば入力例 1 では
# 
# PaizaPaizaPaiza
# 
# と入力されるので
# 
# PaizaPaiza
# Paiza
# 
# と出力してください。


# string型が既にcharの配列のためリストに変更する必要なし
strs = input()
ret = []

for i in range(len(strs)):
    ret.append(strs[i])
    if (i + 1) % 10 == 0:
        ret.append("\n")

print(''.join(ret))