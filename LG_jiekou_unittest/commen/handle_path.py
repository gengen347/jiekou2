import os
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH=os.path.join(BASE_PATH,'conf')
DATA_PATH=os.path.join(BASE_PATH,'data')
CASE_PATH=os.path.join(BASE_PATH,'testcase')
REPORT_PATH=os.path.join(BASE_PATH,'reports')
LOG_PATH=os.path.join(BASE_PATH,'logs')