import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def exchange_file(json_l,output_file,json_table,trackname):
    
    mul = 8.0 #mul*2分音符まで対応
    space = 24 #開始時、終了時の猶予

    time_list = []
    bpm_list = []
    tps_list = []

    #BPM変化を計算 
    for tempo in json_l["tempo"]:
        bpm = int(tempo["bpm"])
        time = (tempo["seconds"] * mul) + space
        tps = 20*(bpm/150) * (mul/8.0)
        time_list.append(time)
        bpm_list.append(bpm)
        tps_list.append(tps)
    
    #modが導入されているならtpsコマンドを導入
    is_mod_introdused = bln.get()
    finish = 0
    output_file.write("scoreboard players add cul_" + trackname + " cul_piano 1\n")
    if is_mod_introdused:
        for i in range(len(time_list)):
            output_file.write("execute if score cul_" + trackname + " cul_piano matches " + str(int(time_list[i])) + " run tps " + str(round(tps_list[i], 1)) + "\n")

    #bpmとtpsを初期化
    bpm = bpm_list[0]
    tps = tps_list[0]


    #note情報を変換
    for i in range(16):
        if json_l['tracks'][i]['notes'] != []:
            track_note = json_l['tracks'][i]['notes']
            for note in track_note:
                note_name = str(note["name"]).lower().replace('#', 's')
                note_midi = note["midi"]
                timestamp = int(note["time"] * mul + space)
                if finish < timestamp:
                    finish = timestamp
                for j in range(len(time_list)-1): #bpm変化を適応
                    if timestamp == time_list[j]:
                        bpm = bpm_list[j]
                        tps = tps_list[j]
                velocity = str((note["velocity"] ** 2) * 11/(((note_midi%12)**2)/11+11))
                duration = note["duration"]
                inst_d = (60.0 / bpm) * duration
                animation_time = str(int(inst_d * tps) + 1)
                for tb in range(88):
                    if json_table["table"][tb]["midi"] == note_midi:
                        if inst_d < 0.15:
                            inst = str(json_table["table"][tb]["inst"][0])
                        elif inst_d < 0.25:
                            inst = str(json_table["table"][tb]["inst"][1])
                        elif inst_d < 0.35:
                            inst = str(json_table["table"][tb]["inst"][2])
                        elif inst_d < 0.5:
                            inst = str(json_table["table"][tb]["inst"][3])
                        elif inst_d < 0.7:
                            inst = str(json_table["table"][tb]["inst"][4])
                        else:
                            inst = str(json_table["table"][tb]["inst"][5])

                        value = str(json_table["table"][tb]["value"])
                        output_file.write("execute if score cul_" + trackname + " cul_piano matches " + str(timestamp) + " run scoreboard players set cul_" + note_name + "_ani cul_piano " + animation_time + "\n")
                        output_file.write("execute at @a run execute if score cul_" + trackname + " cul_piano matches " + str(timestamp) + " run playsound minecraft:block." + inst + " master @p ~ ~ ~ " + velocity + " " + value + "\n")

    output_file.write("execute if score cul_" + trackname + " cul_piano matches 1.." + str(finish + space) + " run schedule function cul:piano/music/" + trackname +" 1t\n")
    output_file.write("execute if score cul_" + trackname + " cul_piano matches " + str(finish + space + 1) + ".. run scoreboard players reset cul_" + trackname +" cul_piano\n")


def json_to_mcf(path,dirpath,trackname):
    try:
        file = open(path, "r")
        output_file = open(dirpath, "w")
    #エラー処理
    except FileNotFoundError as FE:
        messagebox.showerror(title="complete",message= str(type(FE)) + "ファイルが見つかりません")
        #stop()

    table = open("table2.json")
    json_l = json.load(file)
    json_table = json.load(table)
    try:
        exchange_file(json_l,output_file,json_table,trackname)
        messagebox.showinfo(title="complete",message="変換が完了しました")
        file.close()
        output_file.close()
        table.close()
    except:
        messagebox.showerror(title="format error",message="ファイルのフォーマットが対応していない可能性があります")
        file.close()
        output_file.close()
        table.close()
        os.remove(dirpath)
    
    


#rootウィンドウ設定
root = tk.Tk()
root.title("Minecraft Realistic Piano Datapack")
root.geometry("480x320")

#チェックボックスを作成
bln = tk.BooleanVar()
bln.set(True)

#チェックボタン設定
chk = tk.Checkbutton(root, variable=bln, text="G4mespeed changer Modを導入済み")
#chk.place(x=100, y=70)

#文字設定
selected_file = ""
label = tk.Label(root, text= "読み込むjsonファイルを選択してください。\nModが導入されていない場合は下のチェックボックスを外してください。\n")

path = ""
trackname = ""
dirpath = ""

def stop():
    root.destroy()

# ボタンクリック時に呼び出す関数を定義
def file_select():
    global path,trackname,dirpath
    typ = [('Jsonファイル','*.json')]
    dir = 'C:\\pg'
    path = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    filename = os.path.basename(path)
    trackname = (filename).split(".")[0]
    dirname = "output"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    dirpath = dirname + "/" + trackname + ".mcfunction"

    #選択したファイル名を表示
    entry_box.configure(state="normal")  #書き込み可に設定
    entry_box.delete(0,tk.END)
    entry_box.insert(tk.END,filename)    #ファイル名を表示
    entry_box.configure(state="readonly")#読み取り用に再設定

def exchanging():
    json_to_mcf(path,dirpath,trackname)
    #stop()

# ボタンの作成はButtonを使用する。commandにて実行関数を指定する。
button = tk.Button(text="ファイルを選択", command=file_select)
exchange_button = tk.Button(text="変換", command=exchanging)
exit_button = tk.Button(text="終了", command=stop)


#エントリーボックス
entry_box = tk.Entry(width=40,state="readonly") #読み込み専用に設定



#ボタン類表示
label.pack()
chk.pack()
button.pack()
entry_box.pack()
exchange_button.pack()
exit_button.place(x=420, y=260)



root.mainloop()
