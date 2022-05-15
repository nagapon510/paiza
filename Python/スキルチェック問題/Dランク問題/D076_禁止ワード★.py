# あなたは禁止ワードが含まれるかどうかを判定するプログラムを作成しています。
# 
# 禁止ワード W と判定する文字列 S が改行区切りで順に与えられるので S に W が含まれている時は "NG" それ以外の場合は文字列 S をそのまま出力してください。
# 
# 例えば入力例 1 の場合
# 
# ngword
# thisisngword
# 
# "ngword" が "thisisngword" 内に含まれているので
# 
# NG
# 
# と出力してください。

ban = input()
s = input()
if ban in s:
    print("NG")
else:
    print(s)