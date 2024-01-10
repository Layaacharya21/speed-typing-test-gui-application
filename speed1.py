import time
from tkinter import *
import random
from tkinter import messagebox

def randomtext():
    with open("words.txt", "r") as f:
        words_list = f.readlines()
    return random.choice(words_list)

def start():
    text_type = randomtext()
    lb1.config(text=text_type)
    user_input.set("")
    start_time = time.time()

    def finish_test():
        input_text = user_input.get()
        elapsed_time = time.time() - start_time
        accuracy = calculate_accuracy(text_type, input_text)
        wpm = int((len(input_text.split()) / elapsed_time) * 60)
        result.config(text=f"Words per minute: {wpm}\nAccuracy: {accuracy:.2f}%")

    root.after(1000 * 15, finish_test)

def calculate_accuracy(original, typed):
    correct_words = sum(c1 == c2 for c1, c2 in zip(original, typed))
    total_chars = len(original)
    accuracy = (correct_words / total_chars) * 100
    return accuracy

root = Tk()
root.title("Speed Typing Test")
root.geometry("500x600")

# Background Image
'''bg_image = PhotoImage(file="bg_image.png")  # Replace with your image file
background_label = Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)'''

user_input = StringVar()

lb = Label(root, text="Type the following text: ", font=("Helvetica", 14), bg="#4CAF50", fg="white")
lb.pack(padx=5, pady=10)

lb1 = Label(root, text="", font=("Helvetica", 16), bg="#4CAF50", fg="white")
lb1.pack(padx=5, pady=10)

entry = Entry(root, textvariable=user_input, font=("Helvetica", 12))
entry.pack(pady=10)

b1 = Button(root, text="Start!", command=start, bg="#008CBA", fg="white", font=("Helvetica", 12))
b1.pack(padx=5, pady=10)

result = Label(root, text="", font=("Helvetica", 14), bg="#4CAF50", fg="white")
result.pack(pady=10)

root.mainloop()
