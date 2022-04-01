from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore
import os

# PATH and driver settings
PATH = os.getenv("chrome")
option = Options()
option.headless = True
service = Service(PATH)
driver = webdriver.Chrome(service=service, options=option)
driver.get('https://www.sodexobeneficios.com.br/sodexo-club/login/')

# XPaths
email = driver.find_element(by=By.XPATH,
                          value="/html/body/main/section/section/div/div[1]/div[1]/div/form[1]/div[1]/input")
password = driver.find_element(by=By.XPATH,
                               value="/html/body/main/section/section/div/div[1]/div[1]/div/form[1]/div[2]/input")
enter = driver.find_element(by=By.XPATH, value="/html/body/main/section/section/div/div[1]/div[1]/div/form[1]/button")

# Action
email.send_keys(os.getenv("email"))
password.send_keys(os.getenv("password"))
sleep(1)
enter.click()
sleep(5)

# XPaths - Result
refeicao = driver.find_element(by=By.XPATH,
                               value="/html/body/main/section/section[1]/div[1]/div[2]/div[1]/div/div[1]/div/span[2]/span")
alimentacao = driver.find_element(by=By.XPATH,
                                  value="/html/body/main/section/section[1]/div[1]/div[2]/div[2]/div/div[1]/div/span[2]/span")

# Result
print(Fore.RED + '-------------------------------------------')
print(Fore.RED + "Vale Refeição")
print(Fore.GREEN + ('R$ ' + refeicao.text))
print(Fore.RED + "Vale Alimentação")
print(Fore.GREEN + ('R$ ' + alimentacao.text))
print(Fore.RED + '-------------------------------------------')

driver.quit()
