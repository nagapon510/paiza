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

# replaceの記載に変更
bfr = input()
aft = bfr.replace('A', '4').replace('E', '3').replace('G', '6').replace('I', '1').replace('O', '0').replace('S', '5').replace('Z', '2')
print(aft)