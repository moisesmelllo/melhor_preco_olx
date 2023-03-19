from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_oprions = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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


driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.com/')  # navegar até um site
driver.maximize_window()  # maximizar a janela
driver.refresh()  # recarrega página atual
driver.get(driver.current_url)  # recarrega página atual
driver.back()  # volta à página
driver.forward()  # navega 1 vez para frente
print(driver.title)  # Obtem o titulo da página
print(driver.current_url)  # Obtem URL(endereço) da página atual
print(driver.page_source)  # Obtem o código fonte da página atual
# obtem o texto dentro de um elemento

print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').text)
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').get_attribute("href"))

driver.close()  # Fecha a janela atual
input()
