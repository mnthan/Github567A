"""
"""
from HW05a import RepoLister
from unittest import mock
import unittest
from unittest.mock import patch, Mock
import json

class Testgetinfo(unittest.TestCase):
    @patch('HW05a.requests.get')
    def testgetinfo(self, mockedReq):
        results_binding = [Mock(),Mock(),Mock(),Mock(),Mock()]
        results_binding[0].json.return_value = [{
            "name": "Github567A",
            "name": "Python_01",
            "name": "Python_HW01",
            "name": "TriangleManthan"
        }]
        results_binding[1].json.return_value = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        results_binding[2].json.return_value = [{}, {}]
        results_binding[3].json.return_value = [{}, {}, {}, {}, {}, {}]
        results_binding[4].json.return_value = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        mockedReq.side_effect = results_binding
        res_code = RepoLister('mnthan')
        self.assertEqual(res_code, "200")
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
