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
class Add(unittest.TestCase):
    excel=Excel(os.path.join(DATA_PATH,'cases1.xlsx'), 'add')
    case_data=excel.read()

    @classmethod
    def setUpClass(cls) -> None:
        cls.token ,cls.member_id,cls.leave_amount_before=fixture.login_jiekuan()

    @my_ddt1.data(*case_data)
    def test_add(self,item):
        url=conf.get('env','base_url')+item['url']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = self.token
        method=item['method']
        expected=eval(item['expected'])
        data=item['data']
        data=eval(replace_data(data,Add))

        if item['check_sql']:
            sql = f"SELECT COUNT(1) FROM futureloan.member,futureloan.loan WHERE member.id = loan.member_id and member.id={self.member_id}"
            count_befor = db.find_all(sql)[0]['COUNT(1)']

        res=requests.request(url=url,method=method,json=data,headers=headers)
        # print(res.text)
        # print(item['expected'])
        try:
            if expected['msg']=='OK':
                sql = f"SELECT COUNT(1) FROM futureloan.member,futureloan.loan WHERE member.id = loan.member_id and member.id={self.member_id}"
                count_after = db.find_all(sql)[0]['COUNT(1)']
                self.assertEqual((count_after-count_befor),1)

            self.assertEqual(res.json()['code'],expected['code'])
            self.assertEqual(res.json()['msg'], expected['msg'])
        except Exception as e:
            log.error(f"{item['interface']}：{item['title']}【失败】*****")
            log.exception(e)
            raise e
        else:
            log.info(f"{item['interface']}：{item['title']}【通过】")



