'''
    sample test file for testing the functionality of the calculator module
'''
from django.test import SimpleTestCase
# Import the add function from the calc module
from .calc import add

class CalcTest(SimpleTestCase):
    ''' test the calculator module '''
    def test_add_two_numbers(self):
        ''' test the add function '''
        res = add(2 , 2)
        
        self.assertEqual(res , 9)
        ''' docker-compose run --rm app  sh -c "python manage.py test" '''