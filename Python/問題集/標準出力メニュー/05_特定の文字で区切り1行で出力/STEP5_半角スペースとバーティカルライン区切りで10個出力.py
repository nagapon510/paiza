# 10 個の数値が改行区切りで与えられます。
# これらの数値を半角スペース 2 つとバーティカルライン | 区切りで出力してください。
# ただし、末尾には改行を出力してください。

import sys

strs = []
for line in sys.stdin.readlines():
    strs.append(line.rstrip())
print(' | '.join(strs))