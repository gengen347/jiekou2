import  pymysql
from commen.handle_config import conf

class DB:
    def __init__(self,host,user,password,port):
        # 第一步：连接到数据库
        self.con = pymysql.connect(host=host,  # 数据库的地址
                              user=user,               # 登录数据库的账号
                              password=password,           # 登录数据库的密码
                              port=port,                  # 端口
                              cursorclass = pymysql.cursors.DictCursor,
                              charset = "utf8"
                              )
        # 第二步：创建游标
        self.cur = self.con.cursor()

    def find_all(self,sql):
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

db=DB(host=conf.get('mysql','host'),user=conf.get('mysql','user'),
      password=conf.get('mysql','password'),port=conf.getint('mysql','port'))

if __name__ == '__main__':
    db = DB(host=conf.get('mysql', 'host'), user=conf.get('mysql', 'user'),
            password=conf.get('mysql', 'password'), port=conf.getint('mysql', 'port'))
    sql = 'SELECT * FROM futureloan.member where reg_name="小橘子" limit 10'
    res = db.find_all(sql)
    print(res)