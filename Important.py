import pygame, time
from propervalues import *

pygame.init()

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



hand = pygame.image.load('/Users/alanlin/Desktop/python final project/images/ChopHand.png')



openball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/OpenPokeball.png')
square = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Square.png')
table = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Table.png')
oak = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Oak.png')
pokeball = pygame.image.load('/Users/alanlin/Desktop/python final project/images/Pokeball.png')
logo = pygame.image.load('/Users/alanlin/Desktop/python final project/images/PokemonLogo.png')

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
infernapeso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Infernape.wav")
giratinaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Giratina.wav")
palkiaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Palkia.wav")
shayminso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Shaymin.wav")
bisharpso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Bisharp.wav")
electivireso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Electivire.wav")
lugiaso = pygame.mixer.Sound("/Users/alanlin/Desktop/python final project/Sound/Lugia.wav")

#defining colors

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


font = pygame.font.Font('/Users/alanlin/Desktop/python final project/freesansbold.ttf', 25)
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Pokemon模擬戰鬥畫面')

class Pokemon():
    def __init__(self, name, type, move1, move2, move3, move4, picture, picture2, sound, width, height, weakness, strenghts, hp, attack, defence, speed):
	    self.type = type
	    self.name = name
	    self.move = []
	    self.move.append(move1)
	    self.move.append(move2)
	    self.move.append(move3)
	    self.move.append(move4)
	    self.image = picture
	    self.image2 = picture2
	    self.weakness = weakness
	    self.music = sound
	    self.width = width
	    self.height = height
	    self.strenghts = strenghts
	    self.hp = hp
	    self.attack = attack
	    self.defence = defence
	    self.speed = speed
		
    def draw(self, x, y):
	    image(self.image, x, y)
		
    def healthp(self, iv):
	    health = int(2 * self.hp + 2  * iv + 100 + 5)
	    return health
		
    def stats(self, iv):
	    rand = int((random.randrange(85, 100) / 1.0) * 1.0)
	    rand = rand / 100
	
	    mattack = int((2 * self.attack + 2 * iv) * rand + 5)
	    mdefence = int(2 * self.defence + 2 * iv + 5)
	    mspeed = int(2 * self.speed +  2 * iv + 5)
		
	    stat = [mattack, mdefence, mspeed]
	    return stat
		
		
