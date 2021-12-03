import matplotlib.pyplot as plt
import pandas as pd
from data import get_data
from data import get_data_from_url
from convert import Convert
import numpy as np
from matplotlib.ticker import PercentFormatter
from timer import timer
from graphviz import Digraph
from sorters import desc


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
    view_country(doc_uuid: str)
        Plots countries of viewers for a given document_id

    view_continent(doc_uuid: str)
        Plots continents of viewers for a given document_id

    view_long_browsers
        Plots long name browser histogram for entire dataset

    view_short_browsers
        Plots short name browser histogram for entire dataset

    view_top_readers
        Displays top 10 readers for the entire dataset

    readers_of_document(doc_uuid: str)
        Returns all readers of a document

    documents_read_by_user(user_uuid: str)
        Returns all documents_uuids read by a user

    counter(readers:list, doc_id:str, user_id:str)
        Function meant to use as a higher order counter

    view_top_documents(doc_uuid: str, user_uuid: str, sort: func)
        Returns the top 10 also like documents

    view_also_likes(doc_uuid: str, user_uuid: str)
        Graphs all also like documents

    """

    def __init__(self, args, document_id):
        # Make document_id private so values can be validated before setting
        self._document_id = document_id
        self.args = args
        # In the command line, if url was mentioned use it to retrieve JSON data
        if args['url'] is not None:
            self.df = get_data_from_url(args['url'])
        # If no url was mentioned, use the file name passed in CLI
        else:
            self.current_filename = args['file_name']
            self.df = get_data(self.current_filename)

    def select_data(self, filename):
        self.df = get_data(filename)

    @property
    def document_id(self):
        """Getter for _document_id"""
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
            raise KeyError("No document found with that UUID found.")
        # Otherwise change the Model class's current document_id to supplied value
        else:
            self._document_id = value

    def view_country(self, viewing=True):
        """
        View country of viewers for the class's current document_id

        Parameters
        ----------
        viewing: Bool, optional
            Default is True. This method returns a dataframe where only records corresponding to the Model class's
            document_id are present. That new df is used by view_continents method so that it does not have to filter
            data again, but if we use this method directly it will display the country histogram too. The bool value
            prevents unwanted graph.

        """
        # If running the app without the GUI set the document id manually (otherwise View does it via Controller)
        if self.args['task'] != '7':
            self.document_id = self.args['document_uuid']

        # Filter the dataset dataframe to only get rows which correspond to the given document_id
        # i.e. get countries of viewers for this file
        doc_with_id = self.df[self.df.subject_doc_id == self.document_id]

        if viewing:
            # Prepare two figures side by side
            fig, ax1 = plt.subplots(1, 1, figsize=(6, 6))
            fig.suptitle(f'Histogram of Countries for file:\n{self._document_id}')

            # Plot countries
            ax1.hist(doc_with_id.visitor_country)
            ax1.set_title('Countries')
            ax1.set(ylabel='Count')
            plt.show()

        return doc_with_id

    def view_continent(self):
        """View continent of viewers for the class's current document_id"""

        # If running the app without the GUI set the document id manually (otherwise View does it via Controller)
        if self.args['task'] != '7':
            self.document_id = self.args['document_uuid']

        # Prepare two figures side by side
        fig, ax2 = plt.subplots(1, 1, figsize=(6, 6))
        fig.suptitle(f'Histogram of Continents for file:\n{self._document_id}')

        # Use data from view countries function to get the country dataframe
        doc_with_countries = self.view_country(viewing=False)

        # Instantiate a converter
        converter = Convert()
        # Convert viewer countries into continent names and save new dataframe
        docs_with_continent_codes = converter.map_to_continent_code(doc_with_countries)

        # Plot new dataframe with continent names
        ax2.hist(docs_with_continent_codes.visitor_country)
        ax2.set_title('Continents')
        ax2.set(ylabel='Count')

        plt.show()

    def view_long_browsers(self):
        """
        Display Histogram of each browser used in the dataset

        Displays histogram of long browser names, i.e. the full visitor_useragent string
        """
        print("Creating Histogram...")
        # Prepare figure and axis
        fig, ax1 = plt.subplots(1, 1, figsize=(10, 6))
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
        print("Creating Histogram...")
        # Get the useragent string, split it at '/' since all browser names have that followed by their versions.
        # Once we have the split string, browser name is always the first element so we access it using the 0 index.
        self.df['browser'] = self.df.apply(lambda row: row['visitor_useragent'].split('/')[0], axis=1)

        # Prepare figure and axis
        fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
        fig.suptitle('Histogram of Short Browser Names')

        # Divide each category by total observations to get percentage
        ax1.hist(self.df.browser, weights=np.ones(len(self.df.browser)) / len(self.df.browser))
        ax1.set(ylabel='Percentage')
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.show()

    @timer
    def view_top_readers(self):
        """View Top 10 Readers for the dataset according to their page read time"""
        data = []
        # Group dataset by visitor_uuid
        groups = self.df.groupby('visitor_uuid')
        for group_key, group_value in groups:
            # Separate into groups using uuid
            group = groups.get_group(group_key).reset_index(drop=True)
            # Sum their page read time column and convert it to seconds
            total_read_time_seconds = (group.event_readtime.sum()) / 1000
            # Append uuid and read time to data list above
            data.append([group.visitor_uuid.iloc[0], total_read_time_seconds])

        # Convert data list into dataframe
        readers_df = pd.DataFrame(data, columns=['visitor_uuid', 'read_time'])
        # Sort by read time values in descending order
        readers_df.sort_values(by=['read_time'], ascending=False, inplace=True)
        readers_df.rename(columns={'read_time': 'read time (seconds)'}, inplace=True)
        # Get the top ten readers, print and return them. The returned values are used for GUI if requested
        top_10_readers = readers_df.iloc[0:10]
        print(top_10_readers)
        return top_10_readers

    def readers_of_document(self, doc_uuid: str):
        """For a given document_uuid, return all visitor_uuid who read the document"""
        df = self.df[self.df['subject_doc_id'] == doc_uuid]
        df = df[df['subject_type'] == 'doc']
        df = df[df['event_type'] == 'read']
        if len(df) == 0:
            raise ValueError("No document found")
        return list(df['visitor_uuid'].unique())

    def documents_read_by_user(self, user_uuid: str):
        """For a given user_uuid, return all the document_uuids that have been read"""
        df = self.df[self.df.visitor_uuid == user_uuid]
        df = df[df['subject_type'] == 'doc']
        df = df[df['event_type'] == 'read']
        df = df[df['env_type'] == 'reader']
        if len(df) == 0:
            raise ValueError("No user found")
        # Some doc_ids were NaN weirdly enough, so had to drop those.
        df = df[df['subject_doc_id'].notna()]
        # Avoiding sets here because for large series df.unique() is faster
        unique_df = df['subject_doc_id'].unique()
        unique_list = list(unique_df)
        # Abbreviate document IDs to last four characters
        unique_list_with_abbreviated_names = list(map(lambda x: x[-4:], unique_list))
        return unique_list_with_abbreviated_names

    # Higher order function
    def counter(self, readers: list, doc_uuid: str, user_uuid=None) -> dict:
        # Empty dictionary to contain frequency of documents
        records = {}
        for reader in readers:
            # If current user is the same as input reader, we do not count their 'vote'/'read' for non-input documents.
            if user_uuid is not None and reader[-4:] == user_uuid[-4:]:
                continue
            # All documents read by this user
            documents_read = self.documents_read_by_user(reader)

            # Check for each document
            for document in documents_read:
                # If it is not input document
                if document != doc_uuid[-4:]:
                    # And not present in records dictionary
                    if document not in records:
                        # Add document to dic with count as 1
                        records[document] = 1
                    else:
                        # If present in dictionary, increment document count
                        records[document] += 1

        return records

    def view_top_documents(self, doc_uuid: str, user_uuid: str = None, sort=None):
        """ Shows top documents that were also read by users who read doc_uuid"""

        # All readers of input document
        readers = self.readers_of_document(doc_uuid)

        if sort is None:
            sort_type = '(alphabetical on keys)'
            # Generate records of document as keys and their count as values
            records = self.counter(readers, doc_uuid, user_uuid)
            # Sort the dictionary using default params, i.e. on keys of the dic and alphabetically
            sorted_dic = dict(sorted(records.items()))

        # Only implementing one higher order sort function, so else automatically means that
        else:
            sort_type = '(descending on values)'
            # Sort the dictionary using values, i.e. counts and in descending order
            # desc takes in all readers, a function to count them, and ID values
            sorted_dic = desc(readers, self.counter, doc_uuid, user_uuid)

        # If the sorted dictionary has more then 10 documents, we need to trim it
        if len(sorted_dic) > 10:
            # Create new dictionary
            top_documents_dictionary = {}
            # This iteration goes from first element to last. E.g for descending sort, it will iterate from
            # max count to lowest.
            for document, count in sorted_dic.items():
                # Get key, value pair. If the new dic does not have more than 10 entries, append the new one
                if len(top_documents_dictionary) < 10:
                    top_documents_dictionary[document] = count
                else:
                    # Once we have 10 entries break the loop
                    break
        else:
            top_documents_dictionary = sorted_dic

        print('Top 10 Documents ' + sort_type)
        print('document_uuid    number of readers')
        for key, value in top_documents_dictionary.items():
            print(f'{key}                   {value}')

        return top_documents_dictionary

    @timer
    def view_also_likes(self, doc_id, user_id=None):
        """
        Creates graph of all 'also like' documents for given doc_id and user id

        For the input document, all readers are identified. Then for those readers,
        all of the documents they've read are identified. These documents are then
        plotted.

        Parameters
        ----------
        doc_id: str
            Input document ID

        user_id: str, optional
            Input user ID

        """
        # All readers of input document
        readers = self.readers_of_document(doc_id)

        # Create empty dictionary to store readers and their documents
        records = {}
        # Iterate over each reader of the input document
        for reader in readers:
            if user_id is None:
                # Get docs read by user
                docs_read = self.documents_read_by_user(reader)
                # Append it to dictionary
                records[reader[-4:]] = docs_read

            # If input user is provided, we do not want to add them to this dictionary.
            # Will add them manually when graphing
            elif user_id is not None and reader[-4:] != user_id[-4:]:
                docs_read = self.documents_read_by_user(reader)
                records[reader[-4:]] = docs_read

        # get filename to add to the arrow
        num = 'Size: ' + self.current_filename.split('_')[1]

        # create digraph
        graph = Digraph(filename='also_likes.gv')

        # Show relation between nodes
        graph.node('Readers', color='white')
        graph.node('Documents', color='white')
        graph.edge('Readers', 'Documents', label=num)

        # Add input document as node
        graph.node(doc_id[-4:], style='filled', fillcolor='#3ab125')

        # If input user is given, create a node for them and add edge to input doc
        if user_id is not None:
            graph.node(user_id[-4:], style='filled', fillcolor='#3ab125', shape='box')
            graph.edge(user_id[-4:], doc_id[-4:])

        # Iterate over reader:docs_read dic we created earlier
        for key, values in records.items():
            # values represent a list of documents read by reader(key)
            # Iterate over each document read by this reader
            for item in values:
                graph.node(key, shape='box')
                graph.node(item, shape='circle')
                graph.edge(key, item)

        # View Graph
        graph.view()
