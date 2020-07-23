from tkinter import *
import random
import time
scoreP1 = 0
scoreP2 = 0
 
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        pos = self.canvas.coords(self.id)
        print("Init coords", pos[0], pos[1], pos[2], pos[3])
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_right = False
        self.hit_left = False
        
    def hit_paddle1(self, pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        if pos[2] >= paddle1_pos[0] and pos[0] <= paddle1_pos[2]:
            if pos[3] >= paddle1_pos[1] and pos[3]:
                return True
            return False
 
    def hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3]:
                return True
            return False
 
    def miss_paddle1(self, pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        if pos[0] <= 10 and paddle1_pos[1] < pos[1] and paddle1_pos[3] < pos[3]:
            print('x')
            print("Ball Coords", pos[0], pos[1], pos[2], pos[3])
            print("Paddle1 Coords", paddle1_pos[0], paddle1_pos[1], paddle1_pos[2], paddle1_pos[3])
            self.hit_left = True
 
    def miss_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= self.canvas.winfo_width() - 10 and paddle2_pos[1] < pos[1] and paddle2_pos[3] < pos[3]:
            print('y')
            print("Ball Coords", pos[0], pos[1], pos[2], pos[3])
            print("Paddle2 Coords", paddle2_pos[0], paddle2_pos[1], paddle2_pos[2], paddle2_pos[3])
            self.hit_right = True
 
 
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
 
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        self.miss_paddle1(pos)
        self.miss_paddle2(pos)
    
        if pos[0] <= 10:
            self.x = 3
        if pos[2] >= self.canvas_width - 10:
            self.x = -3
 
    def restart(self):
        pos = self.canvas.coords(self.id)
        
        print("Before restart coords", pos[0], pos[1], pos[2], pos[3])
        print("Hit right", self.hit_right, "Hit Left", self.hit_left)  
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.hit_right = False
        self.hit_left = False
        self.canvas.move(self.id, 245, 100)
        x = 0
        while x < 10:
            pos = self.canvas.coords(self.id)
            print("restart coords", pos[0], pos[1], pos[2], pos[3])
            time.sleep(1)
            x += 1
        
        print('I am westating')
        global gotext
        gotext = False
    
class PaddleP1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,10,100,fill=color)
        self.canvas.move(self.id, 0, 100)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-s>', self.turn_up)
        self.canvas.bind_all('<KeyPress-w>', self.turn_down)
        
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y = 0
        elif pos[3] >= self.canvas_height:
            self.y = 0
 
    def turn_left(self, evt):
        self.x = -2
 
    def turn_right(self, evt):
        self.x = 2
 
    def turn_up(self, evt):
        self.y = 2
 
    def turn_down(self, evt):
        self.y = -2
 
class PaddleP2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,10,100,fill=color)
        self.canvas.move(self.id, self.canvas.winfo_width()-10, 0)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Down>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_down)
        
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y = 0
        elif pos[3] >= self.canvas_height:
            self.y = 0
 
    def turn_left(self, evt):
        self.x = -2
 
    def turn_right(self, evt):
        self.x = 2
 
    def turn_up(self, evt):
        self.y = 2
zzz
    def turn_down(self, evt):
        self.y = -2
 
tk = Tk()
tk.title("Pog")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.create_text(50, 390, text='P1 Score: ', fill = 'blue', font=('Courier',10))
canvas.create_text(333, 390, text='P2 Score: ', fill = 'red', font=('Courier',10))
def gameover_text(event):
    global gotext
    gotext= True
 
gotext = False
canvas.bind_all('<KeyPress-q>', gameover_text)
canvas.pack()
tk.update()
 
paddle1 = PaddleP1(canvas, 'blue')
paddle2 = PaddleP2(canvas, 'red')
ball = Ball(canvas, paddle1, paddle2, 'green')
 
while 1:
    if ball.hit_left == False and ball.hit_right == False:
        #canvas.create_text(111, 390, text = scoreP1, fill = 'blue', font=('Courier',10))
        #canvas.create_text(394, 390, text = scoreP2, fill = 'red', font=('Courier',10))
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
 
    else:
        print('else_works')
        print(gotext)
        while gotext == False:
            canvas.create_text(250, 190, text='GAME OVER', fill='red', font=('Courier',30))
            tk.update()
            time.sleep(1)
            canvas.create_text(250, 190, text='GAME OVER', fill='blue', font=('Courier',30))
            tk.update()
            time.sleep(1)
        ball.restart()
        ball.hit_left = False
        ball.hit_right = False
 

