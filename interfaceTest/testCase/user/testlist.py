import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        print("王同学")


if __name__ == '__main__':
    unittest.main()