#定義戰鬥時寶可夢數值
poke = [  Pokemon("Venusaur", [5, 8],  "Razor Leaf", "Sludge Bomb", "Seed Flare", "Energy Ball", 妙蛙花, 妙蛙花2, charizardso, 400, 400, [2, 6, 10, 11], [3, 4, 5, 7, 18], 80, 82, 83, 80) 
		, Pokemon("Charizard" ,[2, 10], "Flamethrower", "Aerial Ace", "Fire Blast", "Overheat", 噴火龍, 噴火龍2, arceusso, 400, 400, [3, 4, 13], [2, 5, 7, 12, 17, 18], 78, 84, 78, 100)
		, Pokemon("Blastoise", [3], "Hydro Pump", "Surf", "Ice Beam", "Ice Fang", 水箭龜, 水箭龜2, greninjaso, 400, 400, [4, 5], [2, 3, 6, 17], 79, 83, 100, 78)
		, Pokemon("Nidoqueen", [8, 9], "Earthquake", "Sludge Bomb", "Smog", "Explosion", 藍色龍, 藍色龍2, darkraiso, 400, 400, [3, 6, 9, 11], [4, 7, 8, 12, 13], 90, 92, 87, 76)
		, Pokemon("Nidoking", [8, 9], "Earthquake", "Sludge Bomb", "Smog", "Explosion", 紫色龍, 紫色龍2, charizardso, 400, 400, [3, 6, 9, 11], [4, 7, 8, 12, 13], 81, 102, 77, 85)
		, Pokemon("Ninetales", [2], "Flamethrower", "Flare Blitz", "Fire Punch", "Overheat", 九尾, 九尾2, laprasso, 400, 400, [3, 9, 13], [2, 5, 6, 12, 17, 18], 73, 76, 75, 100)
		, Pokemon("Arcanine", [2], "Flamethrower", "Flare Blitz", "Fire Punch", "Overheat", 疾風狗, 疾風狗2, meganiumso, 400, 400, [3, 9, 13], [2, 5, 6, 12, 17, 18], 90, 110, 80, 95)
		, Pokemon("Poliwrath", [3, 7], "Hydro Pump", "Surf", "Focus Blast", "Cross Chop", 蚊香蛙, 蚊香蛙2, rhydonso, 400, 400, [4, 5, 10, 11, 18], [2, 3, 6, 12, 13, 16, 17], 90, 95, 95, 70)
		, Pokemon("Machamp", [7], "Cross Chop", "Submission", "Rock Slide", "Karate Chop", 豪力, 豪力2, machampso, 400, 400, [7, 11, 18], [12, 13, 16], 90, 130, 80, 55)
		, Pokemon("Tentacruel", [3, 8], "Sludge Bomb", "Hydro Pump", "Surf", "Smog", 馬腦水母, 馬腦水母2, feraligatrso, 400, 400, [4, 9, 11], [2, 3, 6, 7, 8, 12, 17, 18], 80, 70, 65, 100)
		, Pokemon("Cloyster", [3, 6], "Hydro Pump", "Surf", "Ice Fang", "Ice Beam", 暗貝殼, 暗貝殼2, machampso, 400, 400, [4, 5, 7, 13], [3, 6], 50, 95, 180, 70)
		, Pokemon("Exeggutor", [5, 11], "Synthesis", "Magical Leaf", "Psychic", "Psycho Cut", 三頭草, 三頭草2, articunoso, 400, 400, [2, 6, 8, 10, 12, 14, 16], [3, 4, 5, 7, 9, 11], 95, 95, 85, 55)
		, Pokemon("Starmie", [3, 11], "Hydro Pump", "Surf", "Psycho Cut", "Psychic", 戰鬥星星, 戰鬥星星2, snorlaxso, 400, 400, [4, 5, 12, 14, 16], [2, 3, 6, 7, 11, 17], 60, 75, 85, 115)
		, Pokemon("Gyarados", [3, 10], "Hydro Pump", "Surf", "Sky Attack", "Aerial Ace", 暴鯉龍, 暴鯉龍2, dragoniteso, 400, 400, [4, 13], [2, 3, 7, 9, 12, 17], 95, 125, 79, 81)
		, Pokemon("Lapras", [3, 6], "Ice Beam", "Blizzard", "Surf", "Psychic", 水龍, 水龍2, laprasso, 400, 400, [4, 5, 7, 13], [3, 6], 130, 85, 80, 60)
		, Pokemon("Vaporeon", [3], "Hydro Pump", "Surf", "Ice Beam", "Body Slam", 水伊布, 水伊布2, electabuzzso, 400, 400, [4, 5], [2, 3, 6, 17], 130, 65, 60, 65)
		, Pokemon("Jolteon", [4], "Thunder Bolt", "Thunder", "Shock Wave", "Body Slam", 雷伊布, 雷伊布2, gardevoirso, 400, 400, [9], [4, 10, 17], 65, 65, 60, 130)
		, Pokemon("Flareon", [2], "Overheat", "Fire Blast", "Fire Punch", "Flamethrower", 火伊布, 火伊布2, gengarso, 400, 400, [3, 9, 13], [2, 5, 6, 12, 17, 18], 65, 130, 60, 65)
		, Pokemon("Aerodactyl", [13, 10], "Ancient Power", "Sky Attack", "Aerial Ace", "Rock Slide", 恐龍蝙蝠, 恐龍蝙蝠2, dialgaso, 400, 400, [3, 4, 6, 13, 17], [1, 2, 8, 10, 12], 80, 105, 65, 130)
		, Pokemon("Snorlax", [1], "Body Slam", "Thunder Bolt", "Rock Slide", "Hyper Beam", 卡比獸, 卡比獸2, snorlaxso, 400, 400, [7], [14], 160, 110, 65, 30)
		, Pokemon("Articuno", [6, 10], "Ice Beam", "Blizzard", "Aerial Ace", "Recover", 急凍鳥, 急凍鳥2, articunoso, 400, 400, [2, 4, 13, 17], [5, 9, 12], 90, 85, 100, 85)
		, Pokemon("Zapdos", [4, 10], "Thunder Bolt", "Thunder", "Sky Attack", "Shock Wave", 雷電鳥, 雷電鳥2, giratinaso, 400, 400, [6, 13], [5, 7, 9, 10, 12, 17], 90, 90, 85, 100)
		, Pokemon("Moltres", [2, 10], "Overheat", "Sky Attack", "Flare Blitz", "Fire Blast", 火焰鳥, 火焰鳥2, palkiaso, 400, 400, [3, 4 ,13], [2, 5, 7, 12, 17, 18], 90, 100, 90, 90)
		, Pokemon("Dragonite", [10, 15], "Aerial Ace", "Outrage", "Thunder Bolt", "Hyper Beam", 龍, 龍2, dragoniteso, 400, 400, [6, 13, 15, 18], [2, 3, 5, 7, 9, 12], 91, 134, 95, 80)
		, Pokemon("Mewtwo", [11],  "Psychic", "Recover", "Aerial Ace", "Shadow Ball", 超夢, 超夢2, mewtwoso, 400, 400, [12, 14, 16], [7, 11], 106, 110, 90, 130)
		, Pokemon("Mew", [11], "Psychic", "Recover", "Aerial Ace", "Shadow Ball", 夢幻, 夢幻2, electivireso, 400, 400, [12, 14, 16], [7, 11], 100, 100, 100, 100)
		, Pokemon("Pikachu", [4], "Shock Wave", "Thunder", "Thunder Bolt", "Giga Impact", 皮卡丘, 皮卡丘2, lugiaso, 400, 400, [9], [4, 10, 17], 35, 55, 40, 90)
		]


		
