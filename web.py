#!/usr/bin/python

#Importar selenium. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from datetime import datetime


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
"""Control de Acceso y Regla"""
time.sleep(1) #Es necesario esperar 1 segundo.
frame = driver.find_element("xpath", '//*[@id="frame1"]')
driver.switch_to.frame(frame)
control_acceso = driver.find_element("xpath", '//*[@id="menu_fw"]').click()
reglar = driver.find_element("xpath", '//*[@id="menu_fwrule"]').click()

"""Segundo frame"""
"""Bloque de usuario"""
driver.switch_to.default_content()
frame = driver.find_element("xpath", '//*[@id="frame2"]')
driver.switch_to.frame(frame)
#Seleccionamos el dispositivo.
checkbox = driver.find_element("xpath", '//*[@id="fwid6"]').click()
bloquear = driver.find_element("xpath", '/html/body/div[1]/div/div/div/p[7]/input[2]').click()

"""tercer frame"""
"""Finalizar sesión"""
driver.switch_to.default_content()
frame = driver.find_element("xpath", '//*[@id="frame1"]')
driver.switch_to.frame(frame)
finalizar_sesion = driver.find_element("xpath", '//*[@id="menu_logout"]').click()


"""Cerrar Alerta JavaScript"""
time.sleep(1)
alert = Alert(driver) 
alert.accept() 


"""Cerrar el navegador."""
time.sleep(2)
driver.close()

"""
	Mayeuri: //*[@id="fwid4"]
"""