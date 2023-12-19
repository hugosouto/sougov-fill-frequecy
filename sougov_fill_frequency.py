# from http.server import executable
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep

# from userdata.userdata import username, password

# # Initialize the WebDriver (example with Chrome)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # driver = webdriver.Chrome()

# # Function to perform the required actions
# def perform_actions():
#     try:
#         # Wait and click the 'Saldo do Dia' div
#         saldo_dia = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pill.saldo-negativo"))
#         )
#         saldo_dia.click()

#         # Wait and click the 'Informar Ocorrência' link
#         informar_ocorrencia = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "link-text"))
#         )
#         informar_ocorrencia.click()

#         # Wait for the option to be clickable and then select it
#         teletrabalho_option = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//option[@value='11']"))
#         )
#         teletrabalho_option.click()

#         # Wait and click the 'Salvar' button
#         salvar_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "btnSalvar"))
#         )
#         salvar_button.click()

#         # Wait for the page to reload/refresh
#         sleep(5)

#     except Exception as e:
#         print("Error occurred:", e)
#         return False
#     return True

# # Navigate to the webpage
# driver.get('https://sougov.sigepe.gov.br/sougov/login')

# # Enter login and password
# login = driver.find_element(By.ID, 'username')

# # Repeat the actions until the 'Informar Ocorrência' link is no longer found
# while perform_actions():
#     if not driver.find_elements(By.CLASS_NAME, "link-text"):
#         break

# # Close the browser
# driver.quit()








from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from userdata.userdata import username, password
from selenium_stealth import stealth


# Initialize the WebDriver (example with Chrome)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Hugo\GitHub\sougov-fill-frequecy\chromedriver\chromedriver.exe")


# Enable stealth mode
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    # stealth(
    #     driver: Driver,
    #     user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
    #     languages: [str] = ["en-US", "en"],
    #     vendor: str = "Google Inc.",
    #     platform: str = "Win32",
    #     webgl_vendor: str = "Intel Inc.",
    #     renderer: str = "Intel Iris OpenGL Engine",
    #     fix_hairline: bool = False,
    #     run_on_insecure_origins: bool = False,
    # )

# Function to log in
def login(cpf, password):
    try:
        driver.get('https://sougov.sigepe.gov.br/sougov/login')
        wait = WebDriverWait(driver, 10)

        # Wait for the login button and scroll into view
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "btnLogarGov")))
        driver.execute_script("arguments[0].scrollIntoView(true);", login_button)

        # Wait for any overlapping elements to disappear (adjust the selector as needed)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "img[src*='sougov.sou_govbr_azul.png']")))

        # Click the login button
        login_button.click()

        # Enter CPF
        cpf_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "accountId"))
        )
        cpf_input.send_keys(cpf)

        # Click on 'Continuar' button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "enter-account-id"))
        )
        continue_button.click()

        # Enter Password
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_input.send_keys(password)

        # Click on 'Entrar' button
        enter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-button"))
        )
        enter_button.click()

        sleep(5)  # Wait for redirection or page load

    except Exception as e:
        print("Error occurred during login:", e)
        driver.quit()

# Call the login function with your CPF and password
login(username, password)

# Navigate to the Ficha Frequencia page
driver.get('https://sougov.sigepe.gov.br/sougov/FichaFrequencia')

# Function to perform the required actions after logging in
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

# Repeat the actions until the 'Informar Ocorrência' link is no longer found
while perform_actions():
    if not driver.find_elements(By.CLASS_NAME, "link-text"):
        break

# Close the browser
driver.quit()