class Moves():
    def __init__(self, type, color, textcolor, damage, heal, accuracy, powerpoints, sleep, paralyze):
	    self.type = type
	    self.textcolor = textcolor
	    self.color = color
	    self.damage = damage
	    self.heal = heal
	    self.accuracy = accuracy
	    self.pp = powerpoints
	    self.sleep = sleep
	    self.paralyze = paralyze
		
    def animation(self, x, y):
	    image(self.picture, x, y)
		
    def willhit(self):
	    accu = int((random.randrange(1, 101) / 1.0) * 1.0)
		
	    if accu <= self.accuracy:
		    return 1
	    else:
		    return 0
        
        
                    #定義戰鬥血量及死亡
    def animating(self, name, player):
        if name == "karate chop":
            if player == 1:
                i = 0
                j = 410

                while i < 230:
            	    image(hand, i, j)
            	    hand.fill(imageremoval)

            	    i += 1
            	    clock.tick(100)
            if player == 2:
                i = 790
                j = 180

                while i < 1020:
            	    image(hand, i, j)
            	    hand.fill(imageremoval)

            	    i += 1
            	    clock.tick(100)

        

 #定義技能                   
move =  {  "Psychic":Moves([11], purple, black, 120, 0, 100, 10, 0, 0)
		 , "Recover":Moves([1], brown, white, 0, 190, 100, 20, 0, 0)
		 , "Swift":Moves([1], brown, white, 60, 0, -1, 25, 0, 0)
		 , "Psycho Cut":Moves([11], purple, black, 80, 0, 100, 10, 0, 0)
		 , "Judgement":Moves([1], brown, white, 100, 0, 100, 5, 0, 0)
		 , "Overheat":Moves([2], orange, white, 140, 0, 75, 5, 0, 0)
		 , "Shadow Ball":Moves([14], purple, white, 80, 0, 100, 15, 0, 0)
		 , "Hydro Pump":Moves([3], blue, white, 140, 0, 75, 5, 0, 0)
		 , "Surf":Moves([3], blue, white, 80, 0, 100, 15, 0, 0)
		 , "Cross Chop":Moves([7], red, black, 140, 0, 75, 5, 0, 0)
		 , "Dark Void":Moves([16], black, white, 0, 0, 75, 20, 1, 0)
		 , "Dream Eater":Moves([11], purple, black, 100, 0, 100, 15, 2, 0)
		 , "Dark Pulse":Moves([16], black, white, 80, 0, 100, 15, 0, 0)
		 , "Flamethrower":Moves([2], orange, white, 90, 0, 100, 10, 0, 0)
		 , "Aerial Ace":Moves([10], white, blue, 80, 0, -1, 15, 0, 0)
		 , "Fire Blast":Moves([2], orange, white, 140, 0, 75, 5, 0, 0)
		 , "Ice Beam":Moves([6], navy_blue, blue, 90, 0, 100, 10, 0, 0)
		 , "Blizzard":Moves([6], navy_blue, blue, 140, 0, 100, 5, 0, 0)
		 , "Magical Leaf":Moves([5], forest_green, white, 80, 0, -1, 25, 0, 0)
		 , "Synthesis":Moves([5], forest_green, white, 0, 190, 100, 5, 0, 0)
		 , "Razor Leaf":Moves([5], forest_green, white, 80, 0, 90, 20, 0, 0)
		 , "Hyper Beam":Moves([1], brown, white, 160, 0, 100, 5, 0, 0)
		 , "Horn Drill":Moves([5], yellow, green, 220, 0, 50, 5, 0, 0)
		 , "Megahorn":Moves([5], yellow, green, 100, 0, 100, 10, 0, 0)
		 , "Earthquake":Moves([9], coffee_brown, brown, 100, 0, 100, 10, 0, 0)
		 , "Sludge Bomb":Moves([8], marroon, purple, 80, 0, 100, 10, 0, 0)
		 , "Smog":Moves([8], marroon, purple, 40, 0, 100, 20, 0, 0)
		 , "Explosion":Moves([1], brown, white, 200, 0, 100, 10, 0, 0)
		 , "Tackle":Moves([1], brown, white, 40, 0, 90, 20, 0, 0)
		 , "Ice Fang":Moves([6], navy_blue, blue, 80, 0, 100, 15, 0, 0)
		 , "Submission":Moves([7], red, black, 80, 0, 100, 10, 0, 0)
		 , "Rock Slide":Moves([13], coffee_brown, black, 80, 0, 90, 10, 0, 0)
		 , "Karate Chop":Moves([7], red, black, 40, 0, -1, 20, 0, 0)
		 , "Body Slam":Moves([1], brown, white, 80, 0, 75, 20, 0, 0)
		 , "Thunder Bolt":Moves([4], yellow, black, 80, 0, 100, 15, 0, 0)
		 , "Outrage":Moves([15], red, yellow, 100, 0, 100, 10, 0, 0)
		 , "Crunch":Moves([14], purple, white, 100, 0, 100, 10, 0, 0)
		 , "Thunder":Moves([4], yellow, black, 140, 0, 75, 5, 0, 0)
		 , "Shock Wave":Moves([4], yellow, black, 60, 0, -1, 15, 0, 0)
		 , "Hypnosis":Moves([11], purple, black, 0, 0, 75, 10, 1, 0)
		 , "Shadow Punch":Moves([14], purple, white, 60, 0, -1, 15, 0, 0)
		 , "Roar Of Time":Moves([15], red, yellow, 150, 0, 90, 5, 0, 0)
		 , "Dragon Rush":Moves([15], red, yellow, 100, 0, 85, 10, 0, 0)
		 , "Ancient Power":Moves([13], coffee_brown, black, 60, 0, 100, 5, 0, 0)
		 , "Extrasensory":Moves([11], purple, black, 80, 0, 100, 20, 0, 0)
		 , "Signal Beam":Moves([12], yellow, green, 75, 0, 100, 20, 0, 0)
		 , "Flare Blitz":Moves([2], orange, white, 120, 0, 100, 5, 0, 0)
		 , "Close Combat":Moves([7], red, black, 120, 0, 85, 5, 0, 0)
		 , "Shadow Force":Moves([14], purple, white, 120, 0, 100, 5, 0, 0)
		 , "Draco Meteor":Moves([15], red, yellow, 130, 0, 85, 5, 0, 0)
		 , "Spacial Rend":Moves([15], red, yellow, 100, 0, 100, 5, 0, 0)
		 , "Seed Flare":Moves([5], forest_green, white, 120, 0, 85, 5, 0, 0)
		 , "Energy Ball":Moves([5], forest_green, white, 100, 0, 100, 10, 0, 0)
		 , "Focus Blast":Moves([7], red, black, 120, 0, 85, 5, 0, 0)
		 , "Guillotine":Moves([1], brown, white, 200, 0, 30, 5, 0, 0)
		 , "Iron Head":Moves([17], black, lime, 80, 0, 100, 10, 0, 0)
		 , "Giga Impact":Moves([1], brown, white, 140, 0, 100, 5, 0, 0)
		 , "Fire Punch":Moves([2], orange, white, 80, 0, 100, 20, 0, 0)
		 , "Sky Attack":Moves([10], white, blue, 130, 0, 100, 5, 0, 0)
		}
		
