from tkinter import *
import time

def times():
    current_time = time.strftime(clock_format.get())
    clock.config(text=current_time)
    clock.after(200, times)

def change_bg_color():
    selected_color = color_var.get()
    window.configure(bg=selected_color)

window = Tk()
window.title("Digital Clock")
window.geometry("1000x300")

clock_format = StringVar()
clock_format.set("%H:%M:%S")

format_label = Label(window, text="Select Clock Format:", font="times 14", bg="beige")
format_label.grid(row=0, column=0, padx=10, pady=10)

format_12h_radio = Radiobutton(window, text="12-Hour", variable=clock_format, value="%I:%M:%S %p", font="times 12", bg="beige")
format_12h_radio.grid(row=1, column=0, padx=10, pady=5)

format_24h_radio = Radiobutton(window, text="24-Hour", variable=clock_format, value="%H:%M:%S", font="times 12", bg="beige")
format_24h_radio.grid(row=2, column=0, padx=10, pady=5)

color_var = StringVar()
color_var.set("beige")

color_label = Label(window, text="Select Background Color:", font="times 14", bg="beige")
color_label.grid(row=0, column=1, padx=10, pady=10)

color_option_menu = OptionMenu(window, color_var, "beige", "lightsteelblue", "lavender")
color_option_menu.config(font="times 12")
color_option_menu.grid(row=1, column=1, padx=10, pady=5)

clock = Label(window, font=("times", 50, "bold"), bg=color_var.get())
clock.grid(row=2, column=2, pady=25, padx=100)
times()

title = Label(window, text="Current Time", font="times 24 bold", bg=color_var.get())
title.grid(row=0, column=2)

note = Label(window, text="    hours       minutes     seconds   ", font="times 15 bold", bg=color_var.get())
note.grid(row=3, column=2)

apply_button = Button(window, text="Apply", command=change_bg_color)
apply_button.grid(row=2, column=1, padx=10)

window.mainloop()