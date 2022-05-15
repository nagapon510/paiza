# テストが返却されたので、友達同士で平均点を計算することになりました。
# 人数が自分を含め 7 人なので、どうしても割り切れない場合があるため、 小数点 1 桁まで計算し、小数点以下 2 桁目で四捨五入することにしました。 
# 例えば入力例 1 の場合、平均点が 58.571.... と続いていくので、小数点第一位までの "58.6" を出力します。
# 
# 7 人の点数が入力されるので、平均点を小数点以下 1 桁で表示してください。

score = input().split(' ')
score_sum = 0
for i in range(7):
    score_sum += int(score[i])
score_ave = round(score_sum / 7, 1)
print(score_ave)


# ↓ scoreの中身がstring型のため総和を求めるsum関数は使えない & int関数はリストには使用不可
# 
# score = input().split(' ')
# score_ave = round(sum(int(score)) / 7, 1)
# print(score_ave)