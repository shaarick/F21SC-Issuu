import functools
import time


def timer(func):
    """Decorator to display function run time"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Time taken: {elapsed_time:0.4f} seconds")
        return value

    return wrapper_timer
