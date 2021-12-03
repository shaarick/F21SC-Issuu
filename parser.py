import argparse

"""
Create a parser for Issuu Data Analysis application

Create a parser with several options that can automatically perform courseowrk tasks without having to manually
use the GUI. All options are self-explanatory, especially with their help values.
"""


def create_parser():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-u', '--user_uuid', type=str, action='store', help='User id you want to query with')
    my_parser.add_argument('-d', '--document_uuid', type=str, action='store', help='Document id you want to query with')
    my_parser.add_argument('-url', type=str, action='store', help='URL of the json file')
    my_parser.add_argument('-t', '--task', type=str, action='store',
                           choices=['2a', '2b', '3a', '3b', '4', '5d', '6', '7'],
                           help='Coursework task that you want to test')
    my_parser.add_argument('-s', '--sorter', type=str, action='store', help='Sorter for Task 5d')
    requiredNamed = my_parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-f', '--file_name', type=str, action='store', help='File name containing JSON data',
                               required=True)

    # Save parsed options into a Namespace object
    my_args = my_parser.parse_args()

    # Convert Namespace into a dictionary and return it
    return vars(my_args)
