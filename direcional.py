from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(ChromeDriverManager().install())

navegador.get("https://www.podemorar.com.br/")
navegador.find_element_by_xpath('//*[@id="btnAcessarMinhaConta"]').click()

elem = navegador.find_element_by_xpath('//*[@id="inputEmail"]')
elem.clear()
elem.send_keys('youremail@email.com')

elemPass = navegador.find_element_by_xpath('//*[@id="inputPassword"]')
elemPass.clear()
elemPass.send_keys('yourpass')

navegador.find_element_by_xpath('//*[@id="btnAcessar"]').click()