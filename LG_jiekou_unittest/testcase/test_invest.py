import unittest
from commen.handle_excel1 import Excel
from commen.handle_log1 import log
from commen.handle_path import DATA_PATH
import os
from commen import my_ddt1
from commen.handle_config import conf
from tools.tools import replace_data
from testcase import fixture
import requests
from jsonpath import jsonpath
import decimal
from commen.handle_db import db

@my_ddt1.ddt()
class Invest(unittest.TestCase):
    excel=Excel(os.path.join(DATA_PATH,'cases1.xlsx'), 'invest')
    case_data=excel.read()
    @classmethod
    def setUpClass(cls) -> None:
        token ,member_id,leave_amount_before=fixture.login_jiekuan()
        cls.loan_id=fixture.add_jiekuan(member_id,token)
        admin_token=fixture.login_admin()
        fixture.audit_admin(cls.loan_id,admin_token)
        cls.token_invest ,cls.invest_member_id,leave_amount_invest=fixture.login_invest()
    @my_ddt1.data(*case_data)
    def test_recharge(self,item):
        url=conf.get('env','base_url')+item['url']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = self.token_invest
        method=item['method']
        expected=eval(item['expected'])
        data=item['data']
        data=eval(replace_data(data,Invest))

        res=requests.request(url=url,method=method,json=data,headers=headers)
        print(res.text)
        print(item['expected'])
        try:
            self.assertEqual(res.json()['code'],expected['code'])
            self.assertEqual(res.json()['msg'], expected['msg'])
        except Exception as e:
            log.error(f"{item['interface']}：{item['title']}【失败】*****")
            log.exception(e)
            raise e
        else:
            log.info(f"{item['interface']}：{item['title']}【通过】")



