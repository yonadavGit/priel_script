import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
COURSE_PATH = "https://lemida.biu.ac.il/course/view.php?id=67199"
DOWNLOADS_DIR_PATH = r"C:\Users\Yonad\Downloads\priel_course_files"
HOW_MUCH_SLEEP = 60 * 60 * 24
MOODLE_PASS = "Learning10"
MOODLE_USERNAME = "207424490"


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


def connect_to_course_from_main_page_of_moodle_through_xPath(driver, xPath_of_course):
    course_button = driver.find_element_by_xpath(xPath_of_course)
    course_button.click()


def connect_to_course_from_main_page_of_moodle_through_url(driver, url):
    driver.get(url)


def download_all_files_from_course_page(driver):
    file_buttons = driver.find_elements_by_class_name("instancename")
    num_of_buttons = len(file_buttons)
    i = 0
    while (i < num_of_buttons):
        file_buttons[i].click()
        if driver.current_url != COURSE_PATH:
            connect_to_course_from_main_page_of_moodle_through_url(driver, COURSE_PATH)
        file_buttons = driver.find_elements_by_class_name("instancename")
        i += 1


if __name__ == '__main__':
    while True:
        # Set Up Driver:
        ########################################

        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": DOWNLOADS_DIR_PATH,
                 "download.prompt_for_download": False,  # To auto download the file
                 "download.directory_upgrade": True,
                 "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome

                 }
        # prefs['download.default_directory'] = "C:\Users\Yonad"
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
        driver.maximize_window()
        #########################################

        connect_to_moodle(driver, MOODLE_USERNAME, MOODLE_PASS)
        connect_to_course_from_main_page_of_moodle_through_url(driver, COURSE_PATH)
        time.sleep(2)
        # file_button = driver.find_element_by_xpath('//*[@id="module-1533723"]/div/div/div[2]/div/a/span')
        # file_button.click()
        download_all_files_from_course_page(driver)

        driver.quit()
        time.sleep(HOW_MUCH_SLEEP)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
