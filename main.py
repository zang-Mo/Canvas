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

root = tk.Tk()
root.title("Zangpos Sweet Home")
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

canvas.create_line(230, 190, 230, 235, fill="red", width=2)
canvas.create_line(200, 212, 260, 212, fill="red", width=2)

canvas.create_line(420, 190, 420, 235, fill="red", width=2)
canvas.create_line(390, 212, 450, 212, fill="red", width=2)

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

canvas.create_line(230, 285, 230, 330, fill="red", width=2)
canvas.create_line(200, 307, 260, 307, fill="red", width=2)

canvas.create_line(420, 285, 420, 330, fill="red", width=2)
canvas.create_line(390, 307, 450, 307, fill="red", width=2)

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

root.mainloop()