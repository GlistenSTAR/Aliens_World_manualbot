from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from game import game
from config import page_url
import os
def main():
    # // chrome setting
    chrome_options = Options()
    # chrome_options.add_argument("--allow-running-insecure-content")
    # chrome_options.add_argument("user-data-dir=C:\\Users\\Charlie\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # chrome_options.add_extension(os.getcwd()+"\\anticaptcha-plugin_v0.54.crx")
    driver = webdriver.Chrome(executable_path="E:/Python/wax/chromedriver.exe", options=chrome_options)
    # driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.set_window_position(0,0)
    driver.set_window_size(900, 700)
    driver.get('https://all-access.wax.io/')

    driver.execute_script("window.open('https://play.alienworlds.io/','_blank')")
    game(driver)
if __name__ == '__main__':
    main()
    