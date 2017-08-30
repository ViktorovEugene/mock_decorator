from some_library import tag_decorator


RESULT = 'result'


@tag_decorator
def func_to_test():
    return RESULT
