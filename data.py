import pandas as pd
import json


def get_data():
    doc_list = []
    print("Started reading JSON file.")
    with open("issuu_cw2.json") as f:
        for js in f:
            doc_dic = json.loads(js)
            doc_list.append(doc_dic)
    print("Finished reading JSON file.")
    df = pd.DataFrame(doc_list)
    return df
