from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(30, 30, 50, 50, fill=color)
        self.canvas.move(self.id, 100, 200)

        # ADD THESE LINES TO OUR __INIT__ METHOD
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1


def main():
    tk = Tk()
    tk.title("хуй")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, bg="white", width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    ball1 = Ball(canvas, 'green')
    while 1:
        tk.update()
        ball1.draw()  # call the ball draw method here
        time.sleep(0.01)


main()