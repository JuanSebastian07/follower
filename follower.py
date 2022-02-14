from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys
import time


web = webdriver.Firefox()
web.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

no_seguidos = 0
 
 
def login():
    usuario = web.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
    usuario.send_keys("Tu_cuenta_de_gmail")

    password = web.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("Tu_clave")


    login_boton = web.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")
    login_boton.click()
 
def open_followers(account_instagram):
    web.get("https://www.instagram.com/" + account_instagram + "/followers/")
    time.sleep(5)
    web.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
 
 
def scroll_followers(minutes):
    pop_up_window = web.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]")
    #/html/body/div[6]/div/div/div[2] 
    timeout = time.time() + 60 * minutes
    print(f'-->{timeout}')
    print(f'-->{time.time()}')
    while True:
        if time.time() > timeout:
            break
        web.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
        time.sleep(1)
 
 
def follow_followers():
    #Variable global
    global no_seguidos

    list_followers = web.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul")
    #/html/body/div[6]/div/div/div[2]/ul/div 
    for child in list_followers.find_elements(By.CSS_SELECTOR,"li"):
        user_name = child.find_element(By.CSS_SELECTOR,".notranslate").text
        follow_button = child.find_element(By.CSS_SELECTOR,"button")
        print(user_name)
        print("----")
        print(follow_button.text)
        if "Follow" == follow_button.text:
            follow_button.click()
            time.sleep(2)
            if "Follow" == follow_button.text:
                no_seguidos = 0
                print("Descanso")
                time.sleep(120)
            time.sleep(random.randint(1,3))
            no_seguidos = no_seguidos + 1
            print(f'N°{no_seguidos}')
            print(user_name + "->seguido")
            if(no_seguidos == 20):
                no_seguidos = 0
                time.sleep(120)

        else:
            print("Ya lo sigues")
        time.sleep(1)
 
 
sources = ["Cuenta_a_las_que_deseas_seguir_sus_seguidores"]
login()
time.sleep(5)
for account in sources:
    open_followers(account)
    time.sleep(5)
    scroll_followers(10)
    follow_followers()
 
 
