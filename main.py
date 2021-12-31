import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
PATH ="C:\Program Files (x86)\chromedriver.exe"



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def connect_to_moodle(driver, user_name, password):
    driver.get("https://lemida.biu.ac.il/")
    search_box1 = driver.find_element_by_id("login_username")
    search_box2 = driver.find_element_by_id("login_password")
    submit_button = driver.find_element_by_xpath("//input[@type='submit' and @value='התחברות']")
    search_box1.send_keys(user_name)
    # search_box2.send_keys(keyring.get_password("moodle",user_name))  #Get the password from the keyring
    search_box2.send_keys(password)
    submit_button.click()  # log in


def connect_to_course_from_main_page_of_moodle(driver, xPath_of_course):
    course_button = driver.find_element_by_xpath(xPath_of_course)
    course_button.click()

if __name__ == '__main__':
    #Set Up Driver:
    ########################################
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    #########################################
    connect_to_moodle(driver, "207424490", "Learning10")
    connect_to_course_from_main_page_of_moodle(driver,'//*[@id="fcl_227639_tabpanel2"]/ul/li[1]/a')
    time.sleep(2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
