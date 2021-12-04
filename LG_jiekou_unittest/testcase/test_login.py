import unittest
from commen import my_ddt1
from commen.handle_excel1 import Excel
import os

from commen.handle_log1 import log
from commen.handle_path import DATA_PATH
from commen.handle_config import conf
from tools.tools import replace_data
import requests

@my_ddt1.ddt()
class Login(unittest.TestCase):
    excel =Excel(os.path.join(DATA_PATH,'cases1.xlsx'), 'login')
    case_data=excel.read()
    @my_ddt1.data(*case_data)
    def test_login(self,item):
        method=item['method']
        url = conf.get('env','base_url')+item['url']
        headers = eval(conf.get('env', 'headers'))
        data = item['data']
        expected = eval(item['expected'])
        data=eval(replace_data(data,Login))
        res =requests.request(url=url,method=method,json=data,headers=headers).json()
        print(f'实际结果：{res}')
        print(f'预期结果：{expected}')
        try:
            self.assertEqual(res['code'],expected['code'])
            self.assertEqual(res['msg'], expected['msg'])
        except Exception as e:
            log.error(f'{item["title"]}【失败】')
            log.exception(e)
            raise e
        else:
            log.info(f'{item["title"]}【通过】')

