import openpyxl
from commen.handle_path import DATA_PATH
import os


class Excel:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.file_path)
        self.sheet = self.wb[self.sheet_name]

    def read(self):
        self.open()
        case_data = []
        title =[i.value for i in list(self.sheet.rows)[0]]
        for i in list(self.sheet.rows)[1:]:
            row = [j.value for j in i]
            case_data.append(dict(zip(title, row)))
        return case_data

    def write(self,row, column, value=None):
        self.open()
        self.sheet.cell(row, column, value)
        self.wb.save(self.file_path)


if __name__ == '__main__':
    exl = Excel(os.path.join(DATA_PATH,'cases1.xlsx'), 'register')
    print(type(exl.read()),exl.read())
    # exl.write(1,1,'kk122222111k')
