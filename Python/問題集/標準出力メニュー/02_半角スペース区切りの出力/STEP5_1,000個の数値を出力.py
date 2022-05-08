# 1 から 1,000 までの数値をすべて、半角スペース区切りで出力してください。
# ただし、末尾に半角スペースを出力してはいけません。

nums = []
for i in range(1000):
    nums.append(str(i + 1))
print(' '.join(nums))