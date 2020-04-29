import random
import time
from tkinter import *

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.images_sprite = [PhotoImage(file = "c:/users/tammar/downloads/Uneeded Pics/sketchshuttle.png")]
        self.image = self.canvas.create_image(400,700 , image = self.images_sprite[0], anchor ='s')
        self.x = 0
        self.y = 0
        self.press_left = 0
        self.press_right = 0
        self.pos = self.canvas.coords(self.image)
        print('Init coords', self.pos[0], self.pos[1])
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)

    #def ball_Coords(self):
        #global ball_pos
        #ball_pos = self.canvas.coords(self.id)
        
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
        #self.id = canvas.create_rectangle(7, 7, 14, 14, fill = color)
        self.images_sprite = [PhotoImage(file = "c:/users/tammar/downloads/Uneeded Pics/lazerbeam.png")]
        self.image = self.canvas.create_image(400,700 , image = self.images_sprite[0], anchor ='s')
        #self.canvas.move(self.id, 400, 300)
        self.x = 0
        self.y = 0 
        self.canvas.move(self.image, self.x, self.y)
        self.press_space = 0
        self.press_left = 0
        self.canvas.bind_all('<space>', self.space_press)
        self.pos = self.canvas.coords(self.image)
        print('Init coords', self.pos[0], self.pos[1])
        #print(pos)
        self.canvas_width = self.canvas.winfo_width()
    
    def my_pos(self):
        self.pos = self.canvas.coords(self.image)
        self.x1 = self.pos[0]
        self.y1 = self.pos[1]
        #self.y1 = self.pos[2]
        #self.y2 = self.pos[3]
    
    def space_press(self, evt):
        self.press_space = self.press_space + 1
        
    
    
    
    def draw(self):
        if self.press_space == 1:
            self.canvas.move(self.image, self.x, self.y)
            self.press_space = 0
            self.y = self.y - 1
            self.canvas.move(self.image, self.x, self.y)

        
class enemy:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.images_sprite = [PhotoImage(file = "c:/users/tammar/downloads/Uneeded Pics/spaceshipbmp.png")]
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
        #self.images_sprite = [PhotoImage(file = "c:/users/tammar/downloads/Uneeded Pics/epicexplosion.png")]
        #self.image = self.canvas.create_image(0, 0,\
                #image = self.images_sprite[0], anchor='nw')

ball2 = ball(canvas, 'black')
bullet2 = bullet(canvas, 'white')
death_cube2 = death_cube(canvas, 'red')
enemy2 = enemy(canvas, 'black')
counter = 0
hamster_would_like_to_facetime = 0

while 1:
    counter = counter + 1
    #print('counter',counter)
    ball2.draw()
    bullet2.draw()
    enemy2.my_pos()
    bullet2.my_pos()
    #print('lego death star', enemy2.x1, enemy2.y1)
    if counter == 10:
        enemy2.draw()
        counter = 0
        print('in counter' )
        if bullet2.x1 >= enemy2.x1 and bullet2.y1 <= enemy2.y1 + 70:
            print('chicken nugget')
            death_cube2.draw()
            canvas.create_text(300, 300, text='YOU WIN')
            #hamster_would_like_to_facetime = 1          
    #print('enemy(x,y)', enemy2.x1, enemy2.y1)
    #print('bullet(x,y)', bullet2.x1, bullet2.y1)
    if hamster_would_like_to_facetime == 1:
        death_cube2.draw()
        print('toulouse')
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)