from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

usuario = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
usuario.send_keys("Tu correo o usuario de Instagram")

password = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("Tu password")


login_boton = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")
login_boton.click()

time.sleep(4)

driver.get('https://www.instagram.com/explore/people/')

time.sleep(3)


def delay():
    time.sleep(60)
    driver.get('https://www.instagram.com/explore/people/')
    time.sleep(3)
    ciclo()

def ciclo():
    for i in range(100):
        boton_seguir = driver.find_element(By.XPATH, f"/html/body/div[1]/section/main/div/div[2]/div/div/div[{i+1}]/div[3]/button")
        boton_seguir.click()
        time.sleep(2)
        #Aqui cada 6 cuentas que siga va tomar un descanso de un minuto
        #puedes cambiarle 
        if 5<i+1<7:
           delay()

try:
    ciclo()
except:
    time.sleep(10)
    ciclo()