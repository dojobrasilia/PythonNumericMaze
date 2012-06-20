from unittest.case import TestCase

class Walker(object):
    
    def walk(self,source, target):
        path = [source]
        
        while source != target:
            if( target < source): 
                source /= 2
            else:
                source *= 2
            path.append(source)
            
        return path

class NumericMaze(TestCase):
    
    def test_double_if_the_next_one_is_the_double(self):
        johnny = Walker()
        self.assertEquals([8,16],johnny.walk(8,16))
            
    def test_double_if_sequence_of_doubles(self):
        johnny = Walker()
        self.assertEquals([4,8,16,32], johnny.walk(4, 32))
    
    def test_half_if_sequence_of_halves(self):
        johnny = Walker()
        self.assertEquals([32,16,8,4], johnny.walk(32, 4))