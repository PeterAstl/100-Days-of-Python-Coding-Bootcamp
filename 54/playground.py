
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(10)
        function()
    return wrapper_function

@delay_decorator
def hello_world():
    print('Hello, World!')


hello_world()