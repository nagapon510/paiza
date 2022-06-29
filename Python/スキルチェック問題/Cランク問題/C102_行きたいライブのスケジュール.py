# あなたは 2 つのバンド A, B のライブに行きたいと思っています。
# 全てのライブに行こうと思っていますが、31 日まである今月は、2 つのバンドのライブが被っている日と被っていない日があります。
# そこで、ライブの日付が被っていない日は、ライブがある方のバンドのライブに行くことにし、日付が被った日は、
# バンド A からバンド A のライブとバンド B のライブを交互に行くことにしました。バンド A, Bのライブの日程が与えられるので、今月の i 日目 (1 ≦ i ≦ 31) にバンド A とバンド B のいずれのライブに行くかを表す文字列を出力してください。
# 
# 入力例 1 の場合、バンド A のライブは 6 日、バンド B のライブは 5 日あります。
# まず、12 日目はバンド A, B 両方のライブが入っています。今月最初のライブが被っている日なので、12 日目はバンド A のライブに行くことになります。
# 13 日目は、バンド B のライブしかないので、バンド B のライブに行くことになります。
# 14 日目は、ライブが被っており、前回、ライブが被った 12 日目は、バンド A のライブに行くことになっているので、バンド B のライブに行くことになります。
# 同様に、15 日目も被っているので、15 日目はバンド A のライブに行くことになります。

a_days = int(input())
a_list = []
for i in range(a_days):
    a_list.append(int(input()))

b_days = int(input())
b_list = []
for i in range(b_days):
    b_list.append(int(input()))

j = 0
for i in range(31):
    if i+1 in a_list and i+1 in b_list:
        if (j+2) % 2 == 0:
            print("A")
        else:
            print("B")
        j += 1
    elif i+1 in a_list:
        print("A")
    elif i+1 in b_list:
        print("B")
    else:
        print("x")