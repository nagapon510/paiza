# 1 から 15 までの整数 N が入力されるので、円周率を小数点第 N 位まで出力してください。
# 例えば N = 2 の場合、答えは 3.14 となります。
# 
# また、円周率の小数点第 15 位までは 3.141592653589793 です。

import math

num = int(input())
print(math.floor(math.pi * 10 ** num) / (10 ** num))

# 「math.floor」だと切り捨てる桁数の指定ができない
# import math
# 
# num = int(input())
# print(math.floor(math.pi)

# 提出したやつ(切り捨てできないからごり押し)
# import math
# 
# num = int(input())
# pi_str = str(math.pi)
# pi_float = []
# for i in range(num + 2):
#     pi_float.append(pi_str[i])
# print(''.join(pi_float))