"""
Module for various sorters.

Notes
------
CW Spec does not specify how many to implement, so only implemented one.
"""


def desc(readers: list, counter, doc_uuid: str, user_uuid: str) -> dict:
    records = counter(readers, doc_uuid, user_uuid)
    sorted_dic = dict(sorted(records.items(), key=lambda item: item[1], reverse=True))
    return sorted_dic
