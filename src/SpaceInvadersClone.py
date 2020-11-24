import time
import os
from tkinter import *
#from goto import goto, label
#from tkinter.ttk import *
#import tkinter as tk
#master = tk.Tk()
#t = turtle.Pen()
gs = 0

def GameStart():
    global gs
    gs = gs + 1
    print(' i am in GS')
    print(gs)
tk = Tk()
btn = Button(tk, text = 'Start Game', command = GameStart)
btn.pack()
 

#tk = Tk()
tk.title("SpaceInvaders.exe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
prog_dir = os.path.dirname(__file__)
rel_image_path = "../images/"


class ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        ship_img = os.path.join(prog_dir, rel_image_path)+"spaceship.png"
        self.images_sprite = [PhotoImage(file = ship_img)]
        self.image = self.canvas.create_image(400,700 , image = self.images_sprite[0], anchor ='s')
        self.x = 0
        self.y = 0
        #self.addtag_above(newtag, player)
        self.press_left = 0
        self.press_right = 0
        global pressright
        global pressleft
        pressright=self.press_right
        pressleft=self.press_left
        self.pos = self.canvas.coords(self.image)
        print('Init coords', self.pos[0], self.pos[1])
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)

    def ball_Coords(self):
        global ball_pos     
        ball_pos = self.canvas.coords(self.image)
    #def mypos(self):

    def turn_left(self, evt):
        #print("PressLeft", self.x, self.press_left)
        self.press_left = self.press_left + 1
        self.x = -21
        self.pos = self.canvas.coords(self.image)
        self.draw()       

    def turn_right(self, evt):
        #print("PressRight", self.x, self.press_right)
        self.press_right = self.press_right + 1
        self.x = 21
        self.pos = self.canvas.coords(self.image)
        self.draw()

    #def coords(self):
    #    xy = self.game.canvas.coords(self.image)
    #    self.coordinates.x1 = xy[0]
    #    self.coordinates.y1 = xy[1]
    #    self.coordinates.x2 = xy[0]
    #    self.coordinates.y2 = xy[1]
 
    def draw(self):
        if self.press_right >= 1:
            self.canvas.move(self.image, self.x, self.y)
            #bullet.canvas.move(bullet.image, self.x, self.y)
            #print('Im in the draw func, going right', self.press_right)
            self.press_right = 0  

        elif self.press_left >= 1:
            self.canvas.move(self.image, self.x, self.y)
            #self.canvas.move(bullet.image, self.x, self.y)
            #print('Im in the draw func, going left', self.press_left)
            self.press_left = 0

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def within_x(co1, co2):
        if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
            return True
        else:
            return False

    def within_y(co1, co2):
        if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
            return True
        else:
            return False

    def collided_left(co1, co2):
        if within_y(co1, co2):
            if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
                return True
        return False

    def collided_right(co1, co2):
        if within_y(co1, co2):
            if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
                return True
        return False

    def collided_top(co1, co2):
        if within_x(co1, co2):
            if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
                return True
        return False

    def collided_bottom(y, co1, co2):
        if within_x(co1, co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 and y_calc <= co2.y2:
                return True
        return False

class bullet:
    def __init__(self, canvas, color):
        self.canvas = canvas
        bullet_img = os.path.join(prog_dir, rel_image_path)+"bullet.png"
        #self.id = canvas.create_rectangle(7, 7, 14, 14, fill = color)
        self.images_sprite = [PhotoImage(file = bullet_img)]
        self.image = self.canvas.create_image(400,700 , image = self.images_sprite[0], anchor ='s')
        #self.canvas.move(self.id, 400, 300)
        self.x = 0
        self.y = 0 
        #self.addtag_above(newtag, player)
        self.canvas.move(self.image, self.x, self.y)
        self.press_space = 0
        self.pressleft = 0
        self.pressright = 0
        self.canvas.bind_all('<space>', self.space_press)
        self.canvas.bind_all('<r>', self.respawn)
        self.pos = self.canvas.coords(self.image)
        print('Init coords', self.pos[0], self.pos[1])
        #origX = yourcanvas.xview()[0]
        #origY = yourcanvas.yview()[0]
        #print(pos)
        #self.canvas.bind_all('<KeyPress-a>', self.turnleft)
        #self.canvas.bind_all('<KeyPress-d>', self.turnright)
        if pressleft == 1:
            self.x = 21
        if pressright ==1:
            self.x=-21             
        self.canvas_width = self.canvas.winfo_width()
        self.movement() 

    def my_pos(self):
        self.pos = self.canvas.coords(self.image)
        self.x1 = self.pos[0]
        self.y1 = self.pos[1]
        #self.y1 = self.pos[2]
        #self.y2 = self.pos[3]

    def respawn(self, evt):
        #for i in range()
        print('I am in respawn')
        self.x = 0
        self.y = 0
        self.pos = self.canvas.coords(self.image)
        ball2.ball_Coords()
        movexby = ball_pos[0] - self.pos[0]
        self.canvas.move(self.image, movexby, 700)
        #print(enemy.y1)
        #if self.y1 < enemy2.y1 + 100:
        #    self.x = 0
        #    self.y = 0
        #    self.canvas.move(self.image, self.x, self.y)
        #yourcanvas.xview_moveto(origX)
        #yourcanvas.yview_moveto(origY)
    
    def space_press(self, evt):
        self.press_space = self.press_space + 1

    def movement(self): 
        self.canvas.move(self.image, self.x, self.y) 
        self.canvas.after(100, self.movement)
        #rint('i am in movement')

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0]
        self.coordinates.y2 = xy[1]

    def turnleft(self, evt):
        #print("PressLeft", self.x, self.press_left)
        self.pressleft = self.pressleft + 1
        self.x = -21
        self.pos = self.canvas.coords(self.image)
        self.draw()       

    def turnright(self, evt):
        #print("PressRight", self.x, self.press_right)
        self.pressright = self.pressright + 1
        self.x = 21
        self.pos = self.canvas.coords(self.image)
        self.draw()

    def draw(self):
        if self.press_space == 1:
            self.canvas.move(self.image, self.x, self.y)
            self.press_space = 0
            self.y = - 20
            self.canvas.move(self.image, self.x, self.y)
            self.canvas.after(5, self.movement)
            self.respawn
            print('i am in draw')
        if self.press_space == 0:
            self.y1 = 0
            self.x1 = 0
            #self.canvas.move(self.image, self.x, self.y)
            #print('beesechurger')
            
                


