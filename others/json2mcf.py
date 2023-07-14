#コードの構成が終わってるからいつかなおす
#あとなんか速度がおかしくなるやつも


import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class json2mcf():
    def __init__(self):
        pass

    def select_file(self,path):
        self.path = path
        self.filename = os.path.basename(self.path)
        self.trackname = (self.filename).split(".")[0]
        self.dirname = "output"
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        self.dirpath = self.dirname + "/" + self.trackname + ".mcfunction"
        self.stoppath = self.dirname + "/" + self.trackname + "_stop.mcfunction"


    def load_file(self):
        #正規処理
        try:
            #ファイルを読み込み
            self.input_file = open(self.path, "r")
            self.output_file = open(self.dirpath, "w")
            self.stop_file = open(self.stoppath, "w")
            self.table = open("./table2.json")

            #jsonを辞書化
            self.json_l = json.load(self.input_file)
            self.json_table = json.load(self.table)
            
            return True
        
        #エラー処理
        except:
            messagebox.showerror(title="complete",message="ファイルが見つかりません")
            return False
        

    def get_filename(self):
        return self.filename


    def close_files(self):
        self.input_file.close()
        self.output_file.close()
        self.stop_file.close()


    def make_list(self):
        self.mul = 8.0 #分解能 二分音符をいくつに分割するか
        self.space = int(self.mul * 3)
        
        self.finish = 0     #終了時のtick数
        self.sec = self.space    #実時間記録用

        self.bpm_changes = [] #Mod環境におけるbpm変化時のtick
        self.bpm_list = []
        self.tps_list = []
        
        self.tick_list = [] #Modなし環境におけるbpm変化時のtick

        for tempo in self.json_l["tempo"]: #bpm変化のタイミングと値をリスト化
            self.bpm = tempo["bpm"]
            self.timing = (tempo["seconds"] * self.mul) + self.space
            self.tps = 20*(self.bpm/150) * (self.mul/8.0)

            self.bpm_changes.append(self.timing)
            self.bpm_list.append(self.bpm)
            self.tps_list.append(self.tps)

        if not self.is_mod_installed:
            for d in range(len(self.bpm_changes)-1): #各BPM区間の開始点を実時間(20tps)に変換
                self.diff = self.bpm_changes[d+1] - self.bpm_changes[d]
                self.sec += self.diff/self.tps_list[d] * 20
                self.tick_list.append(self.sec)
        

    def write_header(self):
        self.output_file.write("scoreboard players add cul_" + self.trackname + " cul_piano 1\n")#ループ用

        self.stop_file.write("scoreboard players reset cul_" + self.trackname + " cul_piano\n")#停止用
        self.stop_file.write("schedule clear cul:piano/music/" + self.trackname + "\n")
    
        if self.is_mod_installed:
            self.stop_file.write("tps 20\n")#停止用
            #BPM変化に伴うtps変化の適用
            for i in range(len(self.bpm_changes)): #BPM変化コマンドの書き出し
                self.output_file.write("execute if score cul_" + self.trackname + " cul_piano matches " + str(int(self.bpm_changes[i])) + " run tps " + str(round(self.tps_list[i], 1)) + "\n")


    def write_footer(self):
        self.output_file.write("execute if score cul_" + self.trackname + " cul_piano matches 1.." + str(self.finish + self.space) + " run schedule function cul:piano/music/" + self.trackname +" 1t\n")
        self.output_file.write("execute if score cul_" + self.trackname + " cul_piano matches " + str(self.finish + self.space + 1) + ".. run scoreboard players reset cul_" + self.trackname +" cul_piano\n")
        if self.is_mod_installed:
            self.output_file.write("execute if score cul_" + self.trackname + " cul_piano matches " + str(self.finish + self.space + 1) + ".. run tps 20\n")


    def get_time(self):
        for i in range(len(self.bpm_changes)):
            if self.timestamp >= self.bpm_changes[i]:
                blng = i
        return blng


    def conversion_timestamp_without_mod(self):
        blng = self.get_time() #どのbpm区間に存在しているか
        dist = (self.timestamp-self.bpm_changes[blng]) * (150/self.bpm_list[blng]) #そのbpm区間開始からのtick数
        return round(self.tick_list[blng-1] + dist) #timestampを更新


    def exchanging(self,is_mod_installed):
        self.is_mod_installed = is_mod_installed
        try:
            self.make_list()    #データリストの作成
        except:
            messagebox.showerror(title="format error",message="ファイルのフォーマットが対応していない可能性があります")
            os.remove(self.dirpath)
            os.remove(self.stoppath)
            return False
        
        self.write_header() #output_fileのheaderを書き込み

        #bpmとtpsを初期化
        self.current_bpm = self.bpm_list[0]
        self.current_tps = self.tps_list[0]
        
        for track in self.json_l['tracks']:
            if track['notes'] != []:
                self.track_note = track['notes']
                for note in self.track_note:
                    self.note_name = str(note["name"]).lower().replace('#', 's')
                    self.note_midi = note["midi"]
                    self.timestamp = int(note["time"] * self.mul + self.space)

                    #modなしのtick計算
                    if not self.is_mod_installed:
                        self.timestamp = self.conversion_timestamp_without_mod() #timestampを更新

                    if self.finish < self.timestamp: #timestampの最大値を保存
                        self.finish = self.timestamp

                    for j in range(len(self.bpm_changes)-1): #bpm変化を適応(mod環境)
                        if self.is_mod_installed:
                            if self.timestamp == self.bpm_changes[j]: #bpm変更tickになったら適用 (modあり)
                                self.current_bpm = self.bpm_list[j]
                                self.current_tps = self.tps_list[j]
                        else:
                            if self.timestamp == self.tick_list[j]: #bpm変更tickになったら適用 (modなし)
                                self.current_bpm = self.bpm_list[j]
                                self.current_tps = self.tps_list[j]

                    velocity = str((note["velocity"] ** 2) * 11/(((self.note_midi%12)**2)/11+11))
                    duration = note["duration"]
                    inst_d = (60.0 / self.current_bpm) * duration
                    animation_time = str(int(inst_d * self.current_tps) + 4)
                    for tb in range(88):
                        if self.json_table["table"][tb]["midi"] == self.note_midi:
                            if inst_d < 0.15:
                                inst = str(self.json_table["table"][tb]["inst"][0])
                            elif inst_d < 0.25:
                                inst = str(self.json_table["table"][tb]["inst"][1])
                            elif inst_d < 0.35:
                                inst = str(self.json_table["table"][tb]["inst"][2])
                            elif inst_d < 0.5:
                                inst = str(self.json_table["table"][tb]["inst"][3])
                            elif inst_d < 0.7:
                                inst = str(self.json_table["table"][tb]["inst"][4])
                            else:
                                inst = str(self.json_table["table"][tb]["inst"][5])

                            value = str(self.json_table["table"][tb]["value"])

                            self.output_file.write("execute if score cul_" + self.trackname + " cul_piano matches " + str(self.timestamp) + " run scoreboard players set cul_" + self.note_name + "_ani cul_piano " + animation_time + "\n")
                            self.output_file.write("execute at @a run execute if score cul_" + self.trackname + " cul_piano matches " + str(self.timestamp) + " run playsound minecraft:block." + inst + " master @p ~ ~ ~ " + velocity + " " + value + "\n")

        self.write_footer() #終了用コマンドを追記
        self.close_files()

        return True

