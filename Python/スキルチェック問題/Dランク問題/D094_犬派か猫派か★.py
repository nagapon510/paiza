# あなたは知り合いの 3 人の中で犬が好きか猫が好きかでアンケートをとりました。
# 
# アンケートは "dog" もしくは "cat" のどちらかが書かれています。
# 改行区切りで各人の回答が 3 行の入力されるので 2 人以上が回答した方を出力してください。
# 
# 例えば以下のような入力であれば
# 
# cat
# dog
# cat
# 
# "cat" と回答した人が 2 人なので
# 
# cat
# 
# と出力してください。

dog = 0
cat = 0

for i in range(3):
    if input() == "cat":
        cat += 1
    else:
        dog += 1

if cat > dog:
    print("cat")
else:
    print("dog")