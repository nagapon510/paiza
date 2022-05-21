# あなたは友人に向けてメールを送ろうとしています。
# ただメールを送るだけではつまらないので、文字列を装飾して送ることにしました。
# 送りたい文字列の周囲を "+" で枠のように囲んで装飾します。
# 
# このような処理を手作業で行いたくないため、プログラムで装飾しようとしています。
# この "+" の枠で囲む装飾をするプログラムを書いてください。
# 
# 入力例 1 では "Paiza" という文字列を送ります。
# この文字を枠で囲み装飾すると、以下のようになります。

# +++++++
# +Paiza+
# +++++++

s = input()
print("+" * (len(s) + 2))
print(f"+{s}+")
print("+" * (len(s) + 2))