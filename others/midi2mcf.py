#とりあえずModなしだけ実装

import mido
import math
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class Midi2Mcf():
    def __init__(self,path) -> None:
        self.path = path
        self.filename = os.path.basename(self.path)
        self.trackname = (self.filename).split(".")[0]
        if not os.path.exists("output"):
            os.makedirs("output")
        self.dirpath ="./output/" + self.trackname + ".mcfunction"
        self.stoppath ="./output/" + self.trackname + "_stop.mcfunction"
        
        try:
            self.load_files()
            self.set_const()
        except:
            messagebox.showerror(title="error",message="ファイルが見つかりません")

    def print_header(self):
        print("scoreboard players add cul_{} cul_piano 1".format(self.trackname),file=self.output)
        print("scoreboard players reset cul_{} cul_piano".format(self.trackname),file=self.output_stop)
        print("schedule clear cul:piano/music/{}".format(self.trackname),file=self.output_stop)

    def print_footer(self):
        print("execute if score cul_{} cul_piano matches 1..{} run schedule function cul:piano/music/{} 1t".format(self.trackname,self.track_msec,self.trackname),file=self.output)
        print("execute if score cul_{} cul_piano matches {}.. run scoreboard players reset cul_{} cul_piano".format(self.trackname,self.track_msec+1,self.trackname),file=self.output)

    def load_files(self):
        self.file = mido.MidiFile(self.path)
        self.table = json.load(open("./table2.json"))
        self.output = open(self.dirpath,"w")
        self.output_stop = open(self.stoppath,"w")

    def set_const(self):
        self.space = 24
        self.tempo = 500000.0
        self.ticks_per_beat = self.file.ticks_per_beat
        self.abs_time_tick_msec = self.tempo / self.ticks_per_beat / 1000.0 #1tick当たりの絶対時間(ms)

    def exchange(self):
        self.print_header()
        for track in self.file.tracks:
            now = 0  # 現在の時刻（ms）を保持
            notes = []
            for event in track:
                now = now + event.time * self.abs_time_tick_msec #tick数から絶対時間を計算
                if event.type == 'set_tempo': #bpm更新
                    tempo = event.tempo
                    self.abs_time_tick_msec = tempo / self.ticks_per_beat / 1000.0
                    # print("BPM = ", 60000000.0 / tempo)
                elif event.type == 'note_on' and event.channel == 9:
                    # 打楽器を無視
                    pass
                elif event.type == 'note_off' or (event.type == 'note_on' and event.velocity == 0):
                    # ノートオフを処理
                    for note in notes: #0=note_on, 1=note_off ,2=note_number, 3=velocity, 4=dulation
                        if (note[1] == 0) and (note[2] == event.note):
                            note[1] = now
                            note[4] = (note[1] - note[0]) / 1000.0
                            note[3] = note[3] / 127.0
                elif event.type == 'note_on':
                    notes.append([math.floor(now), 0, event.note, event.velocity, 0])

            #mcf
            for note in notes:
                start = math.floor(note[0]/50) + self.space
                note_num = note[2]
                velocity = (note[3] ** 2) * 11/(((note_num%12)**2)/11+11)
                dulation = math.floor(note[4]*20)
                self.track_msec = 0
                if self.track_msec < note[1]:
                    self.track_msec = note[1]
                self.track_msec = math.floor(self.track_msec/50) + self.space

                for tb in range(88):
                    if self.table["table"][tb]["midi"] == note_num:
                        if dulation < 0.15:
                            inst = self.table["table"][tb]["inst"][0]
                        elif dulation < 0.25:
                            inst = self.table["table"][tb]["inst"][1]
                        elif dulation < 0.35:
                            inst = self.table["table"][tb]["inst"][2]
                        elif dulation < 0.5:
                            inst = self.table["table"][tb]["inst"][3]
                        elif dulation < 0.7:
                            inst = self.table["table"][tb]["inst"][4]
                        else:
                            inst = self.table["table"][tb]["inst"][5]
                        value = self.table["table"][tb]["value"]
                        name = self.table["table"][tb]["name"]

                print("execute if score cul_{} cul_piano matches {} run scoreboard players set cul_{}_ani cul_piano {}".format(self.trackname,start,name,dulation),file=self.output)
                print("execute at @a run execute if score cul_{} cul_piano matches {} run playsound minecraft:block.{} master @p ~ ~ ~ {} {}".format(self.trackname,start,inst,velocity,value),file=self.output)

        #footer
        self.print_footer()
        self.output.close()
        self.output_stop.close()

class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("480x320")
        self.root.title("MIDI Converter for Minecraft Realistic Piano Datapack")
        self.make_buttons()

        self.root.mainloop()

    def stop(self):
        self.root.destroy()

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

    def file_sellect(self):
        typ = [('MIDIファイル','*.mid')]
        dir = 'C:\\pg'
        self.path = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
        selected_file = os.path.basename(self.path)

        self.entry_box.configure(state="normal")       #書き込み可に設定
        self.entry_box.delete(0,tk.END)                #初期化
        self.entry_box.insert(tk.END,selected_file)    #ファイル名を表示
        self.entry_box.configure(state="readonly")     #読み取り用に再設定

    def exchanging(self):
        m2m = Midi2Mcf(self.path)
        if not (m2m.file == None):
            try:
                m2m.exchange()
                messagebox.showinfo(title="complete",message="変換が完了しました")
            except:
                messagebox.showerror(title="format error",message="フォーマットが対応していない可能性があります")

if __name__ == "__main__":
    Application()