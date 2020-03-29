from tkinter import*
import time
import random
tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

canvas.create_rectangle(0,0,800, 600,fill="black")

class MovingObject:
    def __init__(self, id, x, y, w, h, vx, vy, color):
        self.id = id
        self.x, self.y = (x,y)
        self.w, self.h = (w,h)
        self.vx, self.vy = (vx, vy)
        self.color = color
    def redraw(self):
        canvas.coords(self.id, self.x, self.y, self.x+self.w, self.y+ self.h)
    def move(self):
        pass
class Paddle(MovingObject):
    def __init__(self, id, x, y, w, h, color):
        MovingObject.__init__(self, id, x, y, w, h, 0, 0, color)
    def move(self):
        self.x = self.x + self.vx
    def set_v(self, v):
        self.vx = v
    def stop(self):
        self.vx = 0

class Spear(MovingObject):
    def __init__(self, id, x, y, w, h, vy, color):
        MovingObject.__init__(self, id, x, y, w, h, 0, vy, color)
    def move(self):
        self.y = self.y + self.vy

class Hp:
    def __init__(self, id, x, y, w, h, c="blue"):
        self.id=id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
    def delete_hp(self):
        canvas.delete(self.id)

class Life:
    def __init__(self, id, x, y, w, h, c="blue"):
        self.id=id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c


class Block:
    def __init__(self, id, x, y, w, h, c="blue"):
        self.id=id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def redraw(self):
        canvas.coords(self.id, self.x, self.y, self.x + self.w, self.y + self.h)

    def delete_block(self):
        canvas.delete(self.id)

#class Life:



class Ball(MovingObject):
    def __init__(self, id, x, y, d, vx, vy, color):
        MovingObject.__init__(self, id, x, y, d, d, vx, vy, color)
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x <= 0 or self.x + ball_d >= 800:
            self.vx = -self.vx
        if self.y <= 0:
            self.vy = -self.vy


paddle_x=300
paddle_y=400
paddle_w=100
paddle_h=20
paddle_vx=5
block1_x = 5
block1_y = 5
block_w = 100
block_h = 20
ball_x=200
ball_y=200
ball_d=10
ball_vx=4
ball_vy=4
hp_x=650
hp_y=550
hp_w=20
hp_h=20
life_x= 100
life_y=550
life_w=20
life_h=20


