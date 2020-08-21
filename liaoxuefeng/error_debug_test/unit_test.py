
# unit_test.py

import unittest

class Dict(dict):
    # note: **value is a dict
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattribute__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError("'Dict' object has no attribute '%s'" 
                        % key)

    def __setattr__(self, key, value):
        self[key] = value

# unit test
class TestDict(unittest.TestCase):
    # setUp and teardown will be called in every test
    def setUp(self):
        print ("setup...")
    
    def tearDown(self):
        print ("teardown...")

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    # expect to raise a exception
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# test
unittest.main()

# output:
#
# setup...
# teardown...
# .setup...
# teardown...
# .setup...
# teardown...
# .setup...
# teardown...
# .setup...
# teardown...
# .
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s
# 
# OK