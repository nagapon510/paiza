# あなたはソースコードを読んでいる時に区切り文字として「_」(アンダースコア)と「-」(ハイフン)が混在している文字列の存在に気が付きました。
# そこで「_」か「-」どちらか一方に統一するため以下のルールで変換することにしました。
# 
# ・「_」と「-」のうち数が多い方に統一
# ・もし同数の場合は「_」に統一
# 
# 例えば入力例1 の場合
# 
# ruby_python-java-php
# 
# 「-」が2つ、「_」が1つなので「-」に統一し
# 
# ruby-python-java-php
# 
# と出力してください。

strs = input()
hyphen = strs.count('-')
underscore = strs.count('_')

if hyphen > underscore:
    ret =  strs.replace('_', '-')
else:
    ret = strs.replace('-', '_')
print(ret)