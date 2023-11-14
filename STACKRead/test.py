import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def show_image():
    # Get the image path from the Entry widget
    image_path = entry.get()

    try:
        # Load the image
        original_image = Image.open(image_path)

        # Resize the image if needed
        # You can adjust the size according to your requirements
        resized_image = original_image.resize((300, 200))

        # Create a Tkinter PhotoImage object from the resized image
        image = ImageTk.PhotoImage(resized_image)

        # Display the image on a label
        image_label.config(image=image)
        image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected
    except Exception as e:
        # Handle image loading errors
        print(f"Error: {e}")
        image_label.config(image=None)
        image_label.image = None

def browse_image():
    # Open a file dialog to choose an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    
    # Update the Entry widget with the selected file path
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Create an Entry widget for the file path
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to browse for an image
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

# Create a button to trigger image display
show_button = tk.Button(root, text="Show Image", command=show_image)
show_button.pack(pady=5)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Run the Tkinter event loop
root.mainloop()
