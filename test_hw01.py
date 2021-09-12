import unittest
from HW01testingtriangle import classify_triangle


class TestTriangles(unittest.TestCase):
    def test1(self):
        self.assertEqual(classify_triangle(5,4,3), 'right', 'This is a right triangle')
        self.assertEqual(classify_triangle(5,3,4), 'right', 'This is a right triangle')
if __name__ == '__main__':
    unittest.main()


"""
In the main file, I did not specify all the correct cases of a right triangle on purpose

a ** 2 + b **2 == c **2
c ** 2 + b **2 == a **2
a ** 2 + c **2 == b **2

I knew this would raise an error when I input:
5,4,3
or 
5,3,4
because it does not know that any of the values could be C, but the formula states that C has to the hypotenuse.

I had a lot of trouble trying to test this out. No matter how I set it up I would get a fail even when it was correct.


"""