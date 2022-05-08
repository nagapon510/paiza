# 2 つの文字列 S, T が入力されます。S, T を改行区切りで出力してください。

import sys

strs = []
for line in sys.stdin.readlines():
    strs.append(line.rstrip())
print('\n'.join(strs))