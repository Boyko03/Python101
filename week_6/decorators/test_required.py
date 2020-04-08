import unittest
from required import required


class TestRequiredDecorator(unittest.TestCase):
    def test_required_when_method_in_child_class(self):
        class Animal:
            @required
            def eat(self, food):
                pass

        class Panda(Animal):
            def eat(self, food):
                pass

        exc = None
        try:
            p = Panda()
            p.eat(10)
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_required_when_method_not_in_child_class(self):
        class Animal:
            @required
            def eat(self, food):
                pass

        class Panda(Animal):
            pass

        exc = None
        try:
            p = Panda()
            p.eat(10)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), str(Exception('All classes that inherit from "Animal" must provide "eat" method.')))


if __name__ == '__main__':
    unittest.main()
