import tkinter as tk

# Create a list to keep track of frames
frame_stack = []

def create_frame():        
    frame = tk.Frame(window)
    frame.pack()
    
    label = tk.Label(frame, text="Frame Created!")
    label.pack()
    
    # Add the created frame to the stack
    frame_stack.append(frame)

def go_back():
    if frame_stack:
        # Remove and destroy the current frame
        current_frame = frame_stack.pop()
        current_frame.destroy()

        # If there's a previous frame, show it
        if frame_stack:
            previous_frame = frame_stack[-1]
            previous_frame.pack()

window = tk.Tk()
window.title("Tkinter Frame Example")

button_create = tk.Button(window, text="Create Frame", command=create_frame)
button_create.pack()

button_back = tk.Button(window, text="Previous", command=go_back)
button_back.pack()

window.mainloop()
