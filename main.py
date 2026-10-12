# import tkinter as tk
# root = tk.Tk()
# root.title("My First Canvas")

# canvas = tk.Canvas(root, width=500,
#                    height=350, bg="white")
# canvas.pack()
# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(280, 50, 440, 190, fill="red")
# canvas.create_line(50, 250, 500, 250, width=4)
# canvas.create_text(275, 310, text="Hello Canvas", font=("Arial", 20))

# root.mainloop()
import tkinter as tk
import random

root = tk.Tk()
root.title("Zangpo's Sweet Home")
root.geometry("700x600")

canvas = tk.Canvas(root, width=650, height=550, bg="#07152e")
canvas.pack()

stars = [
    (50, 60), (120, 100), (180, 45), (250, 90),
    (330, 50), (400, 110), (480, 55), (550, 95),
    (610, 45), (80, 160), (520, 150)
]

for x, y in stars:
    canvas.create_oval(
        x, y, x + 5, y + 5,
        fill="white",
        outline="white"
    )

canvas.create_oval(
    500, 45, 590, 135,
    fill="#fff4b0",
    outline="#fff4b0"
)

canvas.create_oval(
    525, 40, 600, 115,
    fill="#07152e",
    outline="#07152e"
)

canvas.create_rectangle(
    170, 160, 480, 470,
    fill="#b91c1c",
    outline="black",
    width=4
)

canvas.create_polygon(
    140, 160,
    325, 45,
    510, 160,
    fill="black",
    outline="white",
    width=2
)

canvas.create_line(
    170, 260, 480, 260,
    fill="black",
    width=4
)

canvas.create_line(
    170, 360, 480, 360,
    fill="black",
    width=4
)

canvas.create_rectangle(
    200, 190, 260, 235,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    390, 190, 450, 235,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    200, 285, 260, 330,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    390, 285, 450, 330,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    290, 375, 360, 470,
    fill="black",
    outline="white",
    width=3
)

canvas.create_oval(
    345, 420, 353, 428,
    fill="red",
    outline="white"
)

canvas.create_rectangle(
    200, 390, 260, 435,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    390, 390, 450, 435,
    fill="black",
    outline="white",
    width=2
)

canvas.create_rectangle(
    270, 270, 380, 335,
    fill="#b91c1c",
    outline="black",
    width=3
)

canvas.create_rectangle(
    265, 265, 385, 275,
    fill="black"
)

canvas.create_line(
    275, 275, 275, 325,
    fill="black",
    width=3
)

canvas.create_line(
    295, 275, 295, 325,
    fill="black",
    width=3
)

canvas.create_line(
    315, 275, 315, 325,
    fill="black",
    width=3
)

canvas.create_line(
    335, 275, 335, 325,
    fill="black",
    width=3
)

canvas.create_line(
    355, 275, 355, 325,
    fill="black",
    width=3
)

canvas.create_line(
    375, 275, 375, 325,
    fill="black",
    width=3
)

canvas.create_rectangle(
    265, 325, 385, 335,
    fill="black"
)

canvas.create_rectangle(
    270, 170, 380, 225,
    fill="#b91c1c",
    outline="black",
    width=3
)

canvas.create_rectangle(
    265, 165, 385, 175,
    fill="black"
)

canvas.create_line(
    275, 175, 275, 215,
    fill="black",
    width=3
)

canvas.create_line(
    295, 175, 295, 215,
    fill="black",
    width=3
)

canvas.create_line(
    315, 175, 315, 215,
    fill="black",
    width=3
)

canvas.create_line(
    335, 175, 335, 215,
    fill="black",
    width=3
)

canvas.create_line(
    355, 175, 355, 215,
    fill="black",
    width=3
)

canvas.create_line(
    375, 175, 375, 215,
    fill="black",
    width=3
)

canvas.create_rectangle(
    265, 215, 385, 225,
    fill="black"
)

