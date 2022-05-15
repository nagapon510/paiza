# あなたは文字列 s の中に文字 c が n 文字目に存在するかどうか確認するプログラムを作成しています。
# 
# 文字列 s ,文字 c ,確認する文字列の位置 n が改行区切りで与えられるので、文字列 s の n 文字目に文字 c が存在する場合は "Yes" と存在しない場合は "No" と出力してください。
# 
# 入力例 1 の場合
# 
# paiza
# i
# 3
# 
# paiza の 3 文字目に i が存在するので
# 
# Yes
# 
# と出力してください。

s = input()
c = input()
n = int(input())
if s[n-1] == c:
    print("Yes")
else:
    print("No")


# ↓ 1ケースだけ不正解になる
# s = input()
# c = input()
# n = int(input())
# if s.find(c) + 1 == n and s.find(c) != -1:
#     print("Yes")
# else:
#     print("No")