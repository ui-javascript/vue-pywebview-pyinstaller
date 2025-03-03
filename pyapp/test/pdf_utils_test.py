import sys
import os

# @fix https://blog.csdn.net/qq_40472613/article/details/119670598
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from PyPDF2 import PdfFileReader as pdf_read

#每个书签的索引格式
#{'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

directory_str = ''

def bookmark_listhandler(list):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += "# " + message['/Title'] + '\n\n'
        else:
            bookmark_listhandler(message)

def gen_pdf_outlines(pdf_path):
    global directory_str
    directory_str = ""

    # pdf_path = "D:\\dl-nut\\我的坚果云\\XXX-B·卡尔-201108.pdf"
    with open(pdf_path, 'rb') as f:
        pdf = pdf_read(f)
        #检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
        text_outline_list = pdf.getOutlines()
        bookmark_listhandler(text_outline_list)

    with open(pdf_path + '.txt', 'w', encoding='utf-8') as f:
        f.write(directory_str)

    return pdf_path + '.txt'

gen_pdf_outlines(sys.argv[1])