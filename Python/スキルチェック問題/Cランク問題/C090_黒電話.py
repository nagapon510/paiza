# あなたは黒電話を使ったことがあるでしょうか？
# 
# 黒電話は回転ダイヤル式の電話で、ダイヤルには各数字の位置に穴が空いています。
# 数字の穴に指を入れ、フックの位置まで回して指を離し、ダイヤルが元の位置まで戻ったところで数字が 1 つ入力されます。
# 
# このような入力形式であるため、ボタン式の電話に比べると、電話番号を入力し終えるまでに少し時間がかかります。
# そこで、いくつかの電話番号に対して、ダイヤルが回る必要のある総距離を計算してみることにしましょう。
# ここで、各数字からフックまでの距離を下図のように定めます。

import re

tellno = input()
tellno = re.sub("\-","",tellno)
tell_len = len(tellno)

total_distance = 0
for i in range(tell_len):
    if tellno[i] == "0":
        total_distance += 12 * 2
    else:
        total_distance += (int(tellno[i]) + 2) * 2

print(total_distance)