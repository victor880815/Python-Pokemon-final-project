#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
import tkinter as tk
import tkinter.ttk as ttk
import PIL
from PIL import ImageTk, Image, ImageSequence
import time
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
passwd="xu31i65p4",
database="new_schema"
)

#設定主視窗
root = tk.Tk()
root.title('保可夢戰鬥圖鑑')
root.geometry("1280x700")
root.resizable(width=True, height=True)

#子視窗背景建立路徑
path2 = '子視窗背景.jpg'
img2 = ImageTk.PhotoImage(Image.open(path2))

#子視窗'橫幅圖片'建立路徑
path3 = '橫幅.png'
img3 = ImageTk.PhotoImage(Image.open(path3))

#子視窗'Pokemon圖片'建立路徑
path4 = 'Pokemon.png'
img4 = ImageTk.PhotoImage(Image.open(path4))

#子視窗'搜尋按鈕圖片'建立路徑
path5 = '搜尋按鈕圖片.png'
img5 = ImageTk.PhotoImage(Image.open(path5))

#圖鑑圖片

pic=[ImageTk.PhotoImage(Image.open('%s.png'%(i))) for i in range(1,152)]
pho=ImageTk.PhotoImage(Image.open('框.png'))

#定義子視窗
def second_win():
    top = tk.Toplevel()
    top.title('保可夢戰鬥圖鑑')
    top.geometry("1280x753")
    
    
    #子視窗背景
    canvas2 = tk.Canvas(top, width=1800,height=1100,bd=0, highlightthickness=0)
    canvas2.create_image(750, 365, image=img2)
    canvas2.pack()
    
    
    
    #輸入寶可夢entry建立
    entry = tk.Entry(top, insertbackground='blue', highlightthickness =2)
    entry.pack()
    canvas2.create_window(650, 200, width=200, height=40,
                                       window=entry)
    
    #子視窗圖片1
    
    panel = tk.Label(top, image = img3) 
    panel.pack(side = "top", fill = "both", expand = "yes")

    canvas2.create_window(640, 85, width=1300, height=170,
                          window=panel)
    
    #子視窗圖片2
    
    panel2 = tk.Label(top, image = img4) 
    panel2.pack(side = "top", fill = "both", expand = "yes") 

    canvas2.create_window(485, 200, width=120, height=45,
                          window=panel2)
    
    #搜尋結果取代 函數
    def search():
        cursor=db.cursor()
        sql="select chinese_name,type_1,type_2,total_points,hp,attack,defense,sp_attack,sp_defense,speed,introduce,pokedex_number,number from pokemon where chinese_name=%s"
        cursor.execute(sql,(entry.get(),))
        results=cursor.fetchall()
        for row in results:
            name=row[0]
            type1=row[1]
            type2=row[2]
            total_points=row[3]
            hp=row[4]
            attack=row[5]
            defense=row[6]
            sp_attack=row[7]
            sp_defense=row[8]
            speed=row[9]
            introduce=row[10]
            pokedex_number=row[11]
            number=row[12]
        
        lblnumber.configure(text='圖鑑編號:'+pokedex_number)
        lblname.configure(text='名稱:'+name)
        lbltype1.configure(text='屬性1:'+type1)
        lbltype2.configure(text='屬性2:'+type2)
        lbltp.configure(text='總戰鬥力:'+total_points)
        lblhp.configure(text='血量:'+hp)
        lblatk.configure(text='攻擊力:'+attack)
        lbldfs.configure(text='防禦力:'+defense)
        lblspatk.configure(text='特攻:'+sp_attack)
        lblspdfs.configure(text='特防:'+sp_defense)
        lblspd.configure(text='速度:'+speed)
        lblint.configure(text='簡介:'+introduce)
        lblpicture.configure(image=pic[number-1])
        
    #搜尋按鈕
    
    searchbutton = tk.Button(top, command=search, cursor='hand2', image = img5, bd=0) 
    searchbutton.pack(side = "top", fill = "both", expand = "yes") 

    canvas2.create_window(780, 200, width=49, height=48,
                          window=searchbutton)
    
    #輸入寶可夢combo建立
    combo = ttk.Combobox(top,value = ['妙蛙種子','妙蛙草','妙蛙花','小火龍','火恐龍','噴火龍','傑尼龜','卡咪龜','水箭龜','綠毛蟲','鐵甲蛹','巴大蝶','獨角蟲','鐵殼蛹','大針蜂','波波','比比鳥','大比鳥','小拉達','拉達','烈雀','大嘴雀','阿柏蛇','阿柏怪','皮卡丘','雷丘','穿山鼠','穿山王','尼多蘭','尼多娜','尼多后','尼多朗','尼多力諾','尼多王','皮皮','皮可西','六尾','九尾','胖丁','胖可丁','超音蝠','大嘴蝠','走路草','臭臭花','霸王花','派拉斯','派拉斯特','毛球','摩魯蛾','地鼠','三地鼠','喵喵','貓老大','可達鴨','哥達鴨','猴怪','火爆猴','卡蒂狗','風速狗','蚊香蝌蚪','蚊香君','蚊香泳士','凱西','勇基拉','胡地','腕力','豪力','怪力','喇叭芽','口呆花','大食花','瑪瑙水母','毒刺水母','小拳石','隆隆石','隆隆岩','小火馬','烈焰馬','呆呆獸','呆殼獸','小磁怪','三合一磁怪','大蔥鴨','嘟嘟','嘟嘟利','小海獅','白海獅','臭泥','臭臭泥','大舌貝','刺甲貝','鬼斯','鬼斯通','耿鬼','大岩蛇','催眠貘','引夢貘人','大鉗蟹','巨鉗蟹','霹靂電球','頑皮雷彈','蛋蛋','椰蛋樹','卡拉卡拉','嘎啦嘎啦','飛腿郎','快拳郎','大舌頭','瓦斯彈','雙彈瓦斯','獨角犀牛','鑽角犀獸','吉利蛋','蔓藤怪','袋獸','墨海馬','海刺龍','角金魚','金魚王','海星星','寶石海星','吸盤魔偶','飛天螳螂','迷唇姐','電擊獸','鴨嘴火獸','凱羅斯','肯泰羅','鯉魚王','暴鯉龍','拉普拉斯','百變怪','伊布','水伊布','雷伊布','火伊布','多邊獸','菊石獸','多刺菊石獸','化石盔','鐮刀盔','化石翼龍','卡比獸','急凍鳥','閃電鳥','火焰鳥','迷你龍','哈克龍','快龍','超夢','夢幻'])
    
    combo.pack()
    
    canvas2.create_window(650, 240, width=200, height=20,window=combo)
    
    #combobox函數回應點擊
    
    def callbackFunc(event):
        cursor=db.cursor()
        sql="select chinese_name,type_1,type_2,total_points,hp,attack,defense,sp_attack,sp_defense,speed,introduce,pokedex_number,number from pokemon where chinese_name=%s"
        cursor.execute(sql,(combo.get(),))
        results=cursor.fetchall()
        for row in results:
            name=row[0]
            type1=row[1]
            type2=row[2]
            total_points=row[3]
            hp=row[4]
            attack=row[5]
            defense=row[6]
            sp_attack=row[7]
            sp_defense=row[8]
            speed=row[9]
            introduce=row[10]
            pokedex_number=row[11]
            number=row[12]
        
        lblnumber.configure(text='圖鑑編號:'+pokedex_number)
        lblname.configure(text='名稱:'+name)
        lbltype1.configure(text='屬性1:'+type1)
        lbltype2.configure(text='屬性2:'+type2)
        lbltp.configure(text='總戰鬥力:'+total_points)
        lblhp.configure(text='血量:'+hp)
        lblatk.configure(text='攻擊力:'+attack)
        lbldfs.configure(text='防禦力:'+defense)
        lblspatk.configure(text='特攻:'+sp_attack)
        lblspdfs.configure(text='特防:'+sp_defense)
        lblspd.configure(text='速度:'+speed)
        lblint.configure(text='簡介:'+introduce)
        lblpicture.configure(image=pic[number-1])
    
    combo.bind("<<ComboboxSelected>>", callbackFunc)
    
    #圖鑑編號Label
    lblnumber=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblnumber.pack()
    canvas2.create_window(460,455,window=lblnumber)
    
    #名字Label
    lblname=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblname.pack()
    canvas2.create_window(460,510,window=lblname)
    
    #屬性1
    lbltype1=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lbltype1.pack()
    canvas2.create_window(460,565,window=lbltype1)
    
    #屬性2
    lbltype2=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lbltype2.pack()
    canvas2.create_window(460,620,window=lbltype2)
    
    #total_points
    lbltp=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lbltp.pack()
    canvas2.create_window(460,675,window=lbltp)
    
    #HP
    lblhp=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblhp.pack()
    canvas2.create_window(700,455,window=lblhp)
    
    #attack
    lblatk=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblatk.pack()
    canvas2.create_window(700,510,window=lblatk)
    
    #defense
    lbldfs=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lbldfs.pack()
    canvas2.create_window(700,565,window=lbldfs)
    
    #sp_attack
    lblspatk=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblspatk.pack()
    canvas2.create_window(700,620,window=lblspatk)
    
    #sp_defense
    lblspdfs=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblspdfs.pack()
    canvas2.create_window(700,675,window=lblspdfs)
    
    #speed
    lblspd=tk.Label(top,text='',font=("微軟正黑體",24),bg='#7dad71')
    lblspd.pack()
    canvas2.create_window(700,730,window=lblspd)
    
    #框
    lblsqare=tk.Label(top,image=pho,bg='#7dad71')
    lblsqare.pack(side="top",fill="both",expand="yes")
    canvas2.create_window(1075, 600, width=426, height=346,
                          window=lblsqare)
    
    #introduce
    lblint=tk.Label(top,text='',font=("微軟正黑體",30),wraplength=390,bg='#7dad71')
    lblint.pack()
    canvas2.create_window(1075,600,window=lblint)
    
    #圖片Label
    lblpicture=tk.Label(top,image='',bg='#7dad71')
    lblpicture.pack(side="top",fill="both",expand="yes")
    canvas2.create_window(175, 600, width=300, height=365,
                          window=lblpicture)
    
    top.mainloop()
    
path6 = '主視窗按鈕.png'
img6 = ImageTk.PhotoImage(Image.open(path6))
    

#主視窗背景
canvas = tk.Canvas(root, width=1280,height=720,bd=0, highlightthickness=0)
imgpath = '主視窗背景.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
 
canvas.create_image(650, 350, image=photo)
canvas.pack()

#建立按鈕
button=Button(root,command=second_win,image=img6,cursor='hand2',bd=0)
button.pack()

canvas.create_window(650, 475,window=button)


root.mainloop()

