import pandas as pd
import json
from urllib import request

"""
Module for converting JSON files into dataframes which can then be used by our program.
"""


def get_data() -> pd.DataFrame:
    """
    Convert JSON data to Pandas Dataframe.

    This function assumes a "issuu_cw2.json" file is present in the same directory.
    It converts all JSON objects in the file to a dictionary, all of which are appended to a list
    and then converted to a pandas dataframe.
    Returns
    -------
    df
        A Pandas dataframe containinng all the JSON objects from the local file.

    """
    # Create empty list
    doc_list = []
    print("Started reading JSON file.")

    # Open .JSON file using context manager
    with open("issuu_cw2.json") as f:
        # File contains multiple JSON objects. Loop over all of them.
        for js in f:
            # Convert JSON to dic and append to list
            doc_dic = json.loads(js)
            doc_list.append(doc_dic)
    print("Finished reading JSON file.")
    # Convert list to dataframe
    df = pd.DataFrame(doc_list)
    return df


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
    df
        Pandas Dataframe containing all the JSON objects found on the webpage
    """
    print("Began reading webpage")
    with request.urlopen(url) as response:
        content = response.read()
        text = content.decode()
        json_objects = text.strip().split('\n')
        doc_list = []
        for obj in json_objects:
            js = json.loads(obj)
            doc_list.append(js)
    print("Finished reading webpage")
    df = pd.DataFrame(doc_list)
    return df
