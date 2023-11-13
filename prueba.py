import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PruebaSelenium(unittest.TestCase):
    def setUp(self):
        print("Se ejecuta antes de cada prueba")
        self.driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
                "version": "119.0",
                "enableVNC": True  # Habilita VNC
            }
        )

    def test_haz_clic_en_contacto_y_agrega_email(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        
        # Haz clic en el enlace "Contact"
        element_contacto = self.driver.find_element(By.CSS_SELECTOR, 'a[data-toggle="modal"][data-target="#exampleModal"]')
        element_contacto.click()

        # Encuentra el campo de entrada por su id y agrega un correo electrónico
        element_email = self.driver.find_element(By.ID, 'recipient-email')
        element_email.send_keys('Pedro@example.com')  

        # Encuentra el campo de entrada por su id y agrega el nombre de contacto
        element_name = self.driver.find_element(By.ID, 'recipient-name')
        element_name.send_keys('Pedro')  

         # Encuentra el campo de entrada por su id y agrega el nombre de contacto
        element_message = self.driver.find_element(By.ID, 'message-text')
        element_message.send_keys('hola este es mi mensaje')  

        # Encuentra el botón "Send message" por su texto y haz clic en él
        element_boton = self.driver.find_element(By.XPATH, '//button[text()="Send message"]')
        element_boton.click()

        # Aserciones para verificar si la acción fue exitosa
        success_message = self.driver.find_element(By.ID, 'submit-message')
        self.assertTrue(success_message.is_displayed(), "El mensaje de éxito no está presente")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
