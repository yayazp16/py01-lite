import sys
import math

if len(sys.argv) !=2  :
    print("入力直がありません")
    sys.exit()


try:
    radis = float(sys.argv[1])
    area = math.pi * math.pow(radis,2)
    print(area)

except ValueError :
    print("数字を入力して下さい")
    sys.exit()