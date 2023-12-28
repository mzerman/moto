import time

from wrappers.base_page import BasePage
from enum import Enum

select_brand_dropdown = '//select[@name="manufacturer_id"]'
selected_brand = '//a[@id="jqs-vehicle-brands-2-button"]'
select_model_dropdown = '//select[@name="model_id"]'
select_type_dropdown = '//select[contains(@class, "jqs-vehicle-type")]'
delete_button = '//div[contains(@class, "col2")]/div/a'
vehicle_name_display = '//span[contains(@class, "vehicle-name-display")]/span/a/..'
save_vehicle_button = '//button[contains(@class, "jqs-save-vehicle")]'

# css selector
select_brand_dropdown_css = '#jqs-vehicle-brands-2'
select_model_dropdown_css = '#hp-hero-vehicle-selector > form > ul.vehicle-chain.jqs-new-vehicle-selector > li:nth-child(3) > div > select'
select_type_dropdown_css = '#hp-hero-vehicle-selector > form > ul.vehicle-chain.jqs-new-vehicle-selector > li:nth-child(4) > div > select'


class VehicleType(Enum):
    car = 1
    truck = 2
    motorbike = 3
    farm = 4
    boat = 5


def vehicle_tab(tab_name_value): return f'//div[contains(@class, "vehicle-tab")]/a[{tab_name_value}]'


class ChooseVehicle(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver)

    def switch_tab(self, tab_name):
        if not isinstance(tab_name, VehicleType):
            raise TypeError('direction must be an instance of Direction Enum')
        self.click_element(vehicle_tab(tab_name.value))

    def select_brand_by_text(self, text):
        self.make_element_visible_by_js(select_brand_dropdown_css)
        self.select_dropbox_by_visible_text(select_brand_dropdown, text)
        self.make_element_unvisible_by_js(select_brand_dropdown_css)

    def select_model_by_text(self, text):
        self.make_element_visible_by_js(select_model_dropdown_css)
        self.select_dropbox_by_visible_text(select_model_dropdown, text)
        self.make_element_unvisible_by_js(select_model_dropdown_css)

    def select_type_by_text(self, text):
        self.make_element_visible_by_js(select_type_dropdown_css)
        self.select_dropbox_by_visible_text(select_type_dropdown, text)
        self.make_element_unvisible_by_js(select_type_dropdown_css)

    def click_save_vehicle(self):
        self.click_element(save_vehicle_button)

    def get_chosen_vehicle_name(self):
        str_with_name = self.get_element_text(vehicle_name_display)
        name = str_with_name[:-7]
        return name
