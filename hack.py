from itertools import product as p
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":

    # generating keywords
    ran = [i for i in range(10)]
    print(ran)

    # generating possiblities
    possiblities = list(p(ran, repeat=4))
    print(len(possiblities))

    # selenium conncetion
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://saranathan468.examly.io")
    time.sleep(10)

    # user credentials
    emailId = "grthayalan18@gmail.com"
    password = "1018@thayalan"

    # reference to the elements
    e = browser.find_element_by_id("emailAddress")
    p = browser.find_element_by_id("password")
    b = browser.find_element_by_class_name("ladda-button")

    # authenticating
    e.send_keys(emailId)
    p.send_keys(password)

    # triggering login button
    b.click()

    time.sleep(10)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    # selecting the test module
    m = browser.find_elements_by_class_name("inprogress")[1]
    m.click()
    # print(m)


    # browser.quit()


