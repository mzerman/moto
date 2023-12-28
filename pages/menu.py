from wrappers.base_page import BasePage

# spare parts
spare_parts = '//a[@href="/s/lp-ersatzteile/"]'
filter = '//div[@class="jqs-content"]/ul/li/a[@href="/produkte/filter-101/"]'
breake_system = '//div[@class="jqs-content"]/ul/li/a[@href="/produkte/bremsanlagen-114/"]'
header_with_page_title = '//div[@id="hits"]/h1'


class PageTriangle(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver)

