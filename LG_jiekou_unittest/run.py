import os
import unittest
import pytest
from commen.handle_config import conf
from commen.handle_path import CASE_PATH,REPORT_PATH
from unittestreport import TestRunner
from testcase.fixture import init_env_data

# suite =unittest.defaultTestLoader.discover(CASE_PATH)
# # 准备一些测试的环境数据
# init_env_data()
# # 执行用例
# runner = TestRunner(suite,
#                     filename=conf.get('report', "filename"),
#                     report_dir=REPORT_PATH,
#                     title='测试报告',
#                     tester='ligen',
#                     desc="木森执行测试生产的报告",
#                     templates=1
#                     )
# runner.run()


pytest.main(["-v" ,"-s","--alluredir=test_result/reports","--clean-alluredir" # 指定生产allure报告的路径
             ])

# # 2、启动allure服务
# os.system('allure serve test_result/reports')