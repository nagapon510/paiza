# ひな祭りの準備をしましょう。
# あなたが持っている 10 体の人形を "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" で表します。
# ひな壇の各段 (計 3 段) に並べる人形の数が与えられるので、各段にならべる人形の記号を改行区切りで出力してください。
# 人形は必ずもとの A, B, C, ... の順番で並べます。
# 
# 例)
# 
# 各段にならべる人形の数: 2, 3, 5
# → 人形の並べ方:
# AB
# CDE
# FGHIJ

nums = input().split(' ')
first_step = int(nums[0])
second_step = int(nums[0]) + int(nums[1])
third_step = int(nums[0]) + int(nums[1]) + int(nums[2])

strs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
ret = []

for i in range(10):
    ret.append(strs[i])
    if i + 1 == first_step or i + 1 == second_step or i + 1 == third_step:
        ret.append("\n")

print(''.join(ret))