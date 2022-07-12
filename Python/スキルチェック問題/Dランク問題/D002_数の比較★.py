# ある正の整数aとbがスペース区切りで入力されます。
# aとbを比較し大きい方の値を出力して下さい。aとbが同じ場合は「eq」と出力して下さい。

nums = input().split(' ')
nums.sort(key=int)

if len(set(nums)) == 1:
    print("eq")
else:
    print(nums[1])