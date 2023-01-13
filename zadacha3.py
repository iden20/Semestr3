import tkinter as tk
import time

gravity = 0.5
resistance = 0.005

WIDTH = 600
HEIGHT = 600


class Ball:
    def __init__(self, canvas, x, y, size):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.size = size
        self.acceleration = 5
        self.energy_x = 2
        self.energy_y = 1
        self.ball = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size,
                                       fill='gray', outline='black', width=2)

    def move(self):
        self.gravity_down()
        if self.y >= HEIGHT - self.size:
            self.dy = 0
            self.bounce_up()
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.ball, self.dx, self.dy)
        self.dx *= (1 - resistance)
        self.dy *= (1 - resistance)

    def bounce_up(self):
        if 50 * self.energy_y > gravity:
            self.energy_y -= 0.1
            self.dy -= gravity * 50 * self.energy_y

    def gravity_down(self):
        if 50 * self.energy_y > gravity:
            self.dy += gravity


def main():
    window = tk.Tk()
    window.title('Elastic collision')

    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack()

    x, y = WIDTH // 2, HEIGHT // 2

    ball = Ball(canvas, x, y, 25)


    while True:

        ball.move()

        canvas.update()

        time.sleep(0.009)


main()
