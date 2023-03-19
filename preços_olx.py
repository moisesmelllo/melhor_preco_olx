import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_oprions = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_oprions.add_argument(argument)

    # Uso de configurações experimentais
    chrome_oprions.add_experimental_option('prefs', {
        # Desabilitar a configuração de download
        'diwnload.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_oprions)
    return driver


# navegar até o site
driver = iniciar_driver()
driver.get('https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=monitor&sp=2')
sleep(5)
while True:
    # Carregar todos elementos da tela movendo até o final da página e depois ao topo
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(2)
    # Encontrar os titulos
    titulos = driver.find_elements(By.XPATH, "//div[@class='sc-12rk7z2-7 kDVQFY']//h2")
    # Encontrar os preços
    precos = driver.find_elements(By.XPATH, "//div[@class='sc-1kn4z61-1 dGMPPn']//span")
    # Encontrar os links
    links = driver.find_elements(By.XPATH, '//a[@data-lurker-detail="list_id"]')
    # Guardar isso em um arquivo .csv
    for titulo, preco, link in zip(titulos, precos, links):
        with open('Downloads/precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
            link_processado = link.get_attribute('href')
            arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
    # Fazer isso para todas as paginas
    try:
        botao_proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima pagina']")
        sleep(2)
        botao_proxima_pagina.click()
    except:
        print('fim!')
        break
