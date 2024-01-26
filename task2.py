import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from lxml import etree


class ChemicalElement:
    def __init__(self, atomic, name, weight):
        self.atomic = atomic
        self.name = name
        self.weight = weight


class TestPeriodicTable(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.selenium_service = Service(executable_path=ChromeDriverManager(driver_version='119.0.6045.105').install())
        self.driver = webdriver.Chrome(service=self.selenium_service, options=self.options)

    def tearDown(self):
        self.driver.quit()

    def test_periodic_table_elements(self):
        self.driver.get('https://ptable.com/?lang=ru')

        html = self.driver.page_source  # Получаем HTML страницы
        tree = etree.HTML(html)
        elements = tree.xpath("*//li/abbr")  # Получаем все нужные элементы

        chemical_elements = []

        for el in elements:  # Парсинг элементов
            atomic_num = int((el.xpath("../b/text()"))[0])
            name_el = el.xpath("../abbr/text()")[0].strip()
            weight_el = el.xpath("../data/text()")[0].strip("()")

            ch_element = ChemicalElement(atomic_num, name_el, weight_el)
            chemical_elements.append(ch_element)

        self.assertEqual(118, len(chemical_elements))  # Проверка, что все элементы получены

        for el in chemical_elements:  # Вывод элементов
            print(f"Atomic: {el.atomic}, Name: {el.name}, Weight: {el.weight}")


if __name__ == '__main__':
    unittest.main()
