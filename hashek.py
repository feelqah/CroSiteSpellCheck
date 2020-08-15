from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def check_text(text):
    url = "https://ispravi.me"
    options = Options()
    #options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(url)

    textarea = driver.find_element_by_id("textarea")
    textarea.send_keys(text)

    check_button = driver.find_element_by_id("checkText")
    check_button.click()

    time.sleep(5)

    hascheck_errors = driver.find_elements_by_class_name("hascheck-error")
    suggestions_dict = dict()

    for error in hascheck_errors:
        driver.execute_script("arguments[0].scrollIntoView(true);", error)
        time.sleep(0.5)
        action = webdriver.ActionChains(driver)
        action.move_to_element(error)
        action.perform()

        time.sleep(1)
        suggestions = list()
        corrections = driver.find_elements_by_class_name("correction")

        for correction in corrections:
            suggestions.append(correction.text)
        time.sleep(1)

        suggestions_dict[error.text] = suggestions
        print("Pogresna rijec: %s" % error.text)
        print("Prijedlog ispravki: %s" % ', '.join(suggestions))
    #print(suggestions_dict)
    return suggestions_dict
    driver.close()
