from app import App
from parser import create_parser

"""
Entry point for the Issuu Data Analysis application.

Running the script without any options will start the GUI, where you can enter field values and perform tasks on them.
Running the script with options automatically fill the fields with provided values as well as run the task mentioned.
"""


def main(args: dict):
    # Create a Tkinter application and pass the parser dictionary to it
    app = App(args)
    # Start the GUI mainloop
    app.mainloop()


if __name__ == '__main__':
    parser_args = create_parser()
    main(parser_args)
