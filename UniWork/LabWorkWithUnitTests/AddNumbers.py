from operator import add


def test_add_negative(self):

    self.assertEqual(add(-1, 5), 4)

def test_add_floats(self):
    
    self.assertEqual(add(2.5, 3.1), 5.6)