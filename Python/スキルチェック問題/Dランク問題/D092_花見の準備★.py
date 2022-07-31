# あなたはお花見の準備のためにレジャーシートを買うことにしました。
# レジャーシートの質に興味のないあなたは最も面積あたりの価格の安いレジャーシートを探すため、プログラムを書くことにしました。

# 2つのレジャーシートの横の長さ x, 縦の長さ y, 価格 p が スペース区切りで与えられます。
# 
# 最も面積あたりの価格の安いレジャーシートの x, y ,p をスペース区切りで出力するプログラムを作成してください。
# ただし、面積あたりの価格が同じ場合は "DRAW" と出力してください

sheet1 = input().split(' ')
sheet2 = input().split(' ')
sheet1price = int(sheet1[2]) / (int(sheet1[0]) * int(sheet1[1]))
sheet2price = int(sheet2[2]) / (int(sheet2[0]) * int(sheet2[1]))

if sheet1price == sheet2price:
    print("DRAW")
elif sheet1price < sheet2price:
    print(" ".join(sheet1))
else:
    print(" ".join(sheet2))