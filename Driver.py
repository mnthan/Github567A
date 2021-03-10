import unittest

from HW4a import RepoLister

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRepoA(self): 
        self.assertEqual(RepoLister("mnthan"),'200','Passed')

    def testRepoB(self): 
        self.assertEqual(RepoLister("richkempinski"),'200','Passed')
        
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
