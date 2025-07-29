import tkinter as tk
import json

def launch_app():
    root = tk.Tk()
    root.title("Suivie Sportif - Acceuil")
    root.geometry("1280x720")
    display_user(root)


    root.mainloop()


def display_user(root):
    with open("data/user.json","r") as outfile:
        old_json = json.load(outfile)

    liste = tk.Listbox(root)
    n=0
    for user in old_json:
        liste.insert(n, user["name"])
        n= n+1
    liste.pack()


if __name__ == "__main__":
    launch_app()