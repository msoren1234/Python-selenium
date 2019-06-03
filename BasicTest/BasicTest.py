from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def basic_test():
    # Create chrome Driver
    driver = webdriver.Chrome("../Drivers/chromedriver3")

    # Open test page
    url = "https://www.wixmeup.co.il/test-automation"
    driver.get(url)

    driver.maximize_window()

    num1_text_element = driver.find_element_by_xpath("//input[@id='comp-jv2bkkx0input']")
    num2_text_element = driver.find_element_by_xpath("//input[@id='comp-jv2bldt0input']")
    calc_button_element = driver.find_element_by_xpath("//span[@id='comp-jv2bmxzglabel']")
    drop_down_element = Select(driver.find_element_by_xpath("//select[@id='comp-jvf52vybcollection']"))

    num1_text_element.send_keys("7")
    num2_text_element.send_keys("4")
    drop_down_element.select_by_visible_text('MINUS')

    calc_button_element.click()
    time.sleep(1)

    result_text_element = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/main[1]/div[2]/div[2]/"
                                               "div[1]/div[1]/div[2]/div[1]/div[1]/section[2]/div[2]/div[1]/div[1]/"
                                               "div[2]/div[1]/div[1]/div[1]/div[8]/p[1]/span[1]/span[1]/span[1]")

    try:
        assert "Automation" in driver.title
        assert "3" in result_text_element.text, "Value should be 11"
    except NameError:
        print("Something  went wrong")

    driver.quit()


#Run Method
#basic_test()

if __name__ == '__main__':
    basic_test()


# dropdown = new Select(driver.findElement(By.xpath("//select[@id='comp-jvf52vybcollection']")));
# WebElement
# calcButton = driver.findElement(By.xpath("//span[@id='comp-jv2bmxzglabel']"));





