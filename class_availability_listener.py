from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
options.headless = True

search_url = 'https://webapp4.asu.edu/catalog/classlist?t=2207&s=CSE&n=310&hon=F&promod=F&e=open&page=1'

browser = Firefox(options=options)

x = True

while x:
    browser.get(search_url)

    time.sleep(1)

    data = BeautifulSoup(browser.page_source, "html.parser")
    table = data.find('table', {'id': 'CatalogList'})
    tbody = table.find('tbody')

    classes = len(tbody.find_all('tr'))

    print(classes)

    if classes > 3:
        options.headless = False
        browser = Firefox(options=options)
        browser.get(search_url)
        x = False

    time.sleep(1)
