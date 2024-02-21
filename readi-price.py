from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

navegador = webdriver.Chrome(ChromeDriverManager().install())

# Goes to website and click 'area do cliente' button
navegador.get("https://readi.com.br/")
navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div[1]/div[3]/button[2]').click()

# Time to load page in seconds
navegador.implicitly_wait(20)

# Fullfill the email impyt
elem = navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/form/div[1]/div/input')
elem.clear()
elem.send_keys('youremail@email.com')

# Fullfill the PASSWORD imput
elemPass = navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/form/div[3]/div/input')
elemPass.clear()
elemPass.send_keys('yourpass')

# Click on 'ENTRAR' button, via form submit
navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/form/button').submit()

# Time to load page in seconds
navegador.implicitly_wait(20)

# Click on 'Scanner Inicial' button
#navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/main/div/div[3]/div[1]/div[2]/div[2]/button[1]').click()
navegador.find_element(By.CLASS_NAME, "adopt-c-TjWCe").click()

# Time to load page in seconds
navegador.implicitly_wait(20)

# Click on 'Adopt button' button
navegador.find_element_by_xpath('//*[@id="adopt-accept-all-button"]').click()

# Time to load page in seconds
navegador.implicitly_wait(40)

# Click on 'Iniciar Scanner Inicial' button -- Not used because the RPA does not find this element (i don't now why)
#navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[3]/div[3]/button').click()

# Skip directly to the 'Scanner Inicial' page
navegador.get("https://readi.com.br/sistema/imovel-scanner/imoveis?isScannerCompleto=initial")

# Time to load page in seconds
navegador.implicitly_wait(20)

# Click on 'Iniciar Scanner Inicial' button
navegador.find_element_by_xpath('//*[@id="continueButton"]').click()

# Click on 'Continuar' button
navegador.find_element_by_xpath('//*[@id="successButton"]').click()

# Click on 'Ok Modal' button
navegador.find_element_by_xpath('/html/body/div[3]/div[3]/button').click()

# Time to load page in seconds
navegador.implicitly_wait(20)
navegador.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/span[2]')

# Finally, prints the page with the service amount
navegador.save_screenshot("image.png")
image = Image.open("image.png")
image.show()
