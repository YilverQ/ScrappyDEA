#!/usr/bin/python

#Importar selenium. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import json


#Ejecutar el navegador. 
driver = webdriver.Firefox()


"""Estados"""
def getEstados():
	#Ingresar a la ruta URL. 
	driver.get("https://codigosplanteles.info/")
	time.sleep(2)

	cajaEstados = driver.find_element("xpath" ,'/html/body/div[1]/div[1]/div/div/main/article/div/div[3]/div/div/div[3]')
	estados = cajaEstados.find_elements(By.CLASS_NAME, "uagb-tax-link")

	# Iterar sobre cada estado
	lista_enlaces_estados = []
	for estado in estados:
		enlace = estado.get_attribute("href")
		titulo = estado.find_element(By.CLASS_NAME, "uagb-tax-title").text
		lista_enlaces_estados.append({"Estado": titulo, "Enlace": enlace})

	return lista_enlaces_estados



def getEscuelas(link_estado):
    driver.get(link_estado)
    lista_enlaces_escuelas = []

    while True:
        caja_escuelas = driver.find_element("xpath", '//*[@id="page"]')
        links = caja_escuelas.find_elements(By.TAG_NAME, 'a')

        try:
            load_more_button = driver.find_element("xpath", '//*[@class="ast-load-more no-more active"]')
            if load_more_button:
                break
        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

    for link in links:
        if link.get_attribute("rel") == "bookmark":
            enlace = link.get_attribute("href")
            lista_enlaces_escuelas.append(enlace)

    return lista_enlaces_escuelas



lista_enlaces_estados = getEstados()
lista_enlaces_escuelas = []
for estado in lista_enlaces_estados: 
	lista_escuelas = getEscuelas(estado["Enlace"])
	lista_enlaces_escuelas.append({estado["Estado"] : lista_escuelas})

	with open("Escuelas.json", "w") as file:
		json.dump(lista_enlaces_escuelas, file, indent=4)

	print(estado["Estado"], len(lista_escuelas))