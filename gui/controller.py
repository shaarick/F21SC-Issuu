class Controller:
    """
    Controller class to facilitate interaction between Model and View classes

    Takes instructions from Views and runs appropriate Model methods. E.g: If "View Country & Continent" button is
    pressed in Views, it signals the controller with a document_id, which the controller then passes to the Model class
    to perform necessary logic (like filtering data) and displaying the requested information.

    Methods
    -------
    view_country(document_id: str)
        View countries of viewers who read the file identified with document_id

    view_continent(document_id: str)
        View continents of viewers who read the file identified with document_id

    view_long_browsers
        View long browser names histogram

    view_short_browsers
        View short browser names histogram

    view_top_readers
        View top 10 readers
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def view_country(self, document_id):
        """
        View country of viewers who read document_id file

        Parameters
        ----------
        document_id: str
            unique identification for file on Issuu

        """
        try:
            # Set the model's current document ID
            self.model.document_id = document_id
            # Show a success message indicating document was found
            self.view.show_success("Document found!")
            # Invoke the model's method which shows country and continent for its current document_id
            self.model.view_country()

        except (KeyError, ValueError) as error:
            # If no document found or invalid ID given as input, invoke the View class's method to display
            # this error on the GUI window
            self.view.show_error(error)

    def view_continent(self, document_id):
        """
        View continent of viewers who read document_id file

        Parameters
        ----------
        document_id: str
            unique identification for file on Issuu

        """
        try:
            # Set the model's current document ID
            self.model.document_id = document_id
            # Show a success message indicating document was found
            self.view.show_success("Document found!")
            # Invoke the model's method which shows country and continent for its current document_id
            self.model.view_continent()

        except (KeyError, ValueError) as error:
            # If no document found or invalid ID given as input, invoke the View class's method to display
            # this error on the GUI window
            self.view.show_error(error)

    def view_long_browsers(self):
        """Invoke Model's method to display long name browser histogram"""
        self.model.view_long_browsers()

    def view_short_browsers(self):
        """Invoke Model's method to display short name browser histogram"""
        self.model.view_short_browsers()

    def view_top_readers(self):
        """Invoke Model's method to display top 10 readers and View them as well"""
        # Model returns dataframe of top readers
        top_readers = self.model.view_top_readers()
        # Convert above dataframe to a list
        top_readers_list = top_readers.values.tolist()
        # Use View method to display top readers in GUI
        self.view.view_listbox(top_readers_list)
