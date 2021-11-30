from app import App
from parser import create_parser
from tasks import run_tasks
from gui.model import Model


"""
Entry point for the Issuu Data Analysis application.

Running the script without any options will start the GUI, where you can enter field values and perform tasks on them.
Running the script with options automatically fill the fields with provided values as well as run the task mentioned.
"""


def main(args: dict):

    # Create model and pass the command line options to it
    # This model can be used to run tasks directly or through GUI
    model = Model(args, '')

    if args['task'] == '7':
        # Create a Tkinter application and pass the parser dictionary to it
        app = App(args, model)
        # Start the GUI mainloop
        app.mainloop()
    else:
        run_tasks(args, model)


if __name__ == '__main__':
    parser_args = create_parser()
    main(parser_args)
