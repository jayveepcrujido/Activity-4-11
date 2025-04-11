import unittest
from password import check_password_strength


class TestPasswordStrength(unittest.TestCase):

    def test_strong_password(self):
        self.assertEqual(check_password_strength("Abcdef1!"), "Strong")

    def test_medium_password(self):
        self.assertEqual(check_password_strength("abcdef12"), "Medium")

    def test_weak_password(self):
        self.assertEqual(check_password_strength("abc"), "Weak")

    def test_no_input(self):
        self.assertEqual(check_password_strength(""), "No Input")


if __name__ == "__main__":
    unittest.main()
