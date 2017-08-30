import unittest
import importlib
import some_library  # The module that contains decorator
import tested_module


class TestDecoratorMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_split(self):
        self.assertEqual(tested_module.func_to_test()[:3], '<p>')
        self.assertEqual(tested_module.func_to_test()[-4:], '</p>')
        self.assertEqual(
            tested_module.func_to_test()[3:-4],
            tested_module.RESULT
        )


class TestMockDecoratorMethods(unittest.TestCase):
    def setUp(self):
        self.decorators_backup = some_library.tag_decorator
        self.open_tag = '<a>'
        self.close_tag = '</a>'

        def mocked_decorator(funk):
            def wrapper(*args, **kwargs):
                return self.open_tag + str(funk()) + self.close_tag
            return wrapper

        some_library.tag_decorator = mocked_decorator
        importlib.reload(tested_module)

    def tearDown(self):
        some_library.tag_decorator = self.decorators_backup
        importlib.reload(tested_module)

    def test_split(self):
        self.assertEqual(tested_module.func_to_test()[:3], self.open_tag)
        self.assertEqual(tested_module.func_to_test()[-4:], self.close_tag)
        self.assertEqual(
            tested_module.func_to_test()[3:-4],
            tested_module.RESULT
        )

if __name__ == '__main__':
    unittest.main()
