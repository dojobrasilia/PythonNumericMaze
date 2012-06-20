from unittest.case import TestCase

class Walker(object):
    
    def walk(self,source, target):
        path = [source]
        
        while source != target :
            if target < source:
                source /= 2                
            elif source * 2 > target: 
                source += 2                
            else:
                source *= 2
            
            if (source in path):
                break
            path.append(source)
            
        return path

class NumericMazeTest(TestCase):
    
    def setUp(self):
        self.johnny = Walker()
    
    def test_double_if_the_next_one_is_the_double(self):
        self.assertEquals([8,16],self.johnny.walk(8,16))
            
    def test_double_if_sequence_of_doubles(self):
        self.assertEquals([4,8,16,32], self.johnny.walk(4, 32))
    
    def test_half_if_sequence_of_halves(self):
        self.assertEquals([32,16,8,4], self.johnny.walk(32, 4))
        
    def test_finds_aswer_with_a_single_sum(self):
        self.assertEquals([6,8], self.johnny.walk(6, 8))
    
    def test_finds_answer_with_two_sum(self):
        self.assertEquals([6,8,10], self.johnny.walk(6, 10))
    
    def test_finds_answer_with_double_sum_sum_sum(self):
        self.assertEquals([6,12,14,16,18,20], self.johnny.walk(6, 20))
        
    #def test_from_2_to_9(self):
     #   self.assertEquals([2,4,8,16,18,9], self.johnny.walk(2,9))
     
    def test_odd_with_sum(self):
        self.assertEquals([7,14,16,8], self.johnny.walk(7, 8))        