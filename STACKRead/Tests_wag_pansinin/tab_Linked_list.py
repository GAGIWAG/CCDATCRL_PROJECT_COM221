import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Implementation")
        self.ll = LinkedList()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Element", command=self.add_element)
        self.add_button.pack()

        self.display_button = tk.Button(root, text="Display Elements", command=self.display_elements)
        self.display_button.pack()

        self.delete_button = tk.Button(root, text="Delete Element", command=self.delete_element)
        self.delete_button.pack()

    def add_element(self):
        data = self.entry.get()
        try:
            data = int(data)
            self.ll.append(data)
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")

    def display_elements(self):
        elements = self.ll.display()
        if elements:
            message = "Linked List Elements: " + " -> ".join(map(str, elements))
            messagebox.showinfo("Linked List", message)
        else:
            messagebox.showinfo("Linked List", "The list is empty.")

    def delete_element(self):
        data = self.entry.get()
        try:
            data = int(data)
            self.ll.delete(data)
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()
