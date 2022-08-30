from bs4 import BeautifulSoup as BS
import requests
import json




class Parser:
    def urls_and_check(self, message):
        urls = ['https://coursive.id/api/v1/courses/chto-takoe-vlog-i-kak-ego-vesti/',
                'https://coursive.id/api/v1/courses/chto-takoe-podkast-i-kak-ego-zapisyvat/',
                'https://coursive.id/api/v1/courses/kak-pisat-stati-kotorye-podnimayut-vazhnye-ru',
                'https://coursive.id/api/v1/courses/chto-takoe-kontent-i-kak-ego-sozdavat',
                'https://coursive.id/api/v1/courses/chto-takoe-gendernoe-ravenstvo',
                'https://coursive.id/api/v1/courses/feminizm-zhonundo-kurs'
                ]
        if message == 1:
            self.parser(url=urls[0])
        elif message == 2:
            self.parser(url=urls[1])
        elif message == 3:
            self.parser(url=urls[2])
        elif message == 4:
            self.parser(url=urls[3])
        elif message == 5:
            self.parser(url=urls[4])
        elif message == 6:
            self.parser(url=urls[5])

    def parser(self, url):
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        soup2 = json.loads(soup.text)
        title1 = soup2['title']  # Что такое влог, и как его вести
        blocks = soup2['blocks']
        list1 = []
        for i in blocks:
            list1.append(i['title'])
        print(list1)
"""Доделать парсинг с ссылками и соединить это все с ботом!
Также парсинг с блоками обьединить с ботом!"""


# a = Parser()
# a.urls_and_check(6)
# print(type(title1))
# print(title1)urls = ['https://coursive.id/api/v1/courses/chto-takoe-vlog-i-kak-ego-vesti/',
#                 'https://coursive.id/ru/course/chto-takoe-podkast-i-kak-ego-zapisyvat',
#                 'https://coursive.id/ru/course/kak-pisat-stati-kotorye-podnimayut-vazhnye-ru',
#                 'https://coursive.id/ru/course/chto-takoe-kontent-i-kak-ego-sozdavat',
#                 'https://coursive.id/ru/course/chto-takoe-gendernoe-ravenstvo',
#                 'https://coursive.id/ru/course/feminizm-zhonundo-kurs'
#                 ]
#         if message == 1:
#             self.parser(url=urls[0])
#         elif message == 2:
#             self.parser(url=urls[1])
#         elif message == 3:
#             self.parser(url=urls[2])
#         elif message == 4:
#             self.parser(url=urls[3])
#         elif message == 5:
#             self.parser(url=urls[4])
#         elif message == 6:
#             self.parser(url=urls[5])