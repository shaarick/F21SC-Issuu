class Controller:
    """
    Controller class to facilitate interaction between Model and View

    Takes instructions from Views and runs appropriate Model methods. E.g: If "View Country & Continent" button is
    pressed in Views, it signals the controller with a document_id, which the controller then passes to the Model class
    to perform necessary logic (like filtering data) and displaying the requested information.

    Methods
    -------
    view_country(document_id: str)
        View country and continents of viewers who read the file identified with document_id

    view_browser
        View long browser names histogram

    short_browser_view
        View short browser names histogram
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

    def view_browser(self):
        """Invoke Model's method to display long name browser histogram"""
        self.model.view_browsers()

    def short_browser_view(self):
        """Invoke Model's method to display short name browser histogram"""
        self.model.view_short_browsers()
