from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(ChromeDriverManager().install())

# Goes to website and click 'area do cliente' button
navegador.get("https://www.mobtelecom.com.br/")
navegador.find_element_by_xpath('//*[@id="root"]/header/nav/div[4]/button').click()

# Accept cokkies
# navegador.find_element_by_xpath('/html/body/div[2]/div/a[2]').click()

# Fullfill the CPF impyt
elem = navegador.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/form/input[1]')
elem.clear()
elem.send_keys('00000000000') #Your CPF goes here

# Fullfill the PASSWORD imput
elemPass = navegador.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/form/input[2]')
elemPass.clear()
elemPass.send_keys('*******') #Your Password goes here

# Click on 'ENTRAR' button, via form submit
navegador.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/form').submit()

# Time to load page in seconds
navegador.implicitly_wait(20)

# Click on 'Minhas faturas' button
navegador.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/a').click()

# Finaly click on 'Download fatura' button
navegador.find_element_by_xpath('/html/body/div[3]/div[1]/form/table/tbody/tr/td[4]/button[2]').click()
