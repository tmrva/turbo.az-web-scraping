from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from time import sleep

driver = webdriver.Chrome('C:/Users/Asus/Downloads/chromedriver_win32')

driver.get("https://turbo.az/autos?q%5Bsort%5D=&q%5Bmake%5D%5B%5D=4&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=180&q%5Bused%5D=&q%5Bregion%5D%5B%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bcategory%5D%5B%5D=&q%5Byear_from%5D=&q%5Byear_to%5D=&q%5Bcolor%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bonly_shops%5D=&q%5Bprior_owners_count%5D%5B%5D=&q%5Bseats_count%5D%5B%5D=&q%5Bmarket%5D%5B%5D=&q%5Bcrashed%5D=1&q%5Bpainted%5D=1&q%5Bfor_spare_parts%5D=0")
with open('e300new.csv', 'w', encoding = 'utf-8') as e300new_csv:
    csv_writer = writer(e300new_csv)
    csv_writer.writerow(['price', 'year', 'engine', 'distance', 'city'])

    while True:
        cars = driver.find_elements(By.CLASS_NAME, 'products-i__bottom')
        for car in cars:
            price = car.find_element(By.CLASS_NAME, 'product-price').text
            year, engine, distance = car.find_element(By.CLASS_NAME, 'products-i__attributes').text.split(', ')
            city, time = car.find_element(By.CLASS_NAME, 'products-i__datetime').text.split(', ')

            csv_writer.writerow([price, year, engine, distance, city])
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
            next_button.click()
            sleep(5)
        except NoSuchElementException:
            driver.quit()