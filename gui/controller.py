class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def view_country(self, document_id):
        try:
            self.model.document_id = document_id
            self.model.view_country()

        except (KeyError, ValueError) as error:
            self.view.show_error(error)
