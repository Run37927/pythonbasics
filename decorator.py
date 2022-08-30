def a_decorator(func):
    def wrapper():
        print("a piranha appears")
        func()
        print("original function is finished")
    return wrapper()


@a_decorator
def my_function():
    print("a banana appears")


my_function()
