# あなたはサーバ管理者です。 日々洪水のように流れるログを追っています。
# とうとう自分の目と頭では処理しきれない量になってしまったため、プログラムを作って、重要な文字列を含むログだけ抽出する事にしました。
# 
# 例えば、入力例 2 では、ログは上から順に "pizza"、 "paiza"、 "aizu"、 "ai"、 "sai" の 5 つです。
# この 5 つのログに対して、重要な文字列 "ai" が含まれているのは "pizza" 以外の 4 つです。
# 結果として "pizza" だけが除かれ、 "paiza"、 "aizu"、 "ai"、 "sai" がこの順に抽出されます。
# 
# このように、ログと重要な文字列が与えられたとき、重要な文字列が含まれているログを抽出して出力するプログラムを作成してください。
# 重要な文字列が含まれていない場合は "None" と出力してください。

n = int(input())
key = input()
keylogs = []

for i in range(n):
    log = input()
    if key in log:
        keylogs.append(log)

if len(keylogs) == 0:
    print("None")
else:
    for keylog in keylogs:
        print(keylog)