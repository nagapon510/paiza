# あなたはお祭りでストラックアウトを出すことになりました。
# ストラックアウトは H × W のマス状に配置されたパネルを撃ち抜くゲームです。
# それぞれのパネルにはそれぞれの得点が書かれており、ゲームが終了した際、撃ち抜かれたパネルの得点を合計して最終得点を出します。
# 撃ち抜かれたパネルとそれぞれの得点が与えられるので、得点集計を自動化するプログラムを作成してください。
# 
# 入力例 1 の場合、4 × 3 マスのパネルが与えられます。それぞれのパネルには、下図のように得点が割り当てられています。
# ゲーム終了後には、それぞれのパネルが撃ち抜かれているか、残っているかが、それぞれ半角アルファベットの "o" と "x" で示されます。
# 下図では、1, 3, 4, 5, 7, 9 のパネルが撃ち抜かれているので、期待される出力はそれらの合計である 29 となります。

h, w = map(int, input().split(' '))
ret = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
    panels = input()
    for j, panel in enumerate(panels):
        ret[i][j] = 1 if panel == "o" else 0

total = 0
for i in range(h):
    points = input().split(' ')
    for j, point in enumerate(points):
        total += int(point) * ret[i][j]

print(total)