from app import App
from parser import create_parser
from tasks import run_tasks
from gui.model import Model


def main(args: dict):
    """Entry point for the Issuu Data Analysis application"""

    # Create model and pass the command line options to it
    # This model can be used to run coursework tasks directly or through GUI
    model = Model(args, '')

    if args['task'] == '7' or args['task'] is None:
        # Create a Tkinter application and pass the parser dictionary to it
        app = App(args, model)
        # Start the GUI mainloop
        app.mainloop()
    else:
        # If GUI option (task 7) is not selected, run the tasks directly
        run_tasks(args, model)


if __name__ == '__main__':
    parser_args = create_parser()
    main(parser_args)
