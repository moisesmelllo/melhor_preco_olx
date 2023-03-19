from random import randint
from time import sleep
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_oprions = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_oprions.add_argument(argument)

    # Uso de configurações experimentais
    chrome_oprions.add_experimental_option('prefs', {
        # Desabilitar a configuração de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    drivers = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_oprions)
    return drivers


driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/')
sleep(1)

botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
botao_windows.click()
botao_windows.send_keys(Keys.DOWN)

input('')
driver.close()
