import tkinter as tk

class NodeFrame(tk.Frame):
    def __init__(self, master, value):
        super().__init__(master)
        self.value = value
        self.label = tk.Label(self, text=str(value))
        self.label.pack()
        self.pack()

class LinkedListVisualization(tk.Tk):
    def __init__(self, values):
        super().__init__()
        self.title("Linked List Visualization")
        self.geometry("400x400")

        self.values = values
        self.current_index = 0

        self.prev_button = tk.Button(self, text="<-", command=self.prev_node)
        self.next_button = tk.Button(self, text="->", command=self.next_node)
        self.prev_button.pack()
        self.next_button.pack()

        self.node_frames = []
        for value in self.values:
            node_frame = NodeFrame(self, value)
            self.node_frames.append(node_frame)

        self.show_current_node()

    def show_current_node(self):
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

if __name__ == "__main__":
    values = [1, 2, 3, 4]  # Replace with your own values
    app = LinkedListVisualization(values)
    app.mainloop()
