# あなたは運悪く病気にかかってしまい入院しなくてはいけなくなりました。
# しかし、嫌いな数字があり、その数字が含まれる部屋番号の病室に入ると治療がうまく行かないのでは無いかと不安になってしまいます…。
# 
# そこで、部屋番号のどの桁にも嫌いな数字が含まれていない病室をリストアップして入院先に伝えることにしました。
# 
# ・1行目に嫌いな数字 n (0から9までの1桁の数字)
# ・2行目に病室の総数 m
# ・3行目以降に各病室の部屋番号を表す整数 r_i (1 <= i <= m)
# 
# が改行区切りで与えられるので、希望する病室の部屋番号をすべて改行区切りで出力して下さい。
# もし、希望する病室が1つもない場合は"none" と出力して下さい。

n = input()
m = int(input())

desired_rooms = []
for i in range(m):
    room = input()
    if n not in room:
        desired_rooms.append(room)

if len(desired_rooms) == 0:
    print("none")
else:
    for desired_room in desired_rooms:
        print(desired_room)