import tkinter as tk
from tkinter import ttk
from .controller import Controller


class View(ttk.Frame):
    """
    Class to handle all GUI related tasks and elements

    This class is independent of Model (i.e. our dataset) but interacts with it through the Controller.
    It creates the main GUI window used by our application, and processes GUI tasks such as button clicks,
    which signal Controller (and then Model), as well as displaying errors and taking input.

    Parameters
    ----------
    args: dict
        Dictionary of arguments passed in the command line

    parent: tkinter.Tk
        root window upon which to add this View Frame will be added

    Methods
    -------
    set_controller(value: Controller)
        Sets the controller for this View Frame. All signals (clicks, etc.) will be sent to this controller.

    show_error(message: str)
        Displays error message on the GUI

    show_success(message: str)
        Displays success message on the GUI

    hide_message
        Hides any messages being displayed on the GUI

    view_country_button_clicked
        Signals the controller that country histograms were requested

    view_continent_button_clicked
        Signals the controller that continent histograms were requested

    view_long_browser_button_clicked
        Signals the Controller that long browser histogram is requested

    view_short_browser_button_clicked
        Signals the Controller that short browser histogram is requested

    readers_button_clicked
        Signals the Controller that top readers list is requested
    """

    def __init__(self, args, parent):
        super().__init__(parent)
        self.args = args

        # Create Widgets

        # Label
        self.label = ttk.Label(self, text='Document ID:')
        self.label.grid(row=1, column=0)

        # Document ID Entry box
        self.document_id = tk.StringVar(name="Document UUID")
        self.document_entry = ttk.Entry(self, textvariable=self.document_id, width=30)
        self.document_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # Label
        self.label_user = ttk.Label(self, text='User UUID:')
        self.label_user.grid(row=2, column=0)

        # User ID Entry box
        self.user_id = tk.StringVar(name="User UUID")
        self.user_id = ttk.Entry(self, textvariable=self.user_id, width=30)
        self.user_id.grid(row=2, column=1, sticky=tk.NSEW)

        # View Country Button
        self.view_button = ttk.Button(self, text='View Country', command=self.view_country_button_clicked)
        self.view_button.grid(row=3, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Continent Button
        self.view_button_continent = ttk.Button(self, text='View Continent', command=self.view_continent_button_clicked)
        self.view_button_continent.grid(row=4, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Long Browsers Button
        self.browser_button = ttk.Button(self, text='View Long Browsers', command=self.view_long_browser_button_clicked)
        self.browser_button.grid(row=5, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Short Browsers Button
        self.browser_button_short = ttk.Button(self, text='View Short Browsers',
                                               command=self.view_short_browser_button_clicked)
        self.browser_button_short.grid(row=6, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Top Readers Button
        self.top_readers_button = ttk.Button(self, text='Top 10 Readers',
                                             command=self.view_top_readers_button_clicked)
        self.top_readers_button.grid(row=7, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # Message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=8, column=0, columnspan=2, sticky=tk.NSEW)

        # Set Controller
        self.controller = None

    def set_controller(self, controller):
        """
        Sets the controller for this View Frame

        Once the controller is set, check if command line arguments received at the time of this Frame's
        instantiation contained any tasks that need to be automated. E.g: if document_id and task 2 are
        present, then country/continent histogram will automatically be generated.
        Parameters
        ----------
        controller: Controller
            The controller which needs to be assigned to this frame
        """
        self.controller = controller

    def show_error(self, message):
        """
        Display error message on GUI

        Parameters
        ----------
        message: str
            Error message that needs to be displayed

        """
        # Change message_label to the message argument
        self.message_label['text'] = message
        # Change message colour to red
        self.message_label['foreground'] = 'red'
        # After 3 seconds, hide the error message
        self.message_label.after(3000, self.hide_message)
        # Change the text in the entry box to red to signal erroneous entry
        self.document_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Display success message on the GUI
        Parameters
        ----------
        message: str
            Message to be displayed on the GUI

        """
        # Change message_label to the message argument
        self.message_label['text'] = message
        # Change text colour to green to signal valid input
        self.message_label['foreground'] = 'green'
        # Hide message after 3 seconds
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.document_entry['foreground'] = 'black'
        self.document_id.set('')

    def hide_message(self):
        """Hide any kind of messages being displayed on the GUI"""
        self.message_label['text'] = ''

    def view_country_button_clicked(self):
        """
        Signals controller that country histograms were requested

        Passes text in entry box to controller, which then passes it to Model so text can be validated and histograms
        can be displayed.

        """
        if self.controller:
            self.controller.view_country(self.document_id.get())

    def view_continent_button_clicked(self):
        """
        Signals controller that continent histograms were requested

        Passes text in entry box to controller, which then passes it to Model so text can be validated and histograms
        can be displayed.

        """
        if self.controller:
            self.controller.view_continent(self.document_id.get())

    def view_long_browser_button_clicked(self):
        """Signals controller that long browser histogram is requested"""
        if self.controller:
            self.controller.view_long_browsers()

    def view_short_browser_button_clicked(self):
        """Signals controller that short browser histogram is requested"""
        if self.controller:
            self.controller.view_short_browsers()

    def view_top_readers_button_clicked(self):
        """Signals controller that top readers list is requested"""
        if self.controller:
            self.controller.view_top_readers()
