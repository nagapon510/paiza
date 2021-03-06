#  半径r のお気に入りのボールを手に入れたあなたは、それを収納することができる箱を探しています。
# 今、n 個の箱があり、i (1 ≦ i ≦ n) 番目の箱は高さh_i、幅w_i、奥行きd_i です。各箱においてボールの直径が、
# 箱の高さ、幅、奥行きの3つの長さのうち最も短いもの以下であれば、無事にボールを収納することができます。
# 
# ボールの半径と箱の情報が与えられるので、ボールを収納することができる箱の番号を昇順にすべて答えてください。
# 
# 入力される値
# 入力は以下のフォーマットで与えられます。
# 
# n r　　　#箱の数n, ボールの半径r 表す整数
# h_1 w_1 d_1　　　#1個目の箱の高さ、幅、奥行きを表す整数
# h_2 w_2 d_2　　　#2個目の箱の高さ、幅、奥行きを表す整数
# ...
# h_n w_n d_n　　　#n個目の箱の高さ、幅、奥行きを表す整数
# 
# それぞれの値は文字列で標準入力から渡されます。

n, r = map(int,input().split(' '))
ret = []

for i in range(int(n)):
    box = input().split(' ')
    for j in range(len(box)):
        box[j] = int(box[j])
    if int(r * 2) <= min(box):  #半径×2に修正
        ret.append(i + 1)

# 最後にまとめて出力する仕様に変更
print('\n'.join(map(str,ret)))