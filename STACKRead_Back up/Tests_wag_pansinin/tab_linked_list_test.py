import tkinter as tk

class NodeFrame(tk.Frame):
    def __init__(self, master, value):
        super().__init__(master)
        self.value = value
        self.label = tk.Label(self, text=str(value))
        self.label.pack()
        self.pack()

class LinkedListVisualization(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linked List Visualization")
        self.geometry("400x400")

        self.values = []
        self.current_index = 0

        self.prev_button = tk.Button(self, text="Previous", command=self.prev_node)
        self.next_button = tk.Button(self, text="Next", command=self.next_node)
        self.prev_button.pack()
        self.next_button.pack()

        self.add_entry = tk.Entry(self)
        self.add_button = tk.Button(self, text="Add Value", command=self.add_node)
        self.add_entry.pack()
        self.add_button.pack()

        self.node_frames = []
        
        self.show_current_node()

    def show_current_node(self):
        if self.values:
            for frame in self.node_frames:
                frame.pack_forget()
            self.node_frames[self.current_index].pack()

    def prev_node(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_node()

    def next_node(self):
        if self.current_index < len(self.values) - 1:
            self.current_index += 1
            self.show_current_node()

    def add_node(self):
        new_value = self.add_entry.get()
        if new_value:
            self.values.append(new_value)
            self.node_frames.append(NodeFrame(self, new_value))
            self.add_entry.delete(0, tk.END)
            self.current_index = len(self.values) - 1
            self.show_current_node()

if __name__ == "__main__":
    app = LinkedListVisualization()
    app.mainloop()
