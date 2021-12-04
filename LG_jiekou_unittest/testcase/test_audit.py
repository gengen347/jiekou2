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
class Audit(unittest.TestCase):
    excel=Excel(os.path.join(DATA_PATH,'cases1.xlsx'), 'audit')
    case_data=excel.read()

    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_token=fixture.login_admin()

    @classmethod
    def setUp(cls):
        token ,member_id,leave_amount_before=fixture.login_jiekuan()
        cls.loan_id=fixture.add_jiekuan(member_id,token)



    @my_ddt1.data(*case_data)
    def test_audit(self,item):
        url=conf.get('env','base_url')+item['url']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = self.admin_token
        method=item['method']
        expected=eval(item['expected'])
        data=item['data']
        data=eval(replace_data(data,Audit))

        res=requests.request(url=url,method=method,json=data,headers=headers)
        print(res.text)
        print(item['expected'])
        try:
            if item['check_sql']:
                sql= f"select status from futureloan.loan where id={self.loan_id}"
                self.assertEqual(db.find_all(sql)[0]['status'],expected['status'])
                print(db.find_all(sql)[0]['status'],'*************',expected['status'])
            self.assertEqual(res.json()['code'],expected['code'])
            self.assertEqual(res.json()['msg'], expected['msg'])
        except Exception as e:
            log.error(f"{item['interface']}：{item['title']}【失败】*****")
            log.exception(e)
            raise e
        else:
            log.info(f"{item['interface']}：{item['title']}【通过】")
            setattr(Audit, "pass_loan_id", self.loan_id)


