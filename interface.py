import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None


BASE_DIR = Path(__file__).resolve().parent

with (BASE_DIR / "games.json").open("r", encoding="utf-8") as file:
    games = json.load(file)


window = tk.Tk()
window.title("Game Catalog")
window.geometry("820x500")
window.minsize(720, 420)

title = tk.Label(window, text="My Game Catalog", font=("Arial", 18, "bold"))
title.pack(pady=(15, 8))

content = ttk.Frame(window, padding=(15, 0, 15, 15))
content.pack(fill="both", expand=True)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

columns = ("Name", "System", "Genre", "Status", "Grade")
table = ttk.Treeview(content, columns=columns, show="headings", selectmode="browse")

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=105, anchor="center")

table.column("Name", width=180, anchor="w")
table.column("Genre", width=145, anchor="w")
table.grid(row=0, column=0, sticky="nsew", padx=(0, 15))

details = ttk.LabelFrame(content, text="Selected game", padding=12)
details.grid(row=0, column=1, sticky="ns")

cover_label = tk.Label(
    details,
    text="Select a game\nto view its cover",
    width=22,
    height=15,
    justify="center",
    relief="solid",
    bg="#f0f0f0",
)
cover_label.pack()

game_name_label = ttk.Label(details, text="", font=("Arial", 11, "bold"), wraplength=190)
game_name_label.pack(pady=(10, 0))

cover_image = None


def show_selected_game(_event=None):
    """Show the cover stored in the selected game's 'cover' field."""
    global cover_image

    selection = table.selection()
    if not selection:
        return

    game = games[int(selection[0])]
    game_name_label.config(text=game["name"])
    cover_path = game.get("cover")

    if Image is None:
        cover_image = None
        cover_label.config(
            image="",
            text="Install Pillow to\nshow covers:\npip install pillow",
            width=22,
            height=15,
        )
        return

    if not cover_path or not (BASE_DIR / cover_path).is_file():
        cover_image = None
        cover_label.config(
            image="",
            text="Cover not found\n\nAdd \"cover\" to this\ngame in games.json",
            width=22,
            height=15,
        )
        return

    with Image.open(BASE_DIR / cover_path) as image:
        image.thumbnail((180, 260))
        cover_image = ImageTk.PhotoImage(image.copy())

    cover_label.config(image=cover_image, text="", width=0, height=0)


for index, game in enumerate(games):
    table.insert(
        "",
        tk.END,
        iid=str(index),
        values=(
            game["name"],
            game["system"],
            game["genre"],
            game["status"],
            game["grade"],
        ),
    )

table.bind("<<TreeviewSelect>>", show_selected_game)

window.mainloop()
