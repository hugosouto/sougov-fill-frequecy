from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize the WebDriver (example with Chrome)
driver = webdriver.Chrome('/path/to/chromedriver') # Update with your ChromeDriver path

# Function to perform the required actions
def perform_actions():
    try:
        # Wait and click the 'Saldo do Dia' div
        saldo_dia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pill.saldo-negativo"))
        )
        saldo_dia.click()

        # Wait and click the 'Informar Ocorrência' link
        informar_ocorrencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "link-text"))
        )
        informar_ocorrencia.click()

        # Wait for the option to be clickable and then select it
        teletrabalho_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='11']"))
        )
        teletrabalho_option.click()

        # Wait and click the 'Salvar' button
        salvar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSalvar"))
        )
        salvar_button.click()

        # Wait for the page to reload/refresh
        sleep(5)

    except Exception as e:
        print("Error occurred:", e)
        return False
    return True

# Navigate to the webpage
driver.get('https://sougov.sigepe.gov.br/sougov/FichaFrequencia')

# Repeat the actions until the 'Informar Ocorrência' link is no longer found
while perform_actions():
    if not driver.find_elements(By.CLASS_NAME, "link-text"):
        break

# Close the browser
driver.quit()
