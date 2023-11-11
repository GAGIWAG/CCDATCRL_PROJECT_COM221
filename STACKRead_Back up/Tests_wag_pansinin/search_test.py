import tkinter as tk

def button_click():
    entry_text = entry.get()
    result_label.config(text="You entered: " + entry_text)

window = tk.Tk()
window.title("Entry with Button")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Click Me", command=button_click)
button.place(relx=0.95, rely=0.5, anchor="e")

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
