import unittest

from Calculator import add, sub


class CalculatorTests(unittest.TestCase):
    def test_add_integers(self):
        cases = [
            (5, 3, 8),
            (-5, -3, -8),
            (-5, 3, -2),
            (5, -3, 2),
            (0, 7, 7),
            (7, 0, 7),
            (0, 0, 0),
            (10**100, 1, 10**100 + 1),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_subtract_integers(self):
        cases = [
            (5, 3, 2),
            (3, 5, -2),
            (-5, -3, -2),
            (-5, 3, -8),
            (5, -3, 8),
            (0, 7, -7),
            (7, 0, 7),
            (0, 0, 0),
            (7, 7, 0),
            (10**100, 1, int("9" * 100)),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(sub(a, b), expected)

    def test_add_floating_point_and_mixed_numbers(self):
        cases = [(0.1, 0.2, 0.3), (-1.5, 0.5, -1.0), (2, 0.5, 2.5)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(add(a, b), expected)

    def test_subtract_floating_point_and_mixed_numbers(self):
        cases = [(0.3, 0.1, 0.2), (-1.5, 0.5, -2.0), (2, 0.5, 1.5)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(sub(a, b), expected)

    def test_unsupported_operands_raise_type_error(self):
        for operation in (add, sub):
            for a, b in [(None, 1), (1, None), ("2", 1), (1, "2")]:
                with self.subTest(operation=operation.__name__, a=a, b=b):
                    with self.assertRaises(TypeError):
                        operation(a, b)


if __name__ == "__main__":
    unittest.main()
