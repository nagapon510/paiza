# 九九表を出力してください。
# 具体的には、出力のi行j列目 (1 ≦ i, j ≦ 9) の数値は i * j になるように出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

result = []

for i in range(9):
    for j in range(9):
        result.append(str((i + 1) * (j + 1)))
        if (j + 1) == 9:
            result.append('\n')
        else:
            result.append(' ')

print(''.join(result))