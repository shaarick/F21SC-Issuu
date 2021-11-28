import tkinter as tk
from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create Widgets

        # Label
        self.label = ttk.Label(self, text='Document ID:')
        self.label.grid(row=1, column=0)

        # Document ID Entry
        self.document_id = tk.StringVar(name="Enter Document ID")
        self.document_entry = ttk.Entry(self, textvariable=self.document_id, width=30)
        self.document_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # View Button
        self.view_button = ttk.Button(self, text='View', command=self.view_button_clicked)
        self.view_button.grid(row=1, column=3, padx=10)

        # Message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # Set Controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def view_button_clicked(self):
        if self.controller:
            self.controller.view_country(self.document_id.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.document_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.document_entry['foreground'] = 'black'
        self.document_id.set('')

    def hide_message(self):
        self.message_label['text'] = ''
