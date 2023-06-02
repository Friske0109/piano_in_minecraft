# piano_in_minecraft

--使い方--

datapack     : "datapack"を丸ごと、minecraftのsaves内の、datapacksフォルダに入れてください。
               ファイル名はわかりやすいものに変更してもらって構いません。
               
resourcepack : "resourcepack"を丸ごと、minecraftのreourcepacksフォルダに入れてください。
               こちらもファイル名は自由です。
               
２つとも入れたら、コマンドブロックに

execute positioned ~-1.15 ~0.8 ~0.3 run function cul:piano/new_piano

と入力して実行すると、コマンドブロックの２マス上にピアノが召喚されます。
各鍵盤を右クリックすることで音が鳴ります。

ピアノ音源を聞くには、先ほど入れたリソースパックを適用してください。
自分で演奏する場合はresourcepack
自動演奏する場合はresourcepack2
を適用してください。


--othersファイルについて--

othersファイルの中には、jsonを自動演奏コマンドに変換するツールが入っています。
ソースコードはぐちゃぐちゃですが、多分これから調整します。


↓ midiデータをjson形式に変換するにはこちらのサイトが便利です。
https://www.visipiano.com/midi-to-json-converter/






--USAGE--

datapack     : Put the whole "datapack" into the "datapacks" folder in the .minecraft/saves.
               You may rename the file to something more descriptive.
               
resourcepack : Put the whole "resourcepack" into the "resourcepacks" folder of .minecraft.
               You can name the files as you like.
               
Once both files are in there, add the following line to the command block

execute positioned ~-1.15 ~0.8 ~0.3 run function cul:piano/new_piano

and run it, a piano will be summoned two squares above the command block.
By right-clicking on each key, a sound will be played.

To hear the realistic piano sound, apply the resource pack that you just put in.
