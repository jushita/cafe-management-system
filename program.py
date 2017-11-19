from tkinter import *
import random
import time
import datetime

#Basic window is created
root = Tk()
root.geometry("1350x50+0+0")
root.title("Cafe Management Systems")
root.configure(background = "black")
#basic window creation ends

#Frames are created
Tops = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
Tops.pack(side = TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 440, height = 650, bd = 8, relief = "raise")
f2.pack(side = RIGHT)


f1a = Frame(f1, width = 90, height = 330, bd = 8, relief = "raise")
f1a.pack(side = TOP)

f2a = Frame(f1, width = 90, height = 320, bd = 6, relief = "raise")
f2a.pack(side = BOTTOM)

ft2 = Frame(f2, width = 440, height = 650, bd = 12, relief = "raise")
ft2.pack(side = TOP)
fb2 = Frame(f2, width = 440, height = 330, bd = 16, relief = "raise")
fb2.pack(side = BOTTOM)

f1aa = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1aa.pack(side = LEFT)
f1ab = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1ab.pack(side = RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd = 14, relief = "raise")
f2aa.pack(side = LEFT)

f2ab = Frame(f2a, width = 450, height = 330, bd = 6, relief = "raise")
f2ab.pack(side = RIGHT)


Tops.configure (background = 'black')
f1.configure (background = 'black')
f2.configure (background = 'black')

lblInfo = Label(Tops, font  = ('arial', 70, 'bold'), text = "Cafe Management Systems", bd = 10)
lblInfo.grid(row = 0, column = 0)

#Frame Creation ends

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

var1.set = ("0")
var2.set = ("0")
var3.set = ("0")
var4.set = ("0")
var5.set = ("0")
var6.set = ("0")
var7.set = ("0")
var8.set = ("0")
var9.set = ("0")
var10.set = ("0")
var11.set = ("0")
var12.set = ("0")
var13.set = ("0")
var14.set = ("0")
var15.set = ("0")
var16.set = ("0")
#Widget created
# f1aa == left hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Latte = Checkbutton(f1aa, text="Latte\t", variable = var1, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Espresso = Checkbutton(f1aa, text="Espresso \t\t", variable = var2, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Iced_Latte = Checkbutton(f1aa, text="Iced Latte \t\t", variable = var3, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Vale_Coffee = Checkbutton(f1aa, text="Vale_Coffee \t\t", variable = var4, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Cappuccino  = Checkbutton(f1aa, text="Cappuccino \t\t", variable = var5, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
African_Coffee = Checkbutton(f1aa, text="African Coffee \t\t", variable = var6, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
American_Coffee = Checkbutton(f1aa, text="American Coffee \t\t", variable = var7, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Iced_Cappuccino = Checkbutton(f1aa, text="Iced Cappuccino \t\t", variable = var8, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)


#f1ab == right hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

CoffeeCake= Checkbutton(f1ab, text="Coffee Cake\t", variable = var9, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Red_Velvet_Cake = Checkbutton(f1ab, text="Red Velvet Cake\t", variable = var10, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest Cake\t", variable = var11, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream Cake\t", variable = var12, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos Chocolate Cake\t", variable = var13, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text="Kilburn Chocolatee Cake\t", variable = var14, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
Carlton_Hill_Cake = Checkbutton(f1ab, text="Carlton Hill Cake\t", variable = var15, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Queen_park_Cake = Checkbutton(f1ab, text="Queen's Park Chocolate Cake\t", variable = var16, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtLatte = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', state = DISABLED )
txtLatte.grid(row = 0, column = 1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtCoffeeCake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', state = DISABLED )
txtCoffeeCake.grid(row = 0, column = 1)

root.mainloop()
