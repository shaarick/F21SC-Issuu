import tkinter as tk
from gui.model import Model
from gui.view import View
from gui.controller import Controller


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Issuu Data Analysis")

        model = Model('')

        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
