# 3 つの文字列が改行区切りで与えられます。
# これらの文字列をバーティカルライン | 区切りで出力してください。

import sys

strs = []
for line in sys.stdin.readlines():
    strs.append(line.rstrip())
print('|'.join(strs))