import requests
import unittest
from commen.handle_excel1 import Excel
from commen.handle_path import DATA_PATH
import os
from commen import my_ddt1
from commen.handle_config import conf
from tools import tools
from commen.handle_log1 import log
from commen.handle_db import db


@my_ddt1.ddt()
class Register(unittest.TestCase):
    excel=Excel( os.path.join(DATA_PATH,'cases1.xlsx'), 'register')
    case_data=excel.read()

    @my_ddt1.data(*case_data)
    def test_register(self,item):
        url=conf.get('env', 'base_url')+item['url']
        method=item['method']
        headers=eval(conf.get('env', 'headers'))
        expected=eval(item['expected'])
        data=item['data']
        if '*phone*' in data:
            phone = tools.random_phone()
            data=data.replace('*phone*',phone)
        data=eval(data)
        res = requests.request(url=url, method=method, json=data, headers=headers)
        # print("预期结果：", expected)
        # print("实际结果：", res.text)
        try:
            self.assertEqual(res.json()['code'],expected['code'])
            self.assertEqual(res.json()['msg'], expected['msg'])
            if item['check_sql']:
                res = db.find_all(item['check_sql'].format(data['mobile_phone']))
                self.assertTrue(res)
                print(res)
        except Exception as  e:
            log.error(f'注册：{item["title"]}失败！')
            log.exception(e)
            raise e
        else:
            log.info(f'注册：{item["title"]}通过！')