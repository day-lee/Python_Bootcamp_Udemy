from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None

# ---------------------------- CONTENT SETUP ------------------------------- #
# fetch the words in a dict format to make key:value pair
try:
    df = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    word_dictionary = original_df.to_dict(orient='records')
    print("fetched from french_words.csv")

else:
    word_dictionary = df.to_dict(orient='records')
    print(f"fetched from words_to_learn.csv: {word_dictionary}")

current_card = {}

def checked():
    global current_card
    next_card()
    word_dictionary.remove(current_card)
    print(word_dictionary)

    # word_dictionary is : [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, ...]

    # any list and dict can be converted to dataframe?
    # data_dict = {
    #     "French": [item['French'] for item in word_dictionary],
    #     "English": [item['English'] for item in word_dictionary]
    # }

    # print(data_dict)
    # # saving the dict in csv file

    df = pandas.DataFrame(word_dictionary)
    df.to_csv("data/words_to_learn.csv", index=False)  # not adding index in the far left


# randint or random.choice
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(word_dictionary)
    canvas.itemconfig(title, text='French', fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text='English', fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    window.after_cancel(timer)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# if create it inside function, by the end of the function call, reference will be gone
card_background = canvas.create_image(400, 263, image=card_front_img)  # x,y coordinate not the img size
title = canvas.create_text(400, 150, text="title", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="a", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=checked)
check_button.grid(column=1, row=1)

# first screen setup with actual values
next_card()

window.mainloop()