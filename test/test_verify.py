'''Testing for to verify user'''

import unittest, re
from verify.verify import User

class TestVerify(unittest.TestCase):
    def setUp(self):
        '''Declare instance variables'''
        # Declare dummy instance
        self.me = User('Harsh', 7506298466, 'harsh.sinha@quantiphi.com')

    @classmethod
    def tearDownClass(cls):
        # Class-scoped destructor
        print('Tests completed')

    def test_get_name(self):
        self.assertTrue(self.me.name[0].isupper())
        self.assertIsNotNone(re.search('\S{2}', self.me.name))

    def test_get_phone(self):
        self.assertIsInstance(self.me.phone, int)
        self.assertIsNotNone(re.search('^[0-9]{10,12}$', str(self.me.phone)))
     
    def test_get_email(self):
        self.assertIsNotNone(re.search('\S+[.]\S+@\S+', self.me.email))

# Allows for directly running test file
if __name__ == '__main__':
    unittest.main()
