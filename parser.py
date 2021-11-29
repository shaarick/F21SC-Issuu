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
    my_parser.add_argument('-t', '--task', type=int, action='store', choices=[2, 3, 4, 5, 6],
                           help='Coursework task that you want to test')

    # Save parsed options into a Namespace object
    my_args = my_parser.parse_args()

    # Convert Namespace into a dictionary and return it
    return vars(my_args)