class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.paddle = None
        self.blocks = []
        self.block = None
        self.ball = None
        self.hp = None
        self.hps = []
        self.life = None
        self.lives = []
        self.spear = None

    def create_paddle(self, x, y, w, h, vx,color):
        id = canvas.create_rectangle(x,y,x+w,y+h,fill=color)
        return Paddle(id, x, y, w, h, color)

    def create_block(self, x, y, w, h, color):
        id = canvas.create_rectangle(x, y, x+w, y+h, fill=color)
        return Block(id, x, y, w, h, color)

    def create_ball(self, x, y, d, vx, vy,color):
        id = canvas.create_oval(x, y, x+d, y+d, fill=color)
        return Ball(id, x, y, d, vx, vy, color)

    def create_hp(self, x, y, w, h, color):
        id = canvas.create_rectangle(x, y, x+w, y+h, fill=color)
        return Block(id, x, y, w, h, color)
    def create_life(self, x, y, w, h, color):
        id = canvas.create_oval(x, y, x + w, y + h, fill=color)
        return Block(id, x, y, w, h, color)
    def create_spear(self, x, y, w, h, vy, color):
        id = canvas.create_rectangle(x, y, x+w, y+h, fill=color)
        return Spear(id, x, y, w, h, vy, color)
    def stop_game(self):
        if self.ball.y + self.ball.h > 600:
            return True
    def delete_spear(spear):
        id = spear["id"]
        canvas.delete(id)
    def spear_rand(self):
        if self.spear==None and random.randint(0,1000)<10:
            self.spear = self.create_spear(random.randint(100,700), 10, 1, 40, 5, "red")
        if self.spear and self.spear.y+self.spear.h >= 600:
            self.delete_spear(self.spear)
            self.spear = None

    def del_life(self):
        if self.ball.y + self.ball.h > 600:
            i=1
            for life in self.lives:
                if i==len(self.lives):
                    canvas.delete(life.id)
                    self.lives.remove(life)
                i=i+1
    def delete_block(block):
        id = block["id"]
        canvas.delete(id)
    def up_paddle(self, event):
        self.paddle.vx = paddle_vx

    def down_paddle(self, event):
        self.paddle.vx = -paddle_vx

    def stop_paddle(self, event):
        self.paddle.vx = 0

    def del_block(self):
        for block in self.blocks:
            if block.y + block.h > self.ball.y and block.x < self.ball.x and block.x+block.w > self.ball.x:
                self.ball.vy = -self.ball.vy
                canvas.delete(block.id)
                self.blocks.remove(block)
                return True
    def ball_bounce(self):
        if (self.ball.x + self.ball.w >= self.paddle.x
                and self.paddle.y < self.ball.y + self.ball.h
                and self.ball.x < self.paddle.x + self.paddle.w
                and self.ball.y < self.paddle.y + self.paddle.h):
            if self.ball.x < self.paddle.x + self.paddle.w/2:
                self.ball.vx = self.ball.vx*0.6
                self.ball.vy = -self.ball.vy
            elif self.ball.x > self.paddle.x + self.paddle.w/2:
                self.ball.vx = self.ball.vx*1.5
                self.ball.vy = -self.ball.vy
        #if self.x<self.paddle.x+self.paddle.w and self.paddle.y<self.ball.y and self.paddle.y + self.paddle.h > self.ball.y + self.ball.h:
        #    self.ball.vx = -self.ball.vx
        #    print("aaa")
    def tap_space(self):
        canvas.create_text(400, 300, text="tap space to start", fill="white", font=("FixedSys", 100))



    def animate(self):
        #if canvas.bind_all('<KeyPress-space>', self.tap_space):
        start = time.time()
        while True:
            movingObjs = [self.paddle, self.ball, self.spear]
            while True:
                #self.spear_rand()
                for obj in movingObjs:
                    if obj != None:
                        obj.move()
                if self.ball.y + self.ball.h > 600:
                    break
                    #print("aaa")
                self.ball_bounce()
                for obj in movingObjs:
                    if obj != None:
                        obj.redraw()
                self.del_block()
                if self.blocks == []:
                    break

                tk.update_idletasks()
                tk.update()
                time.sleep(DURATION)

            if self.blocks ==[]:
                canvas.create_text(400, 300, text="Clear!", fill="white", font=("FixedSys", 100))
                canvas.create_text(400, 500, text="time:{}".format(int(time.time() - start)), fill="white",
                                   font=("FixedSys", 50))
                break
            elif self.lives==[] and self.block != []:
                canvas.create_text(400, 300, text="Game Over", fill="white", font=("FixedSys", 100))
                break
            else:
                i = 1
                for life in self.lives:
                    if i == len(self.lives):
                        canvas.delete(life.id)
                        self.lives.remove(life)
                    i = i + 1
                self.ball = self.create_ball(ball_x, ball_y, ball_d, ball_vx, ball_vy, "white")


    def set(self):
        for x in range(3):
            for i in range(8):
                self.block = self.create_block(block1_x + 100 * i, block1_y + 20 * x, block_w, block_h, "green")
                self.blocks.append(self.block)
        self.ball = self.create_ball(ball_x, ball_y, ball_d, ball_vx, ball_vy, "white")
        canvas.bind_all('<KeyPress-Right>', box.up_paddle)
        canvas.bind_all('<KeyPress-Left>', box.down_paddle)
        canvas.bind_all('<KeyRelease-Right>', box.stop_paddle)
        canvas.bind_all('<KeyRelease-Left>', box.stop_paddle)
        self.paddle = self.create_paddle(paddle_x, paddle_y, paddle_w, paddle_h, 0, "white")

        for x in range(5):
            self.hp = self.create_hp(hp_x + x*25, hp_y, hp_w, hp_h, "orange")
            self.hps.append(self.hp)
        for x in range(3):
            self.life = self.create_life(life_x + x*25, life_y, life_w, life_h, "red")
            self.lives.append(self.life)
        canvas.create_text(630, 560, text="HP", fill="orange", font=("FixedSys", 30))
        canvas.create_text(50, 560, text="LIFE", fill="red", font=("FixedSys", 30))

box = Box(100, 100, 200, 200)
DURATION = 0.01


box.set()
box.animate()




tk.mainloop()