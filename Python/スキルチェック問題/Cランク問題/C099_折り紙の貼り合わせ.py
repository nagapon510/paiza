# あなたは、折り紙がたくさん置かれているのをみつけました。
# それらを連結して 1 枚の大きな紙の垂れ幕を作ることにしました。
# 
# 各折り紙は 1 辺の長さが D cm 、すなわち縦 D cm × 横 D cm の正方形です。
# これらの折り紙を、左右に長く伸びた直線を基準に貼り付けていきます。
# ただし、各折り紙について、いずれか 1 辺がちょうど直線に重なるようにします。
# また、 1 枚目を貼り付けたあと、 2 枚目以降は以下のルールに従って順に貼り付けていきます。
# 
# ・1 つ前に貼り付けた折り紙の右辺からみて、 1 cm 以上 D/2 cm 以下だけ重なるように貼り付ける。(下図に例を示しています。)
# 
# 上記のルールを守って作られたある垂れ幕について、基準の直線を平面座標の x 軸とみなして、2 枚目以降の各折り紙における 1 つ前の折り紙への重なり具合が与えられます。
# 1 枚になった垂れ幕部分の面積を計算してください。
# 例えば、入力例 1 では以下のように計算できます。

n, d = map(int, input().split(' '))

width = d
for i in range(n-1):
    width +=  d - int(input())

vol = width * d
print(vol)