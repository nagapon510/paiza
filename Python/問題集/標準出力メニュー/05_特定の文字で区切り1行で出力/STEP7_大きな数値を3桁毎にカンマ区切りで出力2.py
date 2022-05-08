# 大きな数値Nが入力されます。
# 位の小さい方から 3 けたごとにカンマ区切りで出力してください。
# ただし、Nのけた数は 3 の倍数とは限りません。

nums = list(input())
nums.reverse()

result = []

for i,num in enumerate(nums):
    result.append(num)
    if (i + 1) % 3 ==0 and i+1 != len(nums):
        result.append(',')

result.reverse()
print(''.join(result))