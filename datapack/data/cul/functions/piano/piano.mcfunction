#F#3
summon minecraft:interaction ~0.05 ~1.05 ~0.25 {Tags:["cul_fs3"]}
data modify entity @e[tag=cul_fs3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_fs3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_fs3] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_fs3"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_fs3,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]

#G3
summon minecraft:interaction ~ ~1 ~ {Tags:["cul_g3"]}
data modify entity @e[tag=cul_g3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_g3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_g3] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_g3"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_g3,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#G#3
summon minecraft:interaction ~-0.05 ~1.05 ~0.25 {Tags:["cul_gs3"]}
data modify entity @e[tag=cul_gs3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_gs3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_gs3] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_gs3"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_gs3,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#A3
summon minecraft:interaction ~-0.1 ~1 ~ {Tags:["cul_a3"]}
data modify entity @e[tag=cul_a3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_a3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_a3] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_a3"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_a3,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#A#3
summon minecraft:interaction ~-0.15 ~1.05 ~0.25 {Tags:["cul_as3"]}
data modify entity @e[tag=cul_as3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_as3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_as3] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_as3"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_as3,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#B3
summon minecraft:interaction ~-0.2 ~1 ~ {Tags:["cul_b3"]}
data modify entity @e[tag=cul_b3,limit=1] width set value 0.1f
data modify entity @e[tag=cul_b3,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_b3] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_b3"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_b3,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#C4
summon minecraft:interaction ~-0.3 ~1 ~ {Tags:["cul_c4"]}
data modify entity @e[tag=cul_c4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_c4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_c4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_c4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_c4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#C#4
summon minecraft:interaction ~-0.35 ~1.05 ~0.25 {Tags:["cul_cs4"]}
data modify entity @e[tag=cul_cs4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_cs4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_cs4] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_cs4"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_cs4,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#D4
summon minecraft:interaction ~-0.4 ~1 ~ {Tags:["cul_d4"]}
data modify entity @e[tag=cul_d4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_d4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_d4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_d4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_d4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]

#D#4
summon minecraft:interaction ~-0.45 ~1.05 ~0.25 {Tags:["cul_ds4"]}
data modify entity @e[tag=cul_ds4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_ds4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_ds4] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_ds4"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_ds4,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#E4
summon minecraft:interaction ~-0.5 ~1 ~ {Tags:["cul_e4"]}
data modify entity @e[tag=cul_e4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_e4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_e4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_e4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_e4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#F4
summon minecraft:interaction ~-0.6 ~1 ~ {Tags:["cul_f4"]}
data modify entity @e[tag=cul_f4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_f4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_f4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_f4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_f4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]



#F#4
summon minecraft:interaction ~-0.65 ~1.05 ~0.25 {Tags:["cul_fs4"]}
data modify entity @e[tag=cul_fs4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_fs4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_fs4] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_fs4"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_fs4,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]

#G4
summon minecraft:interaction ~-0.7 ~1 ~ {Tags:["cul_g4"]}
data modify entity @e[tag=cul_g4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_g4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_g4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_g4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_g4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#G#4
summon minecraft:interaction ~-0.75 ~1.05 ~0.25 {Tags:["cul_gs4"]}
data modify entity @e[tag=cul_gs4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_gs4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_gs4] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_gs4"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_gs4,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#A4
summon minecraft:interaction ~-0.8 ~1 ~ {Tags:["cul_a4"]}
data modify entity @e[tag=cul_a4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_a4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_a4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_a4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_a4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#A#4
summon minecraft:interaction ~-0.85 ~1.05 ~0.25 {Tags:["cul_as4"]}
data modify entity @e[tag=cul_as4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_as4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_as4] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_as4"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_as4,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#B4
summon minecraft:interaction ~-0.9 ~1 ~ {Tags:["cul_b4"]}
data modify entity @e[tag=cul_b4,limit=1] width set value 0.1f
data modify entity @e[tag=cul_b4,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_b4] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_b4"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_b4,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#C5
summon minecraft:interaction ~-1.0 ~1 ~ {Tags:["cul_c5"]}
data modify entity @e[tag=cul_c5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_c5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_c5] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_c5"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_c5,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#C#5
summon minecraft:interaction ~-1.05 ~1.05 ~0.25 {Tags:["cul_cs5"]}
data modify entity @e[tag=cul_cs5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_cs5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_cs5] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_cs5"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_cs5,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#D5
summon minecraft:interaction ~-1.1 ~1 ~ {Tags:["cul_d5"]}
data modify entity @e[tag=cul_d5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_d5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_d5] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_d5"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_d5,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]

#D#5
summon minecraft:interaction ~-1.15 ~1.05 ~0.25 {Tags:["cul_ds5"]}
data modify entity @e[tag=cul_ds5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_ds5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_ds5] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_ds5"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_ds5,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]


#E5
summon minecraft:interaction ~-1.2 ~1 ~ {Tags:["cul_e5"]}
data modify entity @e[tag=cul_e5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_e5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_e5] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_e5"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_e5,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]


#F5
summon minecraft:interaction ~-1.3 ~1 ~ {Tags:["cul_f5"]}
data modify entity @e[tag=cul_f5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_f5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_f5] run summon minecraft:block_display ~-0.05 ~ ~-0.05 {Tags:["cul_f5"],block_state:{Name:"white_concrete"}}
data modify entity @e[type=block_display,tag=cul_f5,limit=1] transformation.scale set value [0.095f,0.1f,0.5f]

#F#5
summon minecraft:interaction ~-1.35 ~1.05 ~0.25 {Tags:["cul_fs5"]}
data modify entity @e[tag=cul_fs5,limit=1] width set value 0.1f
data modify entity @e[tag=cul_fs5,limit=1] height set value 0.1f

execute at @e[type=interaction,tag=cul_fs5] run summon minecraft:block_display ~-0.025 ~ ~-0.05 {Tags:["cul_fs5"],block_state:{Name:"black_concrete"}}
data modify entity @e[type=block_display,tag=cul_fs5,limit=1] transformation.scale set value [0.05f,0.1f,0.25f]

