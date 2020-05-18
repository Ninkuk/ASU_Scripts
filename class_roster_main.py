from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import json

url_canvas = 'https://canvas.asu.edu'
browser = webdriver.Firefox()


def get_student_roster(courses):
    if "/courses/27320" in courses:
        courses.remove("/courses/27320")

    files_list = []

    for course in courses:
        browser.get(url_canvas + course + '/users')
        time.sleep(3)
        last_height = browser.execute_script("return document.body.scrollHeight")
        students = []

        while True:

            source = browser.page_source
            data = BeautifulSoup(source, "html.parser")

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            table = data.find('table', {'class': 'roster'})
            for student in table.findAll('a'):
                if student.text not in students:
                    students.append(student.text)

            time.sleep(3)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                course_title = table.find('div', {'class': 'section'}).text
                formatted_course_title = course_title[0:3] + '_' + course_title[4:7]

                file_path_name_w_ext = './courses/' + formatted_course_title + '.json'
                with open(file_path_name_w_ext, 'w') as fp:
                    json.dump(students, fp)

                files_list.append(formatted_course_title)
                break
            last_height = new_height

    with open('./courses/classes_list.json', 'w') as fp:
        json.dump(files_list, fp)


def get_classes():
    # browser.get(url_canvas + '/courses')

    source = browser.page_source
    data = BeautifulSoup(source, "html.parser")
    body = data.find("body")

    courses = []

    for link in body.find_all("a"):
        if re.search("/courses/", link.get("href")):
            courses.append(link.get("href"))

    get_student_roster(courses)


def sign_in(username, password, duo):
    browser.get(url_canvas)

    username_selector = browser.find_element_by_id("username")
    password_selector = browser.find_element_by_id("password")
    username_selector.send_keys(username)
    password_selector.send_keys(password)
    browser.find_element_by_class_name("submit").click()

    if duo:
        input("When finished authenticating, press ENTER")

    time.sleep(1)
    get_classes()


def get_user_credentials():
    username = input("Please enter your ASU ID")
    password = input("Please enter your password")

    while True:
        duoInput = input(
            "Does your account have duo authentication? (Y/N) If you don't know what this is Press N.").casefold()
        duo = False

        if duoInput == "y".casefold():
            print("When you reach the authentication page, please authenticate and press enter in the terminal")
            duo = True
            break
        elif duoInput == "n".casefold():
            break
        else:
            print("Please enter Y or N")

    sign_in(username, password, duo)


if __name__ == '__main__':
    get_user_credentials()
