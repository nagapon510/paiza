# あなたは 4 桁のパスワードを考える上で法則性のある数字を避けようと考えています。
# 4 桁の数字で構成されたパスワードの文字列 s が入力されるので同じ数字が 2 つ以上存在すれば「NG」、そうでない場合は「OK」と出力してください。

char = list(input())
if len(set(char)) == 4:
    print("OK")
else:
    print("NG")