import tkinter as tk
from gui.model import Model
from gui.view import View
from gui.controller import Controller


class App(tk.Tk):
    """
    Create a Tkinter root window object for Issuu Data Analysis GUI

    The MVC pattern has been used to implement this GUI. Model controls the logic of data related operations,
    view controls GUI elements. Both of them are independent and do not interact directly with each other.
    Their interaction is governed by the Controller.

    """
    def __init__(self, args: dict):
        super().__init__()
        self.title("Issuu Data Analysis")

        # Create model and pass the command line options to it
        model = Model(args, '')

        # Create views and pass the command line options to it
        view = View(args, self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # Create controller and pass both model and view to it
        controller = Controller(model, view)

        # Set the controller for views
        view.set_controller(controller)
