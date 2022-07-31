# 大きな数値 N が入力されます。
# 3 けたごとにカンマ区切りで出力してください。
# ただし、N のけた数は 3 の倍数です。

nums = list(input())
nums.reverse()

result = []

for i,num in enumerate(nums):
    result.append(num)
    if (i + 1) % 3 ==0 and i+1 != len(nums):
        result.append(',')

result.reverse()
print(''.join(result))