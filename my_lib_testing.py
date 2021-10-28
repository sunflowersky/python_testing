import unittest
import random
import statistics
import my_lib

class TestLib(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n Running class setUp...")
    
    @classmethod
    def tearDownClass(cls):
        print("\n Running class tearDown...")
        
        
    def setUp(self):
        print("\nRunning setUp...")
        
    def tearDown(self):
        print("Running tearDown...")
        
        
    def test_list_avg_null(self):
        # if we provide an input that is none (null), we will get back a none
        print("Running test_list_avg_null...")
        res = my_lib.list_avg(None)
        self.assertEqual(res, None)
        self.assertIsNone(res)
        #c all to a test case to run and check the code is behaving accordingly
        print("Finished test_list_avg_null...")
     
    
    def test_list_avg_empty(self):
        res = my_lib.list_avg([])
        self.assertIsNone(res)
    
    
    def test_list_avg_const(self):
        res = my_lib.list_avg([5, 5, 5, 5, 5, 5])
        self.assertEqual(res,5)
        
        res = my_lib.list_avg([-10, -10, -10,-10])
        self.assertEqual(res,-10)
        
        res = my_lib.list_avg([25])
        self.assertEqual(res,25)
        
        
    def test_list_avg_floats(self):
        for _ in range(10):
            vals = []
            size = random.randint(1,100)
            
            for _ in range(size):
                val = random.uniform(-200,1000)
                vals.append(val)
                
            res = my_lib.list_avg(vals)
            exp = statistics.mean(vals)
            self.assertAlmostEqual(res, exp, places=10)
            
    def test_list_avg_nonlist(self):
        self.assertRaises(TypeError, my_lib.list_avg, {'a': 1, 'b':23.0})
        self.assertRaises(TypeError, my_lib.list_avg, 24.0)
        self.assertRaises(TypeError, my_lib.list_avg, (1.0, 2.0, 42.0))
        

class OtherTest(unittest.TestCase):
    # do another test unit, how do you want to organize this?
    
    @classmethod
    def setUpClass(cls):
        print("\n Other class setUp...")
    
    @classmethod
    def tearDownClass(cls):
        print("\ Other class tearDownn...")
        
    def test_other_func_or_lib(self):
        print("Running our test for other stuff...")
        
    
 
if __name__ == '__main__':
    unittest.main()