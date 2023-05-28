import json

trackname = "babel_f"
bpm = 225

tps = 20*(bpm/150)

file = open(trackname + ".json", "r")
output_file = open(trackname + ".mcfunction", "w")
table = open("table.json")
json_l = json.load(file)
json_table = json.load(table)

output_file.write("scoreboard players add cul_" + trackname + " cul_piano 1\n")
output_file.write("execute if score cul_" + trackname + " cul_piano matches 1 run tps " + str(round(tps, 1)) + "\n")

for i in range(16):
    if json_l['tracks'][i]['notes'] != []:
        track_note = json_l['tracks'][i]['notes']
        for note in track_note:
            note_name = str(note["name"]).lower().replace('#', 's')
            note_midi = str(note["midi"])
            timestamp = str(int(note["time"] * 8.0))
            velocity = str(note["velocity"])
            for tb in range(88):
                if str(json_table["table"][tb]["midi"]) == note_midi:
                    inst = str(json_table["table"][tb]["inst"])
                    value = str(json_table["table"][tb]["value"])
                    output_file.write("execute if score cul_" + trackname + " cul_piano matches " + timestamp + " run scoreboard players set cul_" + note_name + "_ani cul_piano 5\n")
                    output_file.write("execute if score cul_" + trackname + " cul_piano matches " + timestamp + " run playsound minecraft:block.note_block." + inst + " master @p ~ ~ ~ " + velocity + " " + value + "\n")
            
        
file.close()
output_file.close()
table.close()
