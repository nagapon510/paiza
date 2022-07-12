# 半角アルファベットのみで構成された長さmの文字列s_iがn行入力されます。
# 
# 以下のような形式で
# 
# Hello [s_1],[s_2],...[s_n].
# 
# 「Hello」に文字列s_iを入力された順に「,」で結合したものを半角スペースで結合し、末尾に「.」を結合した文字列を出力するプログラムを作成してください。

n = int(input())
strs = []

for i in range(n):
    strs.append(input())

print(f"Hello {','.join(strs)}.")