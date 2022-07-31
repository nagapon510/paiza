# あなたはあるイベントを主催していて、参加者の一人にゲストのサイン入りの本をプレゼントしようとしています。
# 公平を期すため、じゃんけんでプレゼントする人を決めようとしていますが、数が多いため通常のじゃんけんでは決着がつきません。
# 
# そこで、じゃんけんをして、最も同じ手の人が少なかった手を出した人をひとまず勝者とすることにしました。
# ただしこのじゃんけんでは、グーおよびパーしか出すことができません。
#
# 勝った人はどちらの手を出していたか求めるプログラムを作成してください。
# ただし、どちらの手も出している人の数が同じ場合は引き分けとなります。

import collections

num = int(input())
gp = input().split(' ')
gp_cnt = collections.Counter(gp)

if gp_cnt['G'] < gp_cnt['P']:
    print("G")
elif gp_cnt['P'] < gp_cnt['G']:
    print("P")
else:
    print("Draw")


# IF文より↓のがシンプルかも。出現回数が最も少ない要素([-1]で取得)のタプル(要素, 出現回数)から要素のみ取得
# ⇒これ1行だとDrawが拾えない。無理にDrawを拾うくらいだったら↑のIF文のがわかりやすそう。
# 
# print(gp_cnt.most_common()[-1][0])