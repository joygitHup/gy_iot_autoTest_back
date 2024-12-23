import os
import unittest
import pytest
from config.path_config import report_path
case_path1=os.path.join(os.getcwd(),"test_case")
def creat_suite():
   suiteTest_defaultTestLoader = unittest.defaultTestLoader.discover(start_dir=case_path1, pattern='test_*.py',top_level_dir=None)
   return suiteTest_defaultTestLoader
suite = creat_suite()
if  __name__=="__main__":
    pytest.main([r'--alluredir={}'.format(report_path)])

