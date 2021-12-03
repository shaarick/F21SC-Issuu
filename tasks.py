"""Run functions depending on task option passed in CLI"""


def run_tasks(args: dict, model):
    task = args['task']
    if task == '2a':
        model.view_country()
    elif task == '2b':
        model.view_continent()
    elif task == '3a':
        model.view_long_browsers()
    elif task == '3b':
        model.view_short_browsers()
    elif task == '4':
        model.view_top_readers()
    elif task == '5d':
        if args['sorter'] is None:
            model.view_top_documents(args['document_uuid'], args['user_uuid'], sort=None)
        elif args['sorter'] == 'desc':
            model.view_top_documents(args['document_uuid'], args['user_uuid'], sort='desc')
    elif task == '6':
        model.view_also_likes(args['document_uuid'], args['user_uuid'])
