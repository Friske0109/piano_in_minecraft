#メモ用

import json

mul = 8.0 #分解能 mul*2分音符まで対応
space = int(mul*3) #開始時、終了時の猶予

file = open("music_data/babel_f.json", "r")
json_l = json.load(file)

def get_time(time_list,timestamp):
    for i in range(len(time_list)):
        if timestamp >= time_list[i]:
            d = i
    return d
    

time_list = []
bpm_list = []
tps_list = []
tick_list = []

#BPM変化を計算 
for tempo in json_l["tempo"]:
    bpm = tempo["bpm"]
    time = (tempo["seconds"] * mul) + space
    tps = 20*(bpm/150) * (mul/8.0)
    time_list.append(time)
    bpm_list.append(bpm)
    tps_list.append(tps)

sec = space
for d in range(len(time_list)-1):
    diff = time_list[d+1] - time_list[d]
    sec += diff/tps_list[d] * 20
    tick_list.append(sec)

timestamp = 180
t = get_time(time_list,timestamp)
r = (timestamp-time_list[t]) * (150/bpm)
print(t)
print(time_list[t])
print(r)
print(bpm_list[t])
print(tick_list[t-1])

print(round(tick_list[t-1] + r))
#print(time_list)
#print(bpm_list) 
#print(tps_list)
#print(diff)
    
"""
この時点で、time_listにはBPM変化のタイミング(tick)、bpm_listにはBPMが入っている
mul=8.0のときBPM=150とすると、分解能は8.0 * 150/BPM
timestampを絶対時間(秒数)に変換 → tickに変換
"""

