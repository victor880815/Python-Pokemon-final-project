import pygame, time
from propervalues import *
from Important import *

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
圖鑑背景 = pygame.image.load('/Users/alanlin/Desktop/python final project/images/圖鑑背景.png')
NEXT = pygame.image.load('/Users/alanlin/Desktop/python final project/images/NEXT.png')
MENU = pygame.image.load('/Users/alanlin/Desktop/python final project/images/MENU.png')
BACK = pygame.image.load('/Users/alanlin/Desktop/python final project/images/BACK.png')

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



#defining move images

hand = pygame.image.load('/Users/alanlin/Desktop/python final project/images/ChopHand.png')

#defining other images

openball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/OpenPokeball.png')
square = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Square.png')
table = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Table.png')
oak = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Oak.png')
pokeball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Pokeball.png')
logo = pygame.image.load('/Users/alanlin/Desktop/python final project/images/PokemonLogo.png')
dexback = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Pokedexback.jpg')


#定義寶可夢聲音

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
infernapeso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Infernape.wav")
giratinaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Giratina.wav")
palkiaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Palkia.wav")
shayminso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Shaymin.wav")
bisharpso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Bisharp.wav")
electivireso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Electivire.wav")
lugiaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Lugia.wav")


#定義顏色

coffee_brown =((200,190,140))
forest_green = ((0,50,0))
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
navy_blue = ((0,0,100))
imageremoval = (0, 0, 0, 0)

#定義視窗
display_width = 1280
display_height = 760
FPS = 10

#定義變數

go = 0

#定義字體、視窗
font = pygame.font.Font('/Users/alanlin/Desktop/python final project/微軟正黑體.ttf', 25)

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Pokemon模擬戰鬥畫面')

transparent = pygame.Surface((1280, 750))
transparent.set_alpha(0)#圖像值

def Pokedex(pokeindex, val):
    ind = pokeindex

    quit = 0

    while not quit:
        mouse = pygame.mouse.get_pos();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 1060 < mouse[0] < 1260 and 630 < mouse[1] < 690: #下一頁按鈕
                    ind = (ind + 1) % 26
                elif 1080 < mouse[0] < 1270 and 5 < mouse[1] < 65: 
                    quit = 2

        if val == 1:
            image(圖鑑背景, 0, 0)
            gameDisplay.blit(transparent, (0, 0))
            
        else:
            image(圖鑑背景, 0, 0)               
               
                    
        image(BACK, 1080, 5)
        poke[int(ind)].draw(250, 150) #定義寶可夢圖片位置
        button(" %s " % poke[int(ind)].name, 370, 100, white, white, 0, 0, 0, 0, black, black)

        
        #定義屬性位置
        a = 300 
        b = 600

        for types in poke[int(ind)].type:  #字的位置              #-1為了保持迴圈                                   #底的長寬
            button(type[types - 1].name, a  + 10, b + 10, type[types - 1].textcolor, type[types - 1].textcolor, a, b, 120,
                   50,type[types - 1].color, type[types - 1].color,) 
            a = a + 130 #定義type2屬性位置


            
        writes("Stats", white, 920, 175, 50)

        writes("Attack ", red, 700, 275, 35)
        writes("Defence ", blue, 700, 350, 35)
        writes("Speed ", green, 700, 425, 35)

        att = poke[int(ind)].attack
        defe = poke[int(ind)].defence
        sp = poke[int(ind)].speed
                                                                #數值條的長寬
        button(" %s " % att, 890, 280, white, white, 880, 275, int((att / 154) * 300), 40, red, red)
        button(" %s " % defe, 890, 355, white, white, 880, 350, int((defe / 154) * 300), 40, blue, blue)
        button(" %s " % sp, 890, 430, white, white, 880, 425, int((sp / 154) * 300), 40, green, green)
 
                              #按之前字顏色#按之後               #按之前底顏色#按之後
        button("", 1140, 650, white, black, 1060, 630, 200, 60, red, white)
        writes("NEXT", black, 1110, 645, 35)

        pygame.display.update()

    return (quit - 1)
