import random
from commen.handle_db import db
import re
from commen.handle_config import conf

def random_phone():
    while True:
        phone=random.randint(13500000000,13599999999)
        sql=f'select * from futureloan.member WHERE mobile_phone={phone}'
        if not db.find_all(sql):
            return str(phone)

def replace_data(data,cls):
    while re.search("#(.+?)#", data):
        res=re.search("#(.+?)#", data)
        replace_data=res.group()
        attr=res.group(1)
        try:
            new_data=conf.get('test_data',attr)
        except:
            new_data=getattr(cls,attr)
        data=data.replace(replace_data,str(new_data))
    return data








if __name__ == '__main__':
    print(random_phone())
    replace('{"member_id":#invest_member_id#,"amount":300}')