class midi2mcf():
    def __init__(self):
        pass


class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("480x320")
        self.root.title("MIDI Converter for Minecraft Realistic Piano Datapack")
        self.make_buttons()
        self.j2m = json2mcf()

        self.root.mainloop()


    def stop(self):
        self.root.destroy()


    def file_sellect(self):
        typ = [('Jsonファイル, MIDIファイル','*.json , *.mid')]
        dir = 'C:\\pg'
        path = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
        if os.path.basename(path).split(".")[-1] == "json":#jsonの場合
            self.j2m.select_file(path)                     #ファイル選択
            selected_file = self.j2m.get_filename()        #ファイル名を取得

        if os.path.basename(path).split(".")[-1] == "mid": #midiの場合
            selected_file = ""
            messagebox.showerror(title="error",message="midiの変換は未対応です")

        self.entry_box.configure(state="normal")       #書き込み可に設定
        self.entry_box.delete(0,tk.END)                #初期化
        self.entry_box.insert(tk.END,selected_file)    #ファイル名を表示
        self.entry_box.configure(state="readonly")     #読み取り用に再設定


    def exchanging(self):
        if self.j2m.load_file():
            if self.j2m.exchanging(self.bln.get()):
                messagebox.showinfo(title="complete",message="変換が完了しました")


    def make_buttons(self):
        #チェックボックスを作成
        self.bln = tk.BooleanVar()
        self.bln.set(True)
        #チェックボタン設定
        chk = tk.Checkbutton(self.root, variable=self.bln, text="G4mespeed changer Modを導入済み")

        #文字設定
        label = tk.Label(self.root, text= "読み込むjsonファイルを選択してください。\nModが導入されていない場合は下のチェックボックスを外してください。\n")

        # ボタンの作成はButtonを使用する。commandにて実行関数を指定する。
        button = tk.Button(text="ファイルを選択", command=self.file_sellect)
        exchange_button = tk.Button(text="変換", command=self.exchanging)
        exit_button = tk.Button(text="終了", command=self.stop)

        #読み込み済みファイル表示用
        self.entry_box = tk.Entry(width=40,state="readonly") #読み込み専用に設定

        label.pack()
        chk.pack()
        button.pack()
        self.entry_box.pack()
        exchange_button.pack()
        exit_button.place(x=420, y=260)


def main():
    Application()


if __name__ == "__main__":
    main()

