from unittest.case import TestCase

class Walker(object):
    
    def walk(self,source, target):
        return [source,target]

class NumericMaze(TestCase):
    
    def test_double_if_the_next_one_is_the_double(self):
        johnny = Walker()
        self.assertEquals([8,16],johnny.walk(8,16));