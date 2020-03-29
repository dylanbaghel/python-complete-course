"""
Unit Testing:
    --> Test Small Parts of an application in isolation (e.g units).
    --> Good Candidates For Unit Testing: individual classes, modules, or functions.
    --> Bad Candidates for unit testing: an entire application, dependencies across several classes or modules.
"""
"""
--> Python Comes With a built-in module called 'unittest'.
--> We can write unit tests encampsulated as classes that inherit from 'unittest.TestCase'.
--> This inheritance gives access to many assertion helpers that let you test the behaviour of your functions.
--> We can run tests by calling unittest.main()
--> setUp() --> Before Hook
--> tearDown() --> After Hook
"""
import unittest

def add(x, y):
    return x + y

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

class ActivityTests(unittest.TestCase):
    def setUp(self):
        print('Running Before Every Test')

    @classmethod
    def setUpClass(cls):
        print('Running Before All The Test')

    def test_add(self):
        self.assertEqual(
            add(5, 6),
            11
        )
    def test_full_name(self):
        person = Person('Abhishek', 'Baghel')
        self.assertEqual(
            person.full_name,
            'Abhishek Baghel'
        )

    @classmethod
    def tearDownClass(cls):
        print('Running After All The Test')
        
    def tearDown(self):
        print('Running After Every Test')

unittest.main()

