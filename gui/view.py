import tkinter as tk
from tkinter import ttk
from gui.controller import Controller
from tkinter import filedialog
import os


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

    view_top_readers_button_clicked
        Signals the Controller that top readers list is requested

    view_listbox(readers_list: list)
        Displays Top 10 Readers in new GUI window

    view_top_documents
        Requests a dictionary of top documents from the Controller

    view_top_documents_listbox(docs: dict)
        Receives a dictionary of top documents and displays in a new window

    browse_files
        Opens file browser to choose dataset. Does not work on macOS. Works on Linux.

    view_also_likes
        Sends field data to Controller and requests a graph of all also likes documents
    """

    def __init__(self, args, parent):
        super().__init__(parent)
        self.args = args

        # Create Widgets

        # Label
        self.label = ttk.Label(self, text='Document ID:')
        self.label.grid(row=0, column=0)

        # Document ID Entry box
        self.document_id = tk.StringVar(name="Document UUID")
        self.document_entry = ttk.Entry(self, textvariable=self.document_id, width=30)
        self.document_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Label
        self.label_user = ttk.Label(self, text='User UUID:')
        self.label_user.grid(row=1, column=0)

        # User ID Entry box
        self.user_id = tk.StringVar(name="User UUID")
        self.user_id_entry = ttk.Entry(self, textvariable=self.user_id, width=30)
        self.user_id_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # File Dialog
        file_explore = tk.Button(self, text='Select Dataset', command=self.browse_files)
        file_explore.grid(row=2, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Country Button
        self.view_button = ttk.Button(self, text='2a. View Country', command=self.view_country_button_clicked)
        self.view_button.grid(row=3, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Continent Button
        self.view_button_continent = ttk.Button(self, text='2b. View Continent',
                                                command=self.view_continent_button_clicked)
        self.view_button_continent.grid(row=4, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Long Browsers Button
        self.browser_button = ttk.Button(self, text='3a. View Long Browsers',
                                         command=self.view_long_browser_button_clicked)
        self.browser_button.grid(row=5, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Short Browsers Button
        self.browser_button_short = ttk.Button(self, text='3b. View Short Browsers',
                                               command=self.view_short_browser_button_clicked)
        self.browser_button_short.grid(row=6, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Top Readers Button
        self.top_readers_button = ttk.Button(self, text='4. Top 10 Readers',
                                             command=self.view_top_readers_button_clicked)
        self.top_readers_button.grid(row=7, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View Top Documents
        self.top_documents_button = ttk.Button(self, text='5d. Top 10 Documents', command=self.view_top_documents)
        self.top_documents_button.grid(row=8, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # View 'Also Likes' Graph
        self.also_likes_graph_button = ttk.Button(self, text='6. "Also Likes" Graph', command=self.view_also_likes)
        self.also_likes_graph_button.grid(row=9, column=0, columnspan=2, padx=3, sticky=tk.NSEW)

        # Message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=10, column=0, columnspan=2, sticky=tk.NSEW)

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
        self.message_label.after(5000, self.hide_message)
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
        # Hide message after 5 seconds
        self.message_label.after(5000, self.hide_message)

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

    def view_listbox(self, readers_list):
        """
        Displays Top 10 Readers in new GUI window

        Unlike other GUI methods, this one works in reserve order. When Top Readers button is clicked,
        it asks Controller to get the top readers from Model and then this function is invoked with that list.

        Parameters
        ----------
        readers_list: list
            List containing top 10 readers and their read times
        """
        # Create a new tkinter window to display top readers
        readers_window = tk.Tk()
        readers_window.title('Top 10 Readers')
        # Create Tree view widget and add columns/headings
        columns = ('visitor_uuid', 'read_time')
        tree = ttk.Treeview(readers_window, columns=columns, show='headings')
        tree.heading('visitor_uuid', text='Visitor UUID')
        tree.heading('read_time', text='Reading time (seconds)')

        # Loop over reader list and add to tree widget
        for reader in readers_list:
            tree.insert('', tk.END, values=reader)
        tree.grid(row=0, column=0, sticky='nsew')
        # Run the window containing tree widget
        readers_window.mainloop()

    def view_top_documents(self):
        """Signals to controller that top documents were requested"""
        if self.controller:
            self.controller.view_top_documents(self.document_id.get(), self.user_id.get())

    def browse_files(self):
        """Create a file browser to choose a new dataset

        Warnings
        --------
        DOES NOT WORK ON macOS. This has nothing to do with my code, but with tkinter and macOS.
        see:
        https://bugs.python.org/issue44828
        https://www.mail-archive.com/search?l=python-bugs-list@python.org&q=subject:%22%5C%5Bissue44828%5C%5D+Using+tkinter.filedialog+crashes+on+macOS+Python+3.9.6%22&o=newest&f=1

        Notes
        -----
        Working fine on Linux. Tested on Ubuntu 20.4
        """
        direc = os.getcwd()
        filename = filedialog.askopenfilename(initialdir=direc, title='Select a File',
                                              filetypes=[("JSON Files", "*.json")])
        if self.controller:
            self.controller.select_data(filename)

    def view_top_documents_listbox(self, dic):
        """
        Displays Top 10 Documents in a new GUI window

        Parameters
        ----------
        dic
            sorted dictionary containing documents with their reader count

        """
        # Create a new tkinter window to display top documents
        documents_window = tk.Tk()
        documents_window.title('Top 10 Documents')

        # Create Tree view widget and add columns/headings
        columns = ('document_uuid', 'num_readers')
        tree = ttk.Treeview(documents_window, columns=columns, show='headings')
        tree.heading('document_uuid', text='Document UUID (last 4 digit)')
        tree.heading('num_readers', text='Number of Readers')

        # Loop over reader list and add to tree widget
        for key, value in dic.items():
            tree.insert('', tk.END, values=(key, value))
        tree.grid(row=0, column=0, sticky='nsew')
        # Run the window containing tree widget
        documents_window.mainloop()

    def view_also_likes(self):
        """Signals to controller that Also Likes Graph was requested"""
        if self.controller:
            self.controller.view_also_likes(self.document_id.get(), self.user_id.get())
