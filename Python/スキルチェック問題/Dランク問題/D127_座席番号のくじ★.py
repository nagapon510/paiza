# あるコンサートの入場券は大文字アルファベット 1 文字に数字を 3 つ続けた番号が振られています。
# 先頭の大文字アルファベット一文字を除いた数字 3 文字がゾロ目 (全て同じ) のお客さんには豪華プレゼントがあるそうです。
# 入場券に振られていた 4 文字が与えられるのでプレゼントがもらえるかを出力してください。
# 
# 例えば入力される入場券の文字列が、"S123" の場合はもらえないので　"No"、"P777" の場合はプレゼントがもらえるので "Yes" を出力してください。


# string型が既にcharの配列のためリストに変更する必要なし
strs = input()

if len(set(strs)) == 2:
    print("Yes")
else:
    print("No")