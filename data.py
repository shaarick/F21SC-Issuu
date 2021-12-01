import os.path
import pandas as pd
import json
from urllib import request
from timer import timer

"""
Module for converting JSON files into dataframes which can then be used by our program.

This module contains some extra functions (e.g. getting data from url) because of a misunderstanding.
But because those functions were already created and tested, they're still included as additional features.

"""


@timer
def get_data(name: str, testing=False) -> pd.DataFrame:
    """
    Convert JSON data to Pandas Dataframe.

    It converts all JSON objects in the file to a dictionary, all of which are appended to a list
    and then converted to a pandas dataframe.

    Parameters
    ----------
    name: str
        Filename

    testing: Bool, optional
        Default is False. When true, searches for .json text file in parent directory.

    Returns
    -------
    df: pd.DataFrame
        A Pandas dataframe containing all the JSON objects from the file.

    """
    # Create empty list
    doc_list = []
    print("Loading data..")

    # If this module is opened in test dir, then move up one dir to find dataset
    if testing:
        file = os.getcwd() + "/../" + name
    else:
        file = name

    # Open JSON file using context manager
    with open(file) as f:
        # File contains multiple JSON objects. Loop over all of them.
        for js in f:
            # Convert JSON to dic and append to list
            doc_dic = json.loads(js)
            doc_list.append(doc_dic)
    # Convert list to dataframe
    df = pd.DataFrame(doc_list)
    return df


@timer
def get_data_from_url(url: str) -> pd.DataFrame:
    """
    Convert JSON webpage to a Pandas Dataframe

    This function takes a url, assuming it has a sequence of JSON objects and nothing
    else, like the test datasets posted for the coursework. It first converts them to
    a text file, then creates JSON objects out of them. Then objects are then converted
    into a Dataframe.

    Parameters
    ----------
    url:str
        String URL for where the JSON objects are supposed to be extracted from

    Returns
    -------
    df: pd.DataFrame
        Pandas Dataframe containing all the JSON objects found on the webpage
    """
    print("Began reading webpage")
    with request.urlopen(url) as response:
        # Read Webpage
        content = response.read()
        # Convert to string
        text = content.decode()
        # Split into distinct JSON objects based on newline
        json_objects = text.strip().split('\n')
        doc_list = []
        for obj in json_objects:
            # Convert string of JSON to dictionary
            js = json.loads(obj)
            # Append dictionary to list
            doc_list.append(js)
    # Convert list to dataframe
    df = pd.DataFrame(doc_list)
    return df