class enemy:

    def __init__(self, canvas, color):
        self.canvas = canvas
        enemy_img = os.path.join(prog_dir, rel_image_path)+"enemyship.png"
        self.images_sprite = [PhotoImage(file = enemy_img)]
        self.image = self.canvas.create_image(10, 10, \
                image = self.images_sprite[0], anchor='nw')
        self.x = 0
        self.y = 0
        self.move_right = 1
        self.move_left = 0

        self.canvas_width = self.canvas.winfo_width()

    def my_pos(self):
        self.pos = self.canvas.coords(self.image)
        self.x1 = self.pos[0]
        self.y1 = self.pos[1]
        #self.y1 = self.pos[2]
        #self.y2 = self.pos[3]


    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        #return self.coordinates

    def draw(self):
        pos = self.canvas.coords(self.image)
        #print('EnemyCoords', pos[0], pos[1])
        move_right = 1
        if pos[0] <= 0 :
            move_right = 1

        elif pos[0] >= 374 :
            move_right = 0


        if move_right == 1 :
            self.x = self.x + 2        
            self.canvas.move(self.image, self.x, self.y)
            #print('Working0')
            #print('W0 x', self.x)

        else:
            self.x = self.x - 2        
            self.canvas.move(self.image, self.x, self.y)
            #print('Working1')
            #print('W1 x', self.x)

class death_cube:

    def __init__(self, canvas, color):

        self.canvas = canvas
        #self.id = canvas.create_oval(0, 0, 250, 250, fill=color)

    def draw(self):

        self.id = canvas.create_rectangle(0, 0, 2500, 2500, fill = 'red')
        elmo_img = os.path.join(prog_dir, rel_image_path)+"elmo.png"
        self.images_sprite = [PhotoImage(file = elmo_img)]
        self.image = self.canvas.create_image(0, 0,\
                image = self.images_sprite[0], anchor='nw')

#class JW999:
#    print('999')

death_cube2 = death_cube(canvas, 'red')
counter = 0
score = 0
#print('hamster_would_like_to_facetime = 0')

#label .gamerestart

while 1:

    canvas.create_text(400, 700, text = ('Score: ', score))
    while gs == 0:
        #print('e')
        time.sleep(1)
        #print(gs)
        tk.update_idletasks()
        tk.update()
    
    ball2 = ball(canvas, 'blue')
    bullet2 = bullet(canvas, 'white')
    enemy2 = enemy(canvas, 'black')

    while gs >= 1:
        counter = counter + 1
        #print('counter',counter)
        ball2.draw()
        enemy2.my_pos()
        bullet2.draw()
        bullet2.my_pos()
        #print(gs)

        #print('lego death star', enemy2.x1, enemy2.y1)
        if counter == 10:
            enemy2.draw()
            counter = 0
            #print('in counter' )
            if bullet2.x1 >= enemy2.x1 and bullet2.y1 == enemy2.y1 + 70 :
                #print('chicken nugget')
                death_cube2.draw()
                canvas.create_text(400, 400, text='YOU WIN', font=('Times', 69))
                score = score + 100
                print('Enemy defeated')
                gs = 0
                time.sleep(5)
                canvas.delete("all")
                bullet2.respawn
                break
    
            elif bullet2.y1 <= 0:
                print('beesechurger', bullet2.y1)
                bullet2.y = 0
                bullet2.y1 = 700
                
                

                #hamster_would_like_to_facetime = 1          
        #print('enemy(x,y)', enemy2.x1, enemy2.y1)
        #print('bullet(x,y)', bullet2.x1, bullet2.y1)
    

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
