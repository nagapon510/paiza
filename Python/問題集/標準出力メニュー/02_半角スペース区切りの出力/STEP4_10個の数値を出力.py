# 1 から 10 までの数値をすべて、半角スペース区切りで出力してください。
# ただし、末尾に半角スペースを出力してはいけません。

nums = []
for i in range(10):
    nums.append(str(i + 1))
print(' '.join(nums))