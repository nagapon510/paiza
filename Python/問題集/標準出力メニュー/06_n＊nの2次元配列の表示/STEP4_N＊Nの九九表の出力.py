# 自然数 N が入力されます。
# N 行 N 列の九九表を出力してください。
# 具体的には、出力の i 行 j 列目 (1 ≦ i, j ≦ N ) の数値は i * j になるように出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

num = int(input())
result = []

for i in range(num):
    for j in range(num):
        result.append(str((i + 1) * (j + 1)))
        if (j + 1) == num:
            result.append('\n')
        else:
            result.append(' ')

print(''.join(result))