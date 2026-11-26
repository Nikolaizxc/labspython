string_of_values = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
string_of_values = list(string_of_values)
import tkinter as tk
import numpy as np


def keygen(seed):
    a = np.random.default_rng(seed)
    a = a.integers(0, 10+26-1, 5)
    end = ['','','','']
    for i in range(len(a)):
        for j in range(len(end)):
            end[j] += string_of_values[int((a[i] + ((-1) ** (j - 1)) * int(str(seed)[j - 1]) * (j > 0)) % (10 + 26))]

    end[1] = end[1][1:]
    end[2] = end[2][2:]
    end[3] = end[3][3:]
    return "-".join(end)
def click():
    text = entry.get()
    while len(text) < 3:
        text+=string_of_values[3]
    text = int(text)
    text = keygen(text)
    output_label.config(text=text)


root = tk.Tk()
root.title("keygen")
root.geometry("704x435")
photo = tk.PhotoImage(file="game_img.png")
image_label = tk.Label(root, image=photo, bg="white")
image_label.pack()
frame = tk.Frame(root, bg="black", padx=15, pady=15)
frame.place(relx=0.5, rely=0.8, anchor="center")
entry = tk.Entry(frame, bg="#222222", fg="white", insertbackground="white")
entry.pack(side="left", padx=(0, 10))

button = tk.Button(frame, text="OK", command=click ,bg="#333333", fg="white")
button.pack(side="left")
output_label = tk.Label(frame, text="", bg="black", fg="white", font=("Arial", 11))
output_label.pack(pady=(10, 0))
root.mainloop()