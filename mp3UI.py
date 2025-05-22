from customtkinter import *
from tkinter import Menu

app = CTk()
set_appearance_mode("dark")
app.title("MP3 Player")
app.geometry("400x350")

frame = CTkFrame(app)
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

songframe = CTkFrame(frame)
songframe.place(relx=0.5, rely=0.32, anchor="center", relwidth=0.85, relheight=0.6)
# картинка
songcover = CTkCanvas(songframe, width=230, height=130)
songcover.place(relx=0.5, rely=0.45, anchor="center")

# назва пісні
title_label = CTkLabel(songframe, text="Song Title", font=("Arial", 16))
title_label.place(relx=0.5, rely=0.92, anchor="center")

# progress bar
progressbar = CTkProgressBar(frame, width=300)
progressbar.set(0)
progressbar.place(relx=0.5, rely=0.65, anchor="center")

# кнопки
button_frame = CTkFrame(frame)
button_frame.place(relx=0.5, rely=0.75, anchor="center")

prev_button = CTkButton(button_frame, text="⏮", font=("Arial", 20), width=50)
prev_button.grid(row=0, column=0, padx=5)


def play():
    play_button.configure(text="⏸")


play_button = CTkButton(button_frame, text="▶", font=("Arial", 25), command=play, width=60)
play_button.grid(row=0, column=1, padx=5)

next_button = CTkButton(button_frame, text="⏭", font=("Arial", 20), width=50)
next_button.grid(row=0, column=4, padx=5)

# звук
volume_slider = CTkSlider(frame, from_=0, to=100, orientation="vertical")
volume_slider.set(50)
volume_slider.place(relx=0.96, rely=0.4, anchor="center", relheight=0.75)


def addsongwindow():
    addsong_window = CTkToplevel()
    addsong_window.title = "Add song"
    addsong_window.geometry("250x150")
    # назва пісні
    songname_label = CTkLabel(addsong_window, text="Song name:")
    songname_label.place(relx=0.17, rely=0.15, anchor="center")
    songname_entry = CTkEntry(addsong_window)
    songname_entry.place(relx=0.65, rely=0.15, anchor="center", relwidth=0.6)
    # картинка пісні
    songpic_label = CTkLabel(addsong_window, text="Song picture:")
    songpic_label.place(relx=0.17, rely=0.35, anchor="center")
    songpic_entry = CTkEntry(addsong_window)
    songpic_entry.place(relx=0.65, rely=0.35, anchor="center", relwidth=0.6)
    # пісня
    songfile_label = CTkLabel(addsong_window, text="Song file:")
    songfile_label.place(relx=0.17, rely=0.55, anchor="center")
    songfile_entry = CTkEntry(addsong_window)
    songfile_entry.place(relx=0.65, rely=0.55, anchor="center", relwidth=0.6)
    # done
    done_button = CTkButton(addsong_window, text="Done", font=("Arial", 20))
    done_button.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.6, command=addsong)


addsong_button = CTkButton(frame, text="+", font=("Arial", 30), width=120)
addsong_button.place(relx=0.5, rely=0.9, anchor="center")


def set_theme(theme):
    if theme == "light":
        set_appearance_mode("light")
    elif theme == "dark":
        set_appearance_mode("dark")


# меню
menubar = Menu(app)
theme_menu = Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
menubar.add_cascade(label="Тема", menu=theme_menu)

app.config(menu=menubar)

app.mainloop()