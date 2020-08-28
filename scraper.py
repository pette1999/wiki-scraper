import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}

url = 'https://www.americancasinoguide.com/casinos-by-state.html'

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html5lib')

# Casino = []
# City = []
# Country = []
# State = []
# District = []
# Type = []
# Comments = []

# for i in soup.find_all('ul'):
#     try:
#         for m in i.find_all('li'):
#             print("https://www.americancasinoguide.com" + m.a.get('href'))
#     except:
#         continue

# print(len(Casino))
# print(len(City))
# print(len(Country))
# print(len(State))
# print(len(District))
# print(len(Type))
# print(len(Comments))

# for i in Casino:
#     print(i.replace('\n',''))

# driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)

links = []
f = open("link.txt", "r")
for i in f:
    print(i.replace("\n", ""))
    links.append(i.replace("\n", ""))
print('\n')


for i in links:
    count = 0
    if(i == "no link"):
        print(" ")
    else:
        page = requests.get(i, headers=headers)
        soup = BeautifulSoup(page.content, 'html5lib')

        # for i in soup.find_all("tr"):
        #     try:
        #         if(i.get('ng-if') == 'operator_physical_shop.website' and count < 1):
        #             print(i)
        #             count += 1
        #     except:
        #         continue
        print(soup)


print(count)
