import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    """Набор тестов для класса Stack"""

    def test_push_pop(self):
        """Тестирование методов push и pop."""
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')

    def test_push_pop_empty_stack(self):
        """Тестирование методов push и pop для пустого стека."""
        stack = Stack()

        self.assertIsNone(stack.pop())

    def test_push_pop_mixed_types(self):
        """Тестирование методов push и pop для стека с разными типами данных."""
        stack = Stack()
        stack.push(1)
        stack.push('string')

        self.assertEqual(stack.pop(), 'string')
        self.assertEqual(stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()
