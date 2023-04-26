from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    orig_data = pandas.read_csv('spanish_words.csv')
    to_learn = orig_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

current_card = {}

# ---------------------------- NEXT DATA ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Spanish', fill='black')
    canvas.itemconfig(card_word, text=current_card['SPANISH'], fill='black')
    canvas.itemconfig(canvas_img, image=bg)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv('words_to_learn.csv', index=False)


# ---------------------------- SAVING ------------------------------- #

# ---------------------------- CARD FLIP ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card['ENGLISH'], fill="white")
    canvas.itemconfig(canvas_img, image=bg1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('FLASHY')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, height=526, width=810, highlightthickness=0)

bg = PhotoImage(file='card_front.png')
bg1 = PhotoImage(file='card_back.png')
canvas_img = canvas.create_image(402, 262, image=bg)

card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

img1 = PhotoImage(file='wrong.png')
button1 = Button(image=img1, highlightthickness=0, command=next_card)
button1.grid(row=1, column=0)

img2 = PhotoImage(file='right.png')
button2 = Button(image=img2, highlightthickness=0, command=is_known)
button2.grid(row=1, column=1)

next_card()

window.mainloop()
