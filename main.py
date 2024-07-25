import tkinter as tk
from tkinter import ttk


class CounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Counter App")

        self.count = tk.IntVar(value=0)

        self.window = ttk.Frame(self.master, padding=50)
        self.window.grid(padx=10, pady=10)

        self.label = ttk.Label(self.window, textvariable=self.count)
        self.label.grid(column=0, row=0, pady=5)

        self.button = ttk.Button(self.window, text="Count", command=self.counter)
        self.button.grid(column=0, row=1, pady=5)

    def counter(self):
        self.count.set(self.count.get() + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
