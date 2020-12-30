import pygame, random
import time
from propervalues import *
from Important import *
from Pokedex import *

pygame.init()

#載入開始畫面圖片

開始背景 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始背景.png')
開始遊戲 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始遊戲.png')
寶可夢圖鑑 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/寶可夢圖鑑.png')
開始畫面噴火龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始畫面噴火龍.png')
開始畫面噴火龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始畫面噴火龍2.png')
開始畫面急凍鳥 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始畫面急凍鳥.png')
開始畫面急凍鳥2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/開始畫面急凍鳥2.png')
pokemon = pygame.image.load('/Users/alanlin/Desktop/python final project/images/pokemon.png')
圖鑑背景 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/圖鑑背景.jpg')
選擇背景 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/選擇背景.png')
MENU = pygame.image.load('/Users/alanlin/Desktop/python final project/images/MENU.png')
桌子 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/桌子.png')
大木博士 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Oak.png')
選擇球 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/選擇球.png')
MENU2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/MENU2.png')
PLAY = pygame.image.load('/Users/alanlin/Desktop/python final project/images/PLAY.png')
寶可夢圖鑑2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/寶可夢圖鑑2.png')


#載入寶可夢圖片
噴火龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/噴火龍.png')
噴火龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/噴火龍2.png')
超夢 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/超夢.png')
超夢2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/超夢2.png')
九尾 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/九尾.png')
九尾2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/九尾2.png')
三頭草 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/三頭草.png')
三頭草2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/三頭草2.png')
水伊布 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水伊布.png')
水伊布2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水伊布2.png')
水箭龜 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水箭龜.png')
水箭龜2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水箭龜2.png')
水龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水龍.png')
水龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/水龍2.png')
火伊布 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/火伊布.png')
火伊布2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/火伊布2.png')
火焰鳥 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/火焰鳥.png')
火焰鳥2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/火焰鳥2.png')
卡比獸 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/卡比獸.png')
卡比獸2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/卡比獸2.png')
卡比獸 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/卡比獸.png')
皮卡丘 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/皮卡丘.png')
皮卡丘2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/皮卡丘2.png')
妙蛙花 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/妙蛙花.png')
妙蛙花2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/妙蛙花2.png')
急凍鳥 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/急凍鳥.png')
急凍鳥2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/急凍鳥2.png')
恐龍蝙蝠 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/恐龍蝙蝠.png')
恐龍蝙蝠2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/恐龍蝙蝠2.png')
疾風狗 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/疾風狗.png')
疾風狗2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/疾風狗2.png')
蚊香蛙 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/蚊香蛙.png')
蚊香蛙2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/蚊香蛙2.png')
馬腦水母 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/馬腦水母.png')
馬腦水母2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/馬腦水母2.png')
紫色龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/紫色龍.png')
紫色龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/紫色龍2.png')
暗貝殼 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/暗貝殼.png')
暗貝殼2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/暗貝殼2.png')
雷伊布 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/雷伊布.png')
雷伊布2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/雷伊布2.png')
雷電鳥 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/雷電鳥.png')
雷電鳥2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/雷電鳥2.png')
夢幻 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/夢幻.png')
夢幻2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/夢幻2.png')
豪力 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/豪力.png')
豪力2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/豪力2.png')
暴鯉龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/暴鯉龍.png')
暴鯉龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/暴鯉龍2.png')
戰鬥星星 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/戰鬥星星.png')
戰鬥星星2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/戰鬥星星2.png')
龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/龍.png')
龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/龍2.png')
藍色龍 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/藍色龍.png')
藍色龍2 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/藍色龍2.png')




#定義素材圖片

openball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/OpenPokeball.png')
square = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Square.png')
table = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Table.png')
oak = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Oak.png')
pokeball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Pokeball.png')
logo = pygame.image.load('/Users/alanlin/Desktop/python final project/images/PokemonLogo.png')
buton = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Button.png')
pressed = pygame.image.load('/Users/alanlin/Desktop/python final project/images/ButtonPressed.png')
rigid = pygame.image.load('/Users/alanlin/Desktop/python final project/images/RigidSquare.png')
buton2d = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Button2d.png')
hovered2d = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Button2dHover.png')
pressed2d = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Button2dPressed.png')

#定義聲音

dialgaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Dialga.wav")
raikouso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Raikou.wav")
gardevoirso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Gardevoir.wav")
gengarso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Gengar.wav")
electabuzzso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Electabuzz.wav")
tyranitarso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Tyranitar.wav")
dragoniteso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Dragonite.wav")
snorlaxso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Snorlax.wav")
machampso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Machamp.wav")
articunoso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Articuno.wav")
weezingso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Weezing.wav")
feraligatrso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Feraligatr.wav")
meganiumso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Meganium.wav")
rhydonso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Rhydon.wav")
mewtwoso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Mewtwo.wav")
arceusso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Arceus.wav")
charizardso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Charizard.wav")
darkraiso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Darkrai.wav")
greninjaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Greninja.wav")
laprasso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Lapras.wav")

#定義顏色

coffee_brown =((200,190,140))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))

#定義視窗

display_width = 1280
display_height = 760
FPS = 10

#定義整體變數

go = 0

#定義變數

font = pygame.font.Font('/Users/alanlin/Desktop/python final project/freesansbold.ttf', 25)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pokemon模擬戰鬥畫面')

def midscreen(pokeselected):
    quit = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load('/Users/alanlin/Desktop/python final project/Sound/page2.mp3')
    pygame.mixer.music.play(-1)

    k = 0
    z = 0
    back = 0
    but = 0
    selected = [-1, -1, -1, -1, -1, -1]
    total = 0
    goto = 0
    moveselected = 0 #技能
    dex = 0

    values = number(0, 27)#27隻

    while not quit:
        mouse = pygame.mouse.get_pos()#取得滑鼠座標
        for event in pygame.event.get():#事件檢索
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                
                #六顆球滑鼠位置取得               
                
                if 80 < mouse[0] < 179 and 120 < mouse[1] < 219 and k != 1:
                    moveselected = 0
                    k = 1
                    z = 1
                elif 230 < mouse[0] < 329 and 120 < mouse[1] < 219 and k != 2:
                    moveselected = 0
                    k = 2
                    z = 1
                elif 80 < mouse[0] < 179 and 275 < mouse[1] < 374 and k != 3:
                    moveselected = 0
                    k = 3
                    z = 1
                elif 230 < mouse[0] < 329 and 275 < mouse[1] < 374 and k != 4:
                    moveselected = 0
                    k = 4
                    z = 1
                elif 80 < mouse[0] < 179 and 430 < mouse[1] < 529 and k != 5:
                    moveselected = 0
                    k = 5
                    z = 1
                elif 230 < mouse[0] < 329 and 430 < mouse[1] < 529 and k != 6:
                    moveselected = 0
                    k = 6
                    z = 1

                    
                #MENU    
                elif 915 < mouse[0] < 1065 and 520 < mouse[1] < 595:
                    back = 1
                    quit = True
                #選擇寶可夢按鈕    
                elif 270 < mouse[0] < 369 and 600 < mouse[1] < 699 and k != 0 and total < 3 and selected[k - 1] < 0:
                    moveselected = 0
                    but = 1
                    selected[k - 1] = total
                    total = total + 1
                    k = 0
                
                #返回已選擇的寶可夢
                elif 940 < mouse[0] < 1039 and 630 < mouse[1] < 729:
                    i = 0
                    goto = 0
                    for elements in selected:
                        if elements >= 0:
                            selected[i] -= 1

                        i += 1
                        
                    total -= 1
                elif 1049 < mouse[0] < 1148 and 630 < mouse[1] < 729:
                    i = 0
                    goto = 0
                    for elements in selected:
                        if elements == 1:
                            selected[i] = -1
                        elif elements == 2:
                            selected[i] -= 1
                        i += 1

                    total -= 1
                elif 1158 < mouse[0] < 1257 and 630 < mouse[1] < 729:
                    i = 0
                    goto = 0
                    for elements in selected:
                        if elements == 2:
                            selected[i] = -1

                        i += 1

                    total -= 1

                #開始對戰按鈕    
                elif 1110 < mouse[0] < 1260 and 520 < mouse[1] < 595 and goto == 1:
                    goto = 2
                    
                #技能按鈕    
                elif 930 < mouse[0] < 1260 and 60 < mouse[1] < 160 and k != 0:
                    moveselected = 1
                elif 930 < mouse[0] < 1260 and 180 < mouse[1] < 280 and k != 0:
                    moveselected = 2
                elif 930 < mouse[0] < 1260 and 300 < mouse[1] < 400 and k != 0:
                    moveselected = 3
                elif 930 < mouse[0] < 1260 and 420 < mouse[1] < 520 and k != 0:
                    moveselected = 4
                    
                #進入pokedex     
                elif 470 < mouse[0] < 770 and 600 < mouse[1] < 675 and k != 0 and selected[k - 1] < 0:
                    Pokedex(values[k - 1], 1)

                    
        if total == 3 and goto != 2:
            goto = 1
        #背景
        image(選擇背景, 0, 0)
        image(選擇球, 0, 0)
        image(MENU2, 915, 520)
    
        #選擇寶可夢的三個框線
        image(rigid, 940, 630)
        image(rigid, 1049, 630)
        image(rigid, 1158, 630)

        #技能設定
        button(" MOVES ", 1040, 10, white, white, 0, 0, 0, 0, green, green)
        
        if k != 0 and selected[k - 1] < 0:
            if z == 1:
                sound1(poke[int(values[k - 1])].music)
                z = 0
                
            #寶可夢圖像和名稱    
            poke[int(values[k - 1])].draw(430, 150)
            button(" %s " % poke[int(values[k - 1])].name, 570, 100, white, white, 0, 0, 0, 0, black, black)
            
            
            #屬性位置
            a = 500
            b = 545

            
            for types in poke[int(values[k - 1])].type:
                button(type[types - 1].name, a  + 10, b + 10, type[types - 1].textcolor, type[types - 1].textcolor, a, b, 120, 50, type[types - 1].color, type[types - 1].color) 
                a = a + 130
            
            
            #技能解釋
            a = 0
            b = 60
            
            while a < 4:
                button(" %s => PP: %s " % ( poke[int(values[k - 1])].move[a], move[poke[int(values[k - 1])].move[a]].pp ), 940, b + 10, move[poke[int(values[k - 1])].move[a]].textcolor, move[poke[int(values[k - 1])].move[a]].color, 930, b, 330, 100, move[poke[int(values[k - 1])].move[a]].color, move[poke[int(values[k - 1])].move[a]].textcolor)
                b = b + 120
                a = a + 1

            image(寶可夢圖鑑2, 470, 600)

        if moveselected != 0:
            a = poke[int(values[k - 1])].move[moveselected - 1]
            b = 60 + 120 * (moveselected - 1)

            button("", 940, b + 10, move[a].textcolor, move[a].textcolor, 930, b, 330, 100, move[a].color, move[a].color)
            writes("Power: %s" % (move[a].damage), move[a].textcolor, 940, b + 10, 20)
            writes("Accuracy: %s" % (move[a].accuracy), move[a].textcolor, 940, b + 40, 20)
            writes("Heal: %s" % (move[a].heal), move[a].textcolor, 940, b + 70, 20)



        for yes in selected:
            if yes == 0:
                image(pokeball, 940, 630)
            elif yes == 1:
                image(pokeball, 1049, 630)
            elif yes == 2:
                image(pokeball, 1158, 630)



        if but == 0:
            image(buton, 270, 600)
            writes("Select", white, 295, 620, 18)
        elif but == 1:
            image(pressed, 276, 606)
            but = 0

        if goto == 0:
            image(PLAY, 1110, 520)
        elif goto == 1:
            image(PLAY, 1110, 520)
            message("Tap To Play", white, 1125, 605)
        elif goto == 2:
            image(PLAY, 1110, 520)
            for i in range(0, 6):
                if selected[i] == 0:
                    pokeselected.append(int(values[i]))

            for i in range(0, 6):
                if selected[i] == 1:
                    pokeselected.append(int(values[i]))


            for i in range(0, 6):
                if selected[i] == 2:
                    pokeselected.append(int(values[i]))

            quit = True
            back = 2
            goto = 1

        if k == 1 and selected[0] < 0:
            image(openball, 60, 69)
        elif selected[0] < 0:
            pokechange(pokeball, square, 80, 120, 99, 99)

        if k == 2 and selected[1] < 0:
            image(openball, 210, 69)
        elif  selected[1] < 0:
            pokechange(pokeball, square, 230, 120, 99, 99)

        if k == 3 and selected[2] < 0:
            image(openball, 60, 224)
        elif selected[2] < 0:
            pokechange(pokeball, square, 80, 275, 99, 99)

        if k == 4 and selected[3] < 0:
            image(openball, 210, 224)
        elif selected[3] < 0:
            pokechange(pokeball, square, 230, 275, 99, 99)

        if k == 5 and selected[4] < 0:
            image(openball, 60, 379)
        elif selected[4] < 0:
            pokechange(pokeball, square, 80, 430, 99, 99)

        if k == 6 and selected[5] < 0:
            image(openball, 210, 379)
        elif selected[5] < 0:
            pokechange(pokeball, square, 230, 430, 99, 99)
    

        pygame.display.update()

    return back
