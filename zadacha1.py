from tkinter import *
import math
import time

root = Tk()

ekran = Canvas(root, width=600, height=600)
ekran.pack()

a = 30
b = 30
r = 200

t = 0
while t < 2 * math.pi:
    per_x = r * math.cos(t) + a + 200
    per_y = r * math.sin(t) + b + 200
    per_x1 = r * math.cos(t + 0.1) + a + 200
    per_y1 = r * math.sin(t + 0.1) + b + 200
    ekran.create_line(per_x, per_y, per_x1, per_y1)
    t += 0.1

t = 0
r2 = 5
per_x = r * math.cos(t) + a + r
per_y = r * math.sin(t) + b + r
ball = ekran.create_oval(per_x - r2, per_y - r2, per_x1 + r2, per_y1 + r2, fill="#0f1155")
while True:
    per_x = r * math.cos(t) + a + 200
    per_y = r * math.sin(t) + b + 200
    per_x1 = r * math.cos(t + 0.1) + a + r
    per_y1 = r * math.sin(t + 0.1) + b + r
    t += 0.1
    ekran.move(ball, per_x1 - per_x, per_y1 - per_y)
    root.update()
    time.sleep(0.1)

root.mainloop()
