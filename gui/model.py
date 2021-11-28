import matplotlib.pyplot as plt
from data import get_data


class Model:
    def __init__(self, document_id):
        self._document_id = document_id
        self.df = get_data()

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        """Validate subject document id"""
        series = self.df[self.df.subject_doc_id == value]

        if value is None:
            raise ValueError("No document ID entered.")
        elif len(series) == 0:
            raise KeyError("No document found.")
        else:
            self._document_id = value

    def view_country(self):
        doc_with_id = self.df[self.df.subject_doc_id == self.document_id]
        plt.hist(doc_with_id.visitor_country)
        plt.ylabel("Count")
        plt.xlabel("Countries")
        plt.show()
