# Leet と呼ばれるインターネットスラングがあります。
# Leet ではいくつかのアルファベットをよく似た形の他の文字に置き換えて表記します。 
# Leet の置き換え規則はたくさんありますが、ここでは次の置き換え規則のみを考えましょう。
# 置き換え前	置き換え後
# A	4
# E	3
# G	6
# I	1
# O	0
# S	5
# 
# 2文字列が入力されるので、これを Leet に変換して出力するプログラムを書いてください。

leetdic = {'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O':'0', 'S':'5', 'Z':'2'}
bfr = input()
aft = []

for str in bfr:
    if str in leetdic:
        aft.append(leetdic[str])
    else:
        aft.append(str)

print(''.join(aft))