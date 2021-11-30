import matplotlib.pyplot as plt
from data import get_data
from data import get_data_from_url
from convert import Convert
import numpy as np
from matplotlib.ticker import PercentFormatter


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

    view_browsers
        Plots long name browser histogram for entire dataset

    view_short_browsers
        Plots short name browser histogram for entire dataset
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

    def view_browsers(self):
        """
        Display Histogram of each browser used in the dataset

        Displays histogram of long browser names, i.e. the full visitor_useragent value
        """

        # Prepare figure and axis
        fig, ax1 = plt.subplots(1, 1, figsize=(20, 6))
        fig.suptitle('Histogram of Long Browser Names')

        # Plot long names
        long_name_list = list(self.df.visitor_useragent)
        # ax1.hist(long_name_list, orientation='horizontal')
        ax1.hist(long_name_list)
        ax1.set_title('User Agent')
        plt.show()

    def view_short_browsers(self):
        """
        Display Histogram of each browser used in the dataset

        Retrieves all browsers used, then processes their long string
        to return only the short browser name which is then used to plot Histogram

        """
        # Get the useragent string, split it at '/' since all browser names have that followed by their versions.
        # Once we have the split string, browser name is always the first element so we access it using the 0 index.
        self.df['browser'] = self.df.apply(lambda row: row['visitor_useragent'].split('/')[0], axis=1)

        # In the sample small json file saved locally, UCWEB and Dalvik are mentioned in the histogram but appear
        # almost as 0%. Checked their number of instances informally without len here. UCWEB appears once, Davlik 5
        # times. So their proportion is too low to show up on graph.

        # print(self.df.browser[self.df.browser == 'UCWEB'])
        # print(self.df.browser[self.df.browser == 'Dalvik'])

        # Prepare figure and axis
        fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
        fig.suptitle('Histogram of Short Browser Names')

        # Divide each category by total observations to get percentage
        ax1.hist(self.df.browser, weights=np.ones(len(self.df.browser)) / len(self.df.browser))
        ax1.set(ylabel='Percentage')
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.show()
