# インターネットのとあるサービスで利用するためのハンドルネームを作ることにしました。
# そのハンドルネームは名前の文字列から母音を取り除いて子音のみを連結して生成します。
# ただし、ここで母音とは "a", "e", "i", "o", "u" の 5 つのアルファベットの小文字( "a", "e", "i", "o", "u" )、
# 大文字( "A", "E", "I", "O", "U" )を指し、子音とはそれ以外のアルファベットを意味します。

name = list(input())
result = []

for x in name:
    if x.lower() != 'a' and x.lower() != 'i' and x.lower() != 'u' and x.lower() != 'e' and x.lower() != 'o':
        result.append(x)

print(''.join(result))