class Type():
    def __init__(self, name, color, textcolor):
	    self.color = color
	    self.textcolor = textcolor
	    self.name = name
		

type = [  Type("Normal", brown, white)#1
		, Type("Fire", orange, white)#2
		, Type("Water", blue, white)#3
		, Type("Electric", yellow, black)#4
		, Type("Grass", forest_green, white)#5
		, Type("Ice", navy_blue, blue)#6
		, Type("Fighting", red, black)#7
		, Type("Poison", marroon, white)#8
		, Type("Ground", coffee_brown, brown)#9
		, Type("Flying", white, blue)#10
		, Type("Psychic", purple, black)#11
		, Type("Bug", yellow, green)#12
		, Type("Rock", coffee_brown, black)#13
		, Type("Ghost", purple, white)#14
		, Type("Dragon", red, yellow)#15
		, Type("Dark", black, white)#16
		, Type("Steel", black, lime)#17
		, Type("Fairy", pink, white)#18
	   ]


#定義攻擊動畫
class SpriteSheet(object):
    def __init__(self, file_name, x, y, fram, row, col):
	    self.sprite_sheet = pygame.image.load(file_name).convert()
	    self.height = x
	    self.width = y
	    self.fram = fram
	    self.row = row
	    self.col = col

    def get_image(self, num):
	    image = pygame.Surface([self.width, self.height]).convert()#設定螢幕為白紙概念

	    y = int(num / self.col) * self.height    #控制png檔中的位子
	    x = num % self.col * self.width   

 
	    image.blit(self.sprite_sheet, (-20, -20), (x, y, self.width, self.height))#控制傷害動畫位置#繪圖
 
	    image.set_colorkey(black)
 
	    return image


#攻擊動畫編輯                                                                                                  #長度＃寬度＃動畫幀數         
sprit = [  SpriteSheet("/Users/alanlin/Desktop/python final project/images/Explosion.png", 130, 130, 42, 7, 6)
		 , SpriteSheet("/Users/alanlin/Desktop/python final project/images/Thunderbolt.png", 403, 148, 10, 1, 10)
		]

