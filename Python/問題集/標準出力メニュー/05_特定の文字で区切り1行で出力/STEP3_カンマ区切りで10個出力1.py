# 10 個の数値が半角スペース区切りで与えられます。
# これらの数値すべて受け取り、そのまま出力してください。
# ただし、数値を出力した直後に必ずカンマを、末尾にはさらに改行も出力してください。

strs = input().split(' ')
for x in strs:
    print(x, end=",")
print("")