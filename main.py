import tkinter as tk
from tkinter import messagebox

import spotify_play


def yes_clicked():
    player = spotify_play.SpotifyPlayer()
    player.play_when_is_sad()
    messagebox.showinfo("Result", "Hope this helps you feel better!")


def no_clicked():
    messagebox.showinfo("Result", "Glad to hear you're not sad!")
    sleep_time = 1
    root.after(sleep_time * 1000, root.destroy)


root = tk.Tk()
root.title("Mood Checker")
root.geometry("300x150")

question_label = tk.Label(
    root,
    text="Are you sad?",
    font=("Arial", 14)
)
question_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

yes_button = tk.Button(
    button_frame,
    text="Yes",
    width=10,
    command=yes_clicked
)
yes_button.pack(side=tk.LEFT, padx=10)

no_button = tk.Button(
    button_frame,
    text="No",
    width=10,
    command=no_clicked
)
no_button.pack(side=tk.LEFT, padx=10)

root.mainloop()