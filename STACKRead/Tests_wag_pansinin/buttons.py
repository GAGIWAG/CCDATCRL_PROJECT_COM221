import tkinter as tk

def toggle_panel():
    if panel_frame.winfo_viewable():
        panel_frame.pack_forget()
        stop_animations()
    else:
        panel_frame.pack(side="left", fill="y")
        start_animations()

def toggle_button(button_num):
    for i in range(1, 6):
        if i == button_num:
            buttons[i-1].config(relief="sunken")
            labels[i-1].config(fg="red")
        else:
            buttons[i-1].config(relief="raised")
            labels[i-1].config(fg="black")

def animate_button_color_change(button_index, color, interval_ms):
    if buttons[button_index].cget("relief") == "sunken":
        labels[button_index].config(fg=color)
        root.after(interval_ms, animate_button_color_change, button_index, "black", interval_ms)
    else:
        labels[button_index].config(fg="black")

def start_animations():
    for i in range(5):
        animate_button_color_change(i, "red", int(1000 / 24))

def stop_animations():
    for i in range(5):
        root.after_cancel(animate_button_color_change, i)

root = tk.Tk()
root.title("Collapsible Side Panel")

# Create a button to toggle the panel
panel_button = tk.Button(root, text="Toggle Panel", command=toggle_panel)
panel_button.pack(padx=10, pady=10, side="left")

# Create a frame for the side panel
panel_frame = tk.Frame(root, bg="lightgray", width=200)

# Define button text
button_texts = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5"]

# Create buttons with labels inside the panel frame
buttons = []
labels = []
for i in range(5):
    button = tk.Button(panel_frame, text=button_texts[i], command=lambda i=i+1: toggle_button(i))
    button_label = tk.Label(panel_frame, text=f"{button_texts[i]} Label")
    button_label.pack()
    button.pack(padx=10, pady=10, fill="x")
    buttons.append(button)
    labels.append(button_label)

# Initially press the first button
toggle_button(1)

root.mainloop()
