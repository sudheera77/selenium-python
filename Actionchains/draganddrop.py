from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class draganddropsample():
    def draganddrop(self):
        driver=webdriver.Firefox()
        driver.get("https://jqueryui.com/droppable")
        driver.switch_to.frame(0)
        source=driver.find_element_by_id("draggable")
        destination=driver.find_element_by_id("droppable")
        actions = ActionChains(driver)
        actions.click_and_hold(source).move_to_element(destination).release(source).perform()
        print("draganddrop sample")
        time.sleep(2)
obj=draganddropsample()
obj.draganddrop()