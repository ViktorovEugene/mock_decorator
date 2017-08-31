from some_library import tag_decorator


RESULT = 'result'


class MockMethod:
    @staticmethod
    @tag_decorator
    def static_method():
        return RESULT\

    @tag_decorator
    def instance_method(self):
        return RESULT
