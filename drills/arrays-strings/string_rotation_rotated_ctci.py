class StringRotationRotated:

    def __init__(self):
        pass

    def is_string_rotated(self, original, potential_rotation):

        if len(original) != len(potential_rotation):
            return False

        original = original + original 

        if potential_rotation in original:
            return True 

        return False 

s = StringRotationRotated()

print(s.is_string_rotated('klajd', 'ajdkl'))


import unittest 
class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]


    def test_string_rotation(self):
        pass
        
