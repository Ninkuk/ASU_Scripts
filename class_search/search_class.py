from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import datetime
from class_search import notifications


def search_for_class(search_url, class_name):
    if is_class_open(search_url):
        notifications.send_notification(
            "Class Opened",
            class_name + " just opened!",
            "Found at " + str(datetime.datetime.now())
        )
    else:
        print("No open " + class_name + " class found at " + str(datetime.datetime.now()) + " :(")


def is_class_open(search_url):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(search_url)

    time.sleep(1)

    data = BeautifulSoup(browser.page_source, "html.parser")
    table = data.find("table", {"id": "CatalogList"})
    return table is not None
