#!/usr/bin/python

#Importar selenium. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

#Ejecutar el navegador. 
driver = webdriver.Firefox()
#Ingresar a la ruta URL. 
driver.get("http://192.168.0.1/") #Aquí irá la URL a la que quieras ir.
#Eseperar que la página recargue. 
time.sleep(2)


#Datos para ingresar en el login.
name = "yilver"
password = "Yil09Que06#"


"""Login"""
usuario = driver.find_element("xpath" ,'//*[@id="userName"]')
clave = driver.find_element("xpath" ,'//*[@id="pcPassword"]') #Selecciona elementos xpath.
usuario.send_keys(name) #teclea el texto.
clave.send_keys(password)
#Hacer click en el login.
boton = driver.find_element("xpath", '//*[@id="loginBtn"]').click()


"""Dentro del router"""
"""Primer frame"""
frame = driver.find_element("xpath", '//*[@id="frame1"]')
#driver.switch_to.frame(frame)
control_acceso = driver.find_element("xpath", '//*[@id="menu_fw"]').click()
#reglar = driver.find_element("xpath", '//*[@id="menu_fwrule"]').click()



"""
#cerrar la alerta JS
time.sleep(1)
alert = Alert(driver) 
alert.accept() 


#cerrar el navegador
time.sleep(2)
driver.close()

	//*[@id="fwid3"]
"""
