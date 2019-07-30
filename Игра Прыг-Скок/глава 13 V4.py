''' v1 В этой версии исправлено движение ракетки.
Теперь ракетка движется только при нажатой клавише  влево/вправо.
В случае, если клавишу отпустить, ракетка останавливается.
Для баланса увеличина скорость ракетки с abs2 до abs3'''

''' v2 Добавлен запуск  игры по клавише Enter'''
'''v3 Добавлен текст в случае пройгрыша '''


from tkinter import*
import random
import time
class Ball:
    def __init__(self, canvas,paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
        self.score = 0 #Ввели переменной очки значение ноль#
        

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2] >=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<= paddle_pos[3]:
                self.score +=1 # случае соударения добавляем 1 очко#
                self.x+=self.paddle.x
                return True
        return False    

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,220,380)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.started=False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)
        self.canvas.bind_all('<Return>',self.start_game) # Задали вызов функции по клавише Enter#

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0

    def turn_left(self,evt):
        self.x=-3

    def turn_right(self,evt):
        self.x=3
    def stop(self,evt):
        self.x=0

    def start_game(self, evt): #Определили вызываемую функцию. Она после нажатия становится истинной#
        self.started=True
        
tk=Tk()
tk.title("Игра")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle=Paddle(canvas, 'blue')
ball=Ball(canvas,paddle,'red')
game_over=canvas.create_text(250,200,text='ИГРА ОКОНЧЕНА.',state='hidden' )#добавили надпись, невидимого цвета#
score=canvas.create_text(450,20,text=0 )

while 1:
    if ball.hit_bottom==False and paddle.started==True: # Добавили в основной цикл запуск, только если функция начала игры из класса ракетки имеет значение True#
        ball.draw()
        paddle.draw()
        canvas.itemconfig(score, text=ball.score)# Добавили изменение текста на экране в переменной очки, вывод количество очков#
    if ball.hit_bottom==True:
        time.sleep(1)
        canvas.itemconfig(game_over, state='normal') #Если функция класса бол истина, то текст становится видимым.#
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    
