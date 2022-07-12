# 9 個の数値が半角スペース区切りで入力されます。
# この数値を 3 行 3 列の形式で出力してください。
# 具体的には、入力された数値を N_1 , N_2 , N_3 , ..., N_9 とするとき、1 行目にはN_1 からN_3 を、2 行目には N_4 から N_6 を、3 行目には N_7 から N_9 を出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

nums = input().split(' ')
result = []
for i, num in enumerate(nums):
    result.append(str(num))
    if (i+1) % 3 == 0:
        result.append('\n')
    else:
        result.append(' ')

print(''.join(result))