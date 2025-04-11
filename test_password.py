import unittest
from password import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(check_password_strength("Abcdef1!"), "Strong")

    def test_medium_password(self):
        self.assertEqual(check_password_strength("abcdef12"), "Medium")

    def test_weak_password(self):
        self.assertEqual(check_password_strength("abc"), "Weak")

if __name__ == "__main__":
    unittest.main()
