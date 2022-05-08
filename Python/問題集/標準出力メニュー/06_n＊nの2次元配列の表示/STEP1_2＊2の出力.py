# 4 つの数値 0, 8, 1, 3 をこの順に、2 行 2 列の形で出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

nums = [0, 8, 1, 3]
result = []
for i, num in enumerate(nums):
    result.append(str(num))
    if (i+1) % 2 == 0:
        result.append('\n')
    else:
        result.append(' ')

print(''.join(result))