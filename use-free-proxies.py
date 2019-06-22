from selenium import webdriver
from time import sleep
def get_proxies(driver):
    url = "https://free-proxy-list.net/"
    driver.get(url)
    proxies = []
    proxy_table = driver.find_elements_by_xpath('//*[@id="proxylisttable"]/tbody/tr')
    for x in proxy_table:
        row_data = x.find_elements_by_tag_name('td')
        proxy = row_data[0].text+":"+row_data[1].text
        proxies.append(proxy)
    return proxies

driver = webdriver.Chrome()
proxies = get_proxies(driver)
driver.close()
for proxy in proxies:
    PROXY = proxy
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--proxy-server=http://%s' % PROXY)
    driver = webdriver.Chrome(options=options)
    url="https://whatismyipaddress.com/"
    driver.get(url)
    sleep(10)
    #Most free proxies will often get proxy server errors.
    driver.close()