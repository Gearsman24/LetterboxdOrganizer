# Internal Libraries for Download
import time

# External Libraries for Download
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def download(username="", password=""):
    # Check for Valid Username and Password
    if(username == "" and password == ""):
        return False

    # Open Letterboxd Login URL
    browser = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://letterboxd.com/sign-in/'
    browser.get(url)
    browser.maximize_window()
    signin_title = browser.title
    time.sleep(1.5)

    # Get Sign In Elements
    username_el = browser.find_element_by_name("username")
    password_el = browser.find_element_by_name("password")
    signin_btn_el = browser.find_element_by_css_selector(".button.-action") # Sign In Button CSS
    time.sleep(0.5)

    # Sign In
    username_el.send_keys(username)
    password_el.send_keys(password)
    time.sleep(1)
    signin_btn_el.click()
    time.sleep(1.5)

    # Check for Successful Login
    if(signin_title == browser.title):
        browser.quit()
        return False

    # Open Letterboxd Export URL -> Download Data to Computer
    url = "https://letterboxd.com/data/export/"
    browser.execute_script(f"window.open('{url}')")
    browser.switch_to_window(browser.window_handles[-1])
    time.sleep(10) # Give time to download
    browser.quit()
    return True