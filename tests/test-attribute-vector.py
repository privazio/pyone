
import unittest
import pyone

class AttributeVectorTests(unittest.TestCase):
    def test_dict_to_attr(self):
        atts = {
            'NAME': 'abc',
            'MEMORY': '1024',
            'ATT1': 'value1'
            }
        self.assertEqual(pyone.OneServer.cast(atts), '''NAME = "abc"\nATT1 = "value1"\nMEMORY = "1024"\n''')