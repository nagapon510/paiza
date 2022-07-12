# あなたはアメリカで働くことになったので、英語の勉強をしています。
# ある雑誌を読んでいると「asap」という表現が出てきて、これは「as soon as possible」の頭文字を取って略したものであることがわかりました。
# 
# いくつかの単語からなる表現が与えられるので、同じように単語の頭文字を前から順に並べる形で略したものを出力してください

n = int(input())
strs = input().split(' ')
abb = []

for i in range(n):
    abb.append(strs[i][0])

print(''.join(abb))