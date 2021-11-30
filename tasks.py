def run_tasks(args: dict, model):
    task = args['task']
    if task == '2a':
        model.view_country()
    elif task == '2b':
        model.view_continent()
    elif task == '3a':
        model.view_browsers()
    elif task == '3b':
        model.view_short_browsers()
