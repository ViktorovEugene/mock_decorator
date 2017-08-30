from functools import wraps


def tag_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return '<p>' + str(func(*args, **kwargs)) + '</p>'
    return wrapper
