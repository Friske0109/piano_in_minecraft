import json

trackname = "babel_f"
bpm = 225
mul = 8.0

tps = 20*(bpm/150)

file = open(trackname + ".json", "r")
output_file = open(trackname + ".mcfunction", "w")
table = open("table2.json")
json_l = json.load(file)
json_table = json.load(table)

output_file.write("scoreboard players add cul_" + trackname + " cul_piano 1\n")
#output_file.write("execute if score cul_" + trackname + " cul_piano matches 1 run tps " + str(round(tps, 1)) + "\n")

for i in range(16):
    if json_l['tracks'][i]['notes'] != []:
        track_note = json_l['tracks'][i]['notes']
        for note in track_note:
            note_name = str(note["name"]).lower().replace('#', 's')
            note_midi = note["midi"]
            timestamp = str(int(note["time"] * mul))
            velocity = str((note["velocity"] ** 1.2) * 11/(((note_midi%12)**2)/12+11))
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
                    output_file.write("execute if score cul_" + trackname + " cul_piano matches " + timestamp + " run scoreboard players set cul_" + note_name + "_ani cul_piano " + animation_time + "\n")
                    output_file.write("execute if score cul_" + trackname + " cul_piano matches " + timestamp + " run playsound minecraft:block." + inst + " master @a ~ ~ ~ " + velocity + " " + value + "\n")
            
        
file.close()
output_file.close()
table.close()
