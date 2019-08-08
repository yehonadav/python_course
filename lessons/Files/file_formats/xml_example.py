from qaviton.drivers.xml_driver import XMLDriver
import requests

xml: str = requests.get('https://google.com').text

driver = XMLDriver(xml)

elements = driver.find_by_xpath('//div')
for element in elements:
    print(element)
