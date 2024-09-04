import random
import time
import tkinter as tk

import pyautogui


def start_typing_with_delay():
    delay_time = delay_var.get()  
    typing_content = text_input.get("1.0", "end-1c")  
    time.sleep(delay_time) 

    for char in typing_content:
        if random.random() < 0.1:
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^')
            pyautogui.typewrite(wrong_char)
            time.sleep(random.uniform(0.05, 0.2))
            pyautogui.press('backspace')
        if char == '@':
            pyautogui.press('enter')
        else:
            pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.2))

root = tk.Tk()
root.title("GhostCoder")

text_input = tk.Text(root, height=30, width=150)
text_input.pack(pady=10)

delay_frame = tk.Frame(root)
delay_frame.pack(pady=10)
delay_label = tk.Label(delay_frame, text="ghost will start typing in: ")
delay_label.pack(side="left")
delay_var = tk.IntVar(value=10)
delay_options = [("10 sec", 10), ("20 sec", 20), ("30 sec", 30), ("60", 60)]

for text, value in delay_options:
    tk.Radiobutton(delay_frame, text=text, variable=delay_var, value=value).pack(side="left", padx=10)

start_button = tk.Button(root, text="Start off", command=start_typing_with_delay)
start_button.pack()


root.mainloop()