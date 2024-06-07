from unittest import TestCase
import unittest

######## Function to handle the invalid age #######
# def can_drive(age):
#     if age < 0 or age > 100:
#         raise ValueError("Age is out of range")
#     driving_age = 16
#     return age >= driving_age

def can_drive(age):
    driving_age = 16
    return age >= driving_age

class TestCanDrive(TestCase):

    def test_age1(self):
        self.assertEqual(can_drive(16), True)

    def test_age2(self):
        self.assertEqual(can_drive(17), True)

    def test_age3(self):
        self.assertEqual(can_drive(15), False)

    def test_age4(self):
        self.assertEqual(can_drive(0), False)

    def test_age5(self):
        with self.assertRaises(ValueError):
            can_drive(-1)

    def test_age6(self):
        self.assertEqual(can_drive(1), False)

    def test_age7(self):
        self.assertEqual(can_drive(100), True)

    def test_age8(self):
        with self.assertRaises(ValueError):
            can_drive(101)

    def test_age9(self):
        self.assertEqual(can_drive(99), True)

if __name__ == '__main__':
    unittest.main()
