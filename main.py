import time
import data
import helpers
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options=webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", capabilities['goog:loggingPrefs'])
        cls.driver = webdriver.Chrome(options=options)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page=UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)

        assert routes_page.get_from_location() == data.ADDRESS_FROM
        assert routes_page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        time.sleep(2)

        assert "active" in routes_page.get_supportive_plan()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()

        routes_page.click_phone_number()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next()

        code = retrieve_phone_code(self.driver)
        routes_page.enter_phone_code(code)
        routes_page.click_confirm()
        time.sleep(2)

        assert routes_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        routes_page.click_payment_method()
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)

        routes_page.enter_card_code(data.CARD_CODE)

        routes_page.click_link_button()

        assert routes_page.get_payment_method_text() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        assert routes_page.get_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        routes_page.click_blanket_slider()

        assert routes_page.is_blanket_selected()


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        for i in range(2):
            routes_page.click_ice_cream_plus()

        assert routes_page.get_ice_cream_count() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive_plan()
        routes_page.click_phone_number()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next()
        phone_code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_code(phone_code)
        routes_page.click_confirm_button()
        routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.click_order_taxi_button()

        assert routes_page.get_car_search() == "Car search"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()