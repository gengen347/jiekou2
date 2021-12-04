from commen.handle_path import CONFIG_PATH
from configparser import ConfigParser
import os
class Config(ConfigParser):
    def __init__(self,file_path,encoding):
        super().__init__()
        # self.a=111
        self.read(file_path, encoding=encoding)
        self.file_path=file_path
        self.encoding=encoding
    def write_ini(self,section,option,value):
        self.set( section, option, value=value)
        self.write(open(self.file_path, mode='w', encoding=self.encoding))


conf=Config(os.path.join(CONFIG_PATH,'config.ini'),'UTF-8')







if __name__ == '__main__':

    conf=Config(os.path.join(CONFIG_PATH,'config.ini'),'UTF-8')
    print(type(conf.get('mysql', 'password')),conf.get('mysql', 'password'))
    conf.write_ini('report','xingmin1g','li111g1en')
    # print(type(conf.a), conf.a)