canvas.create_rectangle(
    0, 470, 650, 550,
    fill="black",
    outline="black"
)

canvas.create_rectangle(
    290, 470, 360, 550,
    fill="#b91c1c",
    outline="black"
)

canvas.create_rectangle(
    80, 390, 90, 500,
    fill="black"
)

canvas.create_rectangle(
    560, 390, 570, 500,
    fill="black"
)

canvas.create_rectangle(
    50, 350, 600, 420,
    fill="black",
    outline="#b91c1c",
    width=4
)

canvas.create_text(
    325, 385,
    text="Zangpo's Sweet Home",
    fill="white",
    font=("Arial", 24, "bold")
)

canvas.create_polygon(
    500, 450,
    550, 410,
    600, 450,
    fill="#8B4513",
    outline="black",
    width=3
)

canvas.create_rectangle(
    510, 450, 590, 500,
    fill="#A0522D",
    outline="black",
    width=3
)

canvas.create_oval(
    535, 460, 565, 500,
    fill="black",
    outline="black"
)

canvas.create_oval(
    385, 390, 475, 480,
    fill="#8B4513",
    outline="black",
    width=3
)

canvas.create_oval(
    360, 350, 445, 425,
    fill="#A0522D",
    outline="black",
    width=3
)

canvas.create_oval(
    355, 345, 390, 395,
    fill="#5C3317",
    outline="black",
    width=2
)

canvas.create_oval(
    425, 345, 460, 395,
    fill="#5C3317",
    outline="black",
    width=2
)

canvas.create_oval(
    380, 370, 390, 380,
    fill="black"
)

canvas.create_oval(
    415, 370, 425, 380,
    fill="black"
)

canvas.create_oval(
    397, 390, 410, 402,
    fill="black"
)

canvas.create_arc(
    390, 388, 420, 415,
    start=200,
    extent=140,
    style="arc",
    outline="black",
    width=2
)

canvas.create_rectangle(
    395, 450, 415, 510,
    fill="#8B4513",
    outline="black",
    width=3
)

canvas.create_rectangle(
    445, 450, 465, 510,
    fill="#8B4513",
    outline="black",
    width=3
)

canvas.create_arc(
    455, 400, 505, 465,
    start=270,
    extent=180,
    style="arc",
    outline="#8B4513",
    width=12
)

canvas.create_arc(
    365, 380, 440, 430,
    start=0,
    extent=180,
    style="arc",
    outline="red",
    width=6
)

canvas.create_oval(
    120, 450, 130, 460,
    fill="red",
    outline="white"
)

canvas.create_oval(
    520, 450, 530, 460,
    fill="red",
    outline="white"
)

rain = []

for i in range(120):
    x = random.randint(0, 650)
    y = random.randint(0, 550)

    drop = canvas.create_line(
        x, y,
        x - 3, y + 15,
        fill="#6fa8dc",
        width=2
    )

    rain.append(drop)

def move_rain():
    for drop in rain:
        canvas.move(drop, -2, 10)

        x1, y1, x2, y2 = canvas.coords(drop)

        if y1 > 550:
            new_x = random.randint(0, 650)
            new_y = random.randint(-50, 0)

            canvas.coords(
                drop,
                new_x, new_y,
                new_x - 3, new_y + 15
            )

    root.after(50, move_rain)

def lightning():
    canvas.configure(bg="#dce6f2")

    bolt = canvas.create_polygon(
        320, 80,
        300, 170,
        325, 165,
        305, 250,
        355, 145,
        330, 150,
        350, 80,
        fill="#fff200",
        outline="white"
    )

    root.after(
        100,
        lambda: remove_lightning(bolt)
    )

def remove_lightning(bolt):
    canvas.delete(bolt)
    canvas.configure(bg="#07152e")

    root.after(
        random.randint(3000, 7000),
        lightning
    )

move_rain()

root.after(
    random.randint(2000, 5000),
    lightning
)

root.mainloop()