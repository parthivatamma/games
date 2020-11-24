import time
import os
from tkinter import *
gs = 0

def GameStart():
    global gs
    gs = gs + 1
    print(' i am in GS')
    print(gs)
tk = Tk()
btn = Button(tk, text = 'Start Game', command = GameStart)
btn.pack()
 

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

    def turn_left(self, evt):
        self.press_left = self.press_left + 1
        self.x = -21
        self.pos = self.canvas.coords(self.image)
        self.draw()       

    def turn_right(self, evt):
        self.press_right = self.press_right + 1
        self.x = 21
        self.pos = self.canvas.coords(self.image)
        self.draw()
 
    def draw(self):
        if self.press_right >= 1:
            self.canvas.move(self.image, self.x, self.y)
            self.press_right = 0  

        elif self.press_left >= 1:
            self.canvas.move(self.image, self.x, self.y)
            self.press_left = 0

class bullet:
    def __init__(self, canvas, color):
        self.canvas = canvas
        bullet_img = os.path.join(prog_dir, rel_image_path)+"bullet.png"
        self.images_sprite = [PhotoImage(file = bullet_img)]
        self.image = self.canvas.create_image(400,700 , image = self.images_sprite[0], anchor ='s')
        self.x = 0
        self.y = 0 
        self.canvas.move(self.image, self.x, self.y)
        self.press_space = 0
        self.pressleft = 0
        self.pressright = 0
        self.canvas.bind_all('<space>', self.space_press)
        self.canvas.bind_all('<r>', self.reload)
        self.pos = self.canvas.coords(self.image)
        print('Init coords', self.pos[0], self.pos[1])
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

    def reload(self, evt):
        print('Reloading...')
        print('Reloaded')
        self.x = 0
        self.y = 0
        self.pos = self.canvas.coords(self.image)
        ball2.ball_Coords()
        movexby = ball_pos[0] - self.pos[0]
        self.canvas.move(self.image, movexby, 700)
    
    def space_press(self, evt):
        self.press_space = self.press_space + 1

    def movement(self): 
        self.canvas.move(self.image, self.x, self.y) 
        self.canvas.after(100, self.movement)

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0]
        self.coordinates.y2 = xy[1]

    def turnleft(self, evt):
        self.pressleft = self.pressleft + 1
        self.x = -21
        self.pos = self.canvas.coords(self.image)
        self.draw()       

    def turnright(self, evt):
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
            self.reload
            print('i am in draw')
        if self.press_space == 0:
            self.y1 = 0
            self.x1 = 0
            
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

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30

    def draw(self):
        pos = self.canvas.coords(self.image)
        move_right = 1
        if pos[0] <= 0 :
            move_right = 1
        elif pos[0] >= 374 :
            move_right = 0
        if move_right == 1 :
            self.x = self.x + 2        
            self.canvas.move(self.image, self.x, self.y)
        else:
            self.x = self.x - 2        
            self.canvas.move(self.image, self.x, self.y)

class death_cube:

    def __init__(self, canvas, color):
        self.canvas = canvas

    def draw(self):
        self.id = canvas.create_rectangle(0, 0, 2500, 2500, fill = 'red')
        elmo_img = os.path.join(prog_dir, rel_image_path)+"elmo.png"
        self.images_sprite = [PhotoImage(file = elmo_img)]
        self.image = self.canvas.create_image(0, 0,\
                image = self.images_sprite[0], anchor='nw')

death_cube2 = death_cube(canvas, 'red')
counter = 0
score = 0

while 1:

    canvas.create_text(400, 700, text = ('Score: ', score))
    while gs == 0:
        time.sleep(1)
        tk.update_idletasks()
        tk.update()
    
    ball2 = ball(canvas, 'blue')
    bullet2 = bullet(canvas, 'white')
    enemy2 = enemy(canvas, 'black')

    while gs >= 1:
        counter = counter + 1
        ball2.draw()
        enemy2.my_pos()
        bullet2.draw()
        bullet2.my_pos()

        if counter == 10:
            enemy2.draw()
            counter = 0
            if bullet2.x1 >= enemy2.x1 and bullet2.y1 == enemy2.y1 + 70 :
                print("Bullet" , bullet2.x1, bullet2.y1)
                print("Enemy" , enemy2.x1, enemy2.y1)
                death_cube2.draw()
                canvas.create_text(400, 400, text='YOU WIN', font=('Times', 69))
                score = score + 100
                print('Enemy defeated')
                gs = 0
                time.sleep(5)
                canvas.delete("all")
                bullet2.reload
                break
    
            elif bullet2.y1 <= 0:
                print("Press R to reload now")
                bullet2.y = 0
                bullet2.y1 = 700
                
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)