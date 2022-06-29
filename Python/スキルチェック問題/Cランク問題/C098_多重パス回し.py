# あなたは友達とボールのパス回しをしています。
# どうやら、このパス回しはルールが特徴的なようです。
# 
# 最初に各人はそれぞれボールをいくつか所持しています。
# その後、適当な順番でボールをパスしていくのですが、この際にパスする相手とボールの個数を宣言します。
# 宣言した個数以上のボールを持っている場合は宣言した個数のボールを、そうでない場合は持っているボールすべてを、選んだ相手にパスします。
# なお、ボールを所持できる数に上限はありません。
# 
# このパス回しの情報が順番に与えられるので、最終的に各人が持っているボールの個数を求めてください。
# 下図は入力例 1 の様子を表しています。

n = int(input())
balls = []
for i in range(n):
    balls.append(int(input()))

m = int(input())
for i in range(m):
    passturn = input().split(' ')
    if int(passturn[2]) > balls[int(passturn[0])-1]:
        balls[int(passturn[1])-1] += balls[int(passturn[0])-1]
        balls[int(passturn[0])-1] = 0
    else:
        balls[int(passturn[1])-1] += int(passturn[2])
        balls[int(passturn[0])-1] -= int(passturn[2])

for ball in balls:
    print(ball)