from bs4 import BeautifulSoup
from urllib.request import urlopen

url = [
    "https://habr.com/ru/post/580888/",
    "https://habr.com/ru/post/579100/"
]

file = open('text.txt', 'a')

for link in url:
    html_code = str(urlopen(link).read(), 'utf-8')
    soup = BeautifulSoup(html_code, 'html.parser')

    s = soup.find('title').text
    file.write(s + '\n')
    p = soup.find_all('p')
    print(s)
    for i in p:
        print(i.text)
        file.write(i.text + '\n')

file.close()