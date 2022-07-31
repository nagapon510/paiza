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

nums_str = input().split(' ')
nums = list(map(int, nums_str))

steps = []
for i in range(3):
    steps[i] = sum(nums[0:i+1])

strs = "ABCDEFGHIJ"
print(strs[0:steps[0]])
print(strs[steps[0]:steps[1]])
print(strs[steps[1]:steps[2]])