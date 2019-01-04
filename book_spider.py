import re
from urllib import request
class BookInformation():
    # 首页地址
    url = 'http://d81fb43e-d.parkone.cn/'
    root_pattern = ''
    # 书名
    book_name_pattern = '<h2>([\s\S]*?)</h2>'
    # 作者
    author_pattern = '<a href="/author/[\s\S]*?">([\s\S]*?)</a>'
    # 语言
    language_pattern = '<span class="label label-default">语言:([\s\S]*?)</span>'
    # 出版社
    press_pattern = '<span>出版社:([\s\S]*?)</span>'
    # 出版日期
    data_pattern = '<p>出版日期:([\s\S]*?)</p>'
    # 简介
    content_pattern = '<p class="description">([\s\S]*?)</p>'

    def __fetch_content(self):
        r = request.urlopen(BookInformation.url + '/book/' + str(i))
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        anchors = []
        book_name = re.findall(BookInformation.book_name_pattern,htmls)
        author = re.findall(BookInformation.author_pattern,htmls)
        language = re.findall(BookInformation.language_pattern,htmls)
        press = re.findall(BookInformation.press_pattern,htmls)
        data = re.findall(BookInformation.data_pattern,htmls)
        content = re.findall(BookInformation.content_pattern,htmls)
        anchor = {'书名 ':book_name,'作者 ':author,'语言 ':language,'出版社 ':press,'出版日期 ':data,'简介 ':content}
        anchors.append(anchor)
        return anchors
    

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
       
        print(anchors)
 
for i in range(1,254):
    book_infor = BookInformation()
    book_infor.go()
    