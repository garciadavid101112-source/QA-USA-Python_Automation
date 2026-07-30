from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[text()="Supportive"]/..')
    TAXI_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    ACTIVE_PLAN_LOCATOR = (By.XPATH, "//div[contains(@class, 'tcard')][.//div[text()='Supportive']]")
    PHONE_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Phone number"]')
    PHONE_LOCATOR = (By.CLASS_NAME, 'np-text')
    ENTER_PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, "input#phone.input")
    SAVED_PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, ".np-text")
    NEXT_LOCATOR = (By.CSS_SELECTOR, "button.button.full")
    SMS_LOCATOR = (By.ID, "code")
    CONFIRM_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    ACTIVE_PAYMENT_METHOD_LOCATOR = (By.XPATH,'//div[contains(@class,"pp-button") and contains(@class,"filled")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[contains(@class,"pp-button") and .//div[text()="Payment method"]]')
    ADD_CARD_LOCATOR = (By.XPATH, '//img[@class="pp-plus"]/..')
    CARD_NUMBER_LOCATOR = (By.ID,"number")
    CARD_CODE_LOCATOR = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    PAYMENT_METHOD_TEXT_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    COMMENT_LOCATOR = (By.ID, "comment")
    BLANKET_SLIDER_LOCATOR = (By.XPATH, '//div[contains(@class,"r-sw-label") and contains(text(),"Blanket and handkerchiefs")]/following::span[contains(@class,"slider")][1]')
    BLANKET_CHECKBOX_LOCATOR = (By.CLASS_NAME, 'switch-input')
    ORDER_REQUIREMENTS_ARROW_LOCATOR = (By.CSS_SELECTOR, "div.reqs-arrow")
    ORDER_REQUIREMENTS_ARROW_OPEN_LOCATOR =(By.CSS_SELECTOR, "div.reqs-arrow open")
    ICE_CREAM_PLUS_LOCATOR = (By.CSS_SELECTOR, ".counter-plus")
    ICE_CREAM_COUNT_LOCATOR = (By.CSS_SELECTOR, ".counter-value")
    CODE_INPUT_LOCATOR = (By.ID, "code")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Confirm')]")
    CLICK_ORDER_TAXI_BUTTON = (By.CLASS_NAME, 'smart-button-wrapper')
    CAR_SEARCH_LOCATOR = (By.CSS_SELECTOR, ".order-header-title")




    def __init__(self, driver):
        self.driver = driver

    def _wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(locator))

    def enter_from_location(self, from_destination):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_destination)

    def enter_to_location(self, to_destination):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_destination)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def click_call_a_taxi(self):
        self.driver.find_element(*self.TAXI_LOCATOR).click()

    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def get_supportive_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR).get_attribute('class')

    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_BUTTON_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.ENTER_PHONE_NUMBER_LOCATOR).send_keys(phone_number)

    def click_next(self):
        self.driver.find_element(*self.NEXT_LOCATOR).click()

    def enter_phone_code(self, phone_code):
        self.driver.find_element(*self.SMS_LOCATOR).send_keys(phone_code)

    def click_confirm(self):
        self.driver.find_element(*self.CONFIRM_LOCATOR).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_LOCATOR).text

    def get_payment_method(self):
        return self.driver.find_element(*self.ACTIVE_PAYMENT_METHOD_LOCATOR).get_attribute("class")

    def get_payment_method_text(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_TEXT_LOCATOR).text

    def click_payment_method(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.PAYMENT_METHOD_LOCATOR)).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ADD_CARD_LOCATOR)).click()

    def enter_card_number(self, card_number):
        number = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located( self.CARD_NUMBER_LOCATOR))
        number.send_keys(card_number)
        number.send_keys(Keys.TAB)

    #def click_card_code(self):
        #self.driver.find_element(*self.CARD_CODE_LOCATOR).click()

    def enter_card_code(self, card_code):
        code = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.CARD_CODE_LOCATOR))
        code.send_keys(card_code)

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def enter_comment(self, message):
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(message)

    def get_comment(self):
        return self.driver.find_element(*self.COMMENT_LOCATOR).get_attribute("value")

    def click_blanket_slider(self):
        self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def get_blanket_slider_class(self):
        return self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).get_attribute("class")

    def is_blanket_selected(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX_LOCATOR).is_selected()

    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def add_ice_cream(self):
        for i in range(2):
            self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def get_ice_cream_count(self):
        return self.driver.find_element( *self.ICE_CREAM_COUNT_LOCATOR).text

    def click_code_input(self):
        code_input = self.driver.find_element(*self.CODE_INPUT_LOCATOR)
        code_input.click()

    def enter_code(self, code):
        code_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CODE_INPUT_LOCATOR))
        code_input.clear()
        code_input.send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def click_order_taxi_button(self):
        self.driver.find_element(*self.CLICK_ORDER_TAXI_BUTTON).click()

    def get_car_search(self):
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).text






