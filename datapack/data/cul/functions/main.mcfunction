function cul:piano/piano_sound
function cul:piano/piano_animation

execute if score cul_kyu cul_piano matches 1.. run function cul:piano/music/kyu
execute if score cul_babel_f cul_piano matches 1.. run function cul:piano/music/babel_f