import matplotlib.pyplot as plt
from data import get_data
from data import get_data_from_url
from convert import Convert


class Model:
    """
    Model class to handle all data processing tasks

    This class contains method to access, manipulate and process JSON objects to get data specified by the
    coursework specification. It is independent of the Views class and interacts with it only via the Controller.

    Parameters
    ----------
    args: dict
        Dictionary of arguments passed in the command line

    document_id: str
        Document ID that uniquely identifies file on Issuu

    Methods
    -------
    view_country
        Plots countries and continents of viewers for a given document_id

    """

    def __init__(self, args, document_id):
        self._document_id = document_id

        # In the command line, if url was mentioned use it to retrieve JSON data
        if args['url'] is not None:
            self.df = get_data_from_url(args['url'])
        # If no url was mentioned, use the locally saved small sample issuu data
        else:
            self.df = get_data()

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        """
        Validate subject document id

        Parameters
        ----------
        value: str
            String that is supposed to uniquely identify a file in the dataset

        """

        # Get files in the retrieved dataset that correspond to the given document_id
        series = self.df[self.df.subject_doc_id == value]

        # If no document_id is given, raise error
        if value is None:
            raise ValueError("No document ID entered.")
        # If no files found with given document_id, raise error
        elif len(series) == 0:
            raise KeyError("No document found.")
        # Otherwise change the Model class's current document_id to supplied value
        else:
            self._document_id = value

    def view_country(self):
        """
        View country and continent of viewers for the class's current document_id

        """
        # Filter the dataset dataframe to only get rows which correspond to the given document_id
        # i.e. get countries of viewers for this file
        doc_with_id = self.df[self.df.subject_doc_id == self.document_id]

        # Prepare two figures side by side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle(f'Histogram of Country and Continents for file:\n{self._document_id}')

        # Plot countries
        ax1.hist(doc_with_id.visitor_country)
        ax1.set_title('Countries')
        ax1.set(ylabel='Count')

        # Instantiate a converter
        converter = Convert()
        # Convert viewer countries into continent names and save new dataframe
        docs_with_continent_codes = converter.map_to_continent_code(doc_with_id)

        # Plot new dataframe with continent names
        ax2.hist(docs_with_continent_codes.visitor_country)
        ax2.set_title('Continents')

        plt.show()
