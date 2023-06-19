from datetime import datetime
import sys

time1 = input("開始時間")
time2 = input("終了時間")
FMT = '%H:%M'
tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
print(tdelta)