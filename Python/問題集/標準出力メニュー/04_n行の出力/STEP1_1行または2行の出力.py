# 数値 N (N = 1 または 2) が入力されます。
# N = 1 の場合は 1 を、N = 2 の場合は 1 と 2 を改行区切りで出力してください。

num = int(input())
if num == 1:
    print(1)
else:
    print(1, 2, sep="\n")