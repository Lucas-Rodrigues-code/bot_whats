#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importando bibliotecas 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# In[3]:


#Links e Xpaths
WPP_LINK = "https://web.whatsapp.com/"
NEW_MSG_BUTTON = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
SEARCH_CONTACT_FIELD = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
FISRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]'
TYPE_FIELD = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
SEND_BUTTON = '//*[@id="main"]/footer/div[1]/div[3]/button'


# In[4]:


#inicializando o driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(WPP_LINK)


# In[5]:


#criando a função
def send_message(nome,mensagem):
    new_msg_button = driver.find_element_by_xpath(NEW_MSG_BUTTON)
    new_msg_button.click()
    sleep(1)
    search_field = driver.find_element_by_xpath(SEARCH_CONTACT_FIELD)
    search_field.click()
    search_field.send_keys(nome)
    sleep(1)
    first_contact = driver.find_element_by_xpath(FISRST_CONTACT)
    first_contact.click()
    sleep(1)
    type_field= driver.find_element_by_xpath(TYPE_FIELD)
    type_field.click()
    type_field.send_keys(mensagem)
    send_button= driver.find_element_by_xpath(SEND_BUTTON)
    send_button.click()
    sleep(1)


# In[6]:


lista_de_contatos = ["Captain Qwark","Gado D+","Vieira",]
lista_de_codigos = [124123,125124123,5125121]
mensagem= "Olá {}! Seu código de rastreamento é {}"


# In[7]:


for contato,codigo in zip(lista_de_contatos,lista_de_codigos):
    send_message(nome=contato, mensagem=mensagem.format(contato,codigo))


# In[ ]:




