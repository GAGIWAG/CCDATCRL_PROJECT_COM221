import tkinter as tk

# Create the main window
root = tk.Tk()

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the desired window size as a fraction of the screen dimensions
window_width = int(screen_width * 0.8)  # Adjust the fraction as needed
window_height = int(screen_height * 0.6)  # Adjust the fraction as needed

# Set the window size and position it in the center of the screen
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window's geometry
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Add your widgets and code here

# Start the Tkinter main loop
root.mainloop()
