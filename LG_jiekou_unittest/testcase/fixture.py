import requests
from tools.tools import random_phone
from commen.handle_config import conf
from jsonpath import jsonpath


def register_jiekuan():
    data = '{"mobile_phone": "*phone*", "pwd": "12345678", "type": 1, "reg_name": "借款人"}'
    data = eval(data.replace('*phone*', random_phone()))
    url = conf.get('env', 'base_url') + '/member/register'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    conf.write_ini('test_data', 'jiekuan_mobile', res['data']['mobile_phone'])

def login_jiekuan():
    data = {"mobile_phone": conf.get('test_data', 'jiekuan_mobile'), "pwd": "12345678"}
    url = conf.get('env', 'base_url') + '/member/login'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    token = 'Bearer' + ' ' + jsonpath(res, "$..token")[0]
    member_id = jsonpath(res, '$..id')[0]
    leave_amount=jsonpath(res,'$..leave_amount')[0]
    return token, member_id,leave_amount

def add_jiekuan(member_id,token):
    data = {"member_id":member_id,"title":"借钱www","amount":2000,"loan_rate":12.0,"loan_term":3,"loan_date_type":1,"bidding_days":5}
    url = conf.get('env', 'base_url') + '/loan/add'
    headers = eval(conf.get('env', 'headers'))
    headers['Authorization'] = token
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    loan_id=jsonpath(res,'$..id')[0]
    return loan_id


def register_invest():
    data = '{"mobile_phone": "*phone*", "pwd": "12345678", "type": 1, "reg_name": "投资人"}'
    data = eval(data.replace('*phone*', random_phone()))
    url = conf.get('env', 'base_url') + '/member/register'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    conf.write_ini('test_data', 'invest_mobile', res['data']['mobile_phone'])


def login_invest():
    data = {"mobile_phone": conf.get('test_data', 'invest_mobile'), "pwd": "12345678"}
    url = conf.get('env', 'base_url') + '/member/login'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    token = 'Bearer' + ' ' + jsonpath(res, "$..token")[0]
    member_id = jsonpath(res, '$..id')[0]
    leave_amount=jsonpath(res,'$..leave_amount')[0]
    return token, member_id,leave_amount

def recharge_invest(member_id,token):
    url=conf.get('env','base_url')+'/member/recharge'
    headers = eval(conf.get('env', 'headers'))
    headers['Authorization'] = token
    method='POST'
    data={"member_id":member_id,"amount":500000}
    res=requests.request(url=url,method=method,json=data,headers=headers)



def register_admin():
    data = '{"mobile_phone": "*phone*", "pwd": "12345678", "type": 0, "reg_name": "管理员"}'
    data = eval(data.replace('*phone*', random_phone()))
    url = conf.get('env', 'base_url') + '/member/register'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    conf.write_ini('test_data', 'admin_mobile', res['data']['mobile_phone'])

def login_admin():
    data = {"mobile_phone": conf.get('test_data', 'admin_mobile'), "pwd": "12345678"}
    url = conf.get('env', 'base_url') + '/member/login'
    headers = eval(conf.get('env', 'headers'))
    method = 'POST'
    res = requests.request(url=url, method=method, json=data, headers=headers).json()
    print(res)
    token = 'Bearer' + ' ' + jsonpath(res, "$..token")[0]
    member_id = jsonpath(res, '$..id')[0]
    leave_amount=jsonpath(res,'$..leave_amount')[0]
    return token

def audit_admin(loan_id,admin_token):
    url=conf.get('env','base_url')+'/loan/audit'
    headers = eval(conf.get('env', 'headers'))
    headers['Authorization'] = admin_token
    method='patch'
    data={"loan_id":loan_id,"approved_or_not": True}
    res=requests.request(url=url,method=method,json=data,headers=headers)



def un_register_phone():
    phone = random_phone()
    conf.write_ini('test_data', 'un_register_mobile', phone)


def init_env_data():
    register_jiekuan()
    register_admin()
    register_invest()
    un_register_phone()

if __name__ == '__main__':

    token, member_id,leave_amount = login_invest()
    print(member_id, token,leave_amount)
