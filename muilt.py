import unittest


def multiply(x, y):
    return x*y

# your test case class must be subclass of unittest.TestCase
# name of the function starts with test_


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "should be 50")


# we can either run test using this
# or we can use command python -m unittest <filename (without extension)> -v
# -v to get more details
if __name__ == "__main__":
    unittest.main()


# when our test grows we can use "nose" or "pytest" for testing
