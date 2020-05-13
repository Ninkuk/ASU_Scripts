from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import datetime

options = Options()
options.headless = True

search_url = 'https://webapp4.asu.edu/catalog/classlist?t=2207&s=CSE&n=310&hon=F&promod=F&e=open&page=1'

browser = Firefox(options=options)

x = True


def get_classes_num():
    print("Please wait. Fetching data...")
    browser.get(search_url)

    time.sleep(1)

    data = BeautifulSoup(browser.page_source, "html.parser")
    table = data.find('table', {'id': 'CatalogList'})
    tbody = table.find('tbody')

    return len(tbody.find_all('tr'))


initialNum = get_classes_num()
print("Currently there are " + str(initialNum) + " classes open")

while x:
    currentNum = get_classes_num()

    if currentNum > initialNum:
        print("Just opened! " + str(currentNum) + " open class found at " + str(datetime.datetime.now()))
        options.headless = False
        browser = Firefox(options=options)
        browser.get(search_url)
        x = False
    else:
        print("Still only " + str(currentNum) + " open classes at " + str(datetime.datetime.now()))

    time.sleep(10 * 60)  # checks every 10 minutes
