#!/usr/bin/env python3
#_*_conding:utf-8_*_
#-----------------------------------------------------------------------------------
#By:Savioxt
#version='1.0'
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

print('                                                                             ')
print( '$$$$$$\            $$$$$$$\  $$\                                            ')
print('$$  __$$\           $$  __$$\ $$ |                                           ')
print('$$ /  $$ |$$$$$$$\  $$ |  $$ |$$ | $$$$$$\  $$$$$$$$\  $$$$$$\       ')
print('$$$$$$$$ |$$  __$$\ $$$$$$$\ |$$ | \____$$\ \____$$  |$$  __$$\     ')
print('$$  __$$ |$$ |  $$ |$$  __$$\ $$ | $$$$$$$ |  $$$$ _/ $$$$$$$$ |  ')
print('$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$  __$$ | $$  _/   $$   ____|        ')
print('$$ |  $$ |$$ |  $$ |$$$$$$$  |$$ |\$$$$$$$ |$$$$$$$$\ \$$$$$$$\         ')
print('\__|  \__|\__|  \__|\_______/ \__| \_______|\________| \_______|         ')
print('                                                                             ')
print('=================================================================')
print('                              | By:Savioxt |                                 ')
print('=================================================================')                                                                                                                                      

def bdados(url,id):
    print("BUSCANDO DADOS..")
    driver = webdriver.Firefox()
    driver.get(url)
    retorno = ""
    salva=open('temp.txt','w')
    for p in range(12):
        retorno = driver.find_element(By.XPATH,"//DIV[@id='"+id+"']/self::DIV")
        ck = driver.find_element(By.XPATH,"(//BUTTON[@class='pagination__button'])[2]")
        ck.click()
        salva.write(retorno.text+" \n")
    print("SALVANDO RELATORIOS DE PARTITADAS DE...")
    salva.close()
    driver.close()

def Crash():
    leitura = open('temp.txt','r')
    l2=leitura.readlines()

    ListaCrashN = list(filter(lambda x: x[-2].lower() in 'x', l2))
    ListaDateN = list(filter(lambda x: x[2].lower() in '/', l2))
    ListaCrashTemp=[]
    ListaCrash=[]
    ListaDate=[]

    for lista in ListaCrashN:
        ListaCrashTemp.append(lista.replace("x\n",""))
    for lista2 in ListaCrashTemp:
        ListaCrash.append(float(lista2.replace(",",".")[0:5]))
    for lista in ListaDateN:
        ListaDate.append(lista.replace("\n",""))
                        
    Dados = {
        "Crash": ListaCrash,
        "Data e Hora": ListaDate
    }

    DadosDF=pd.DataFrame(Dados)
    print(DadosDF['Crash'].value_counts())
    DadosDF.sort_values(by="Crash").to_csv('Crash.csv')
    print(DadosDF.sort_values(by="Crash"))
    print("Foi gerado Crash.csv")

def Double():
    leitura = open('temp.txt','r')
    l2=leitura.readlines()
    
    Double = list(filter(lambda x: x[2::1].lower() in '\n', l2))    
    HoraDataTemp = list(filter(lambda x: x[-2:2] in '\n', l2 ))
    DoubleData = list(filter(lambda x: x[2] in '/', HoraDataTemp))
    DoubleHora = list(filter(lambda x: x[2] in ':', HoraDataTemp))
    
    ListaDouble= []
    ListaData = []
    ListaHora = []

    for lista in Double:
        ListaDouble.append(int(lista.replace('\n','')))
    for lista in DoubleData:
        ListaData.append(str(lista.replace('\n','')))
    for lista in DoubleHora:
        ListaHora.append(str(lista.replace('\n','')))        

    Dados={
        "Double": ListaDouble,
        "Data": ListaData, 
        "Hora":ListaHora
        
    }
        
    DadosDF=pd.DataFrame(Dados)
    print(DadosDF['Double'].value_counts())
    DadosDF.sort_values(by='Double').to_csv('Double.csv')
    print(DadosDF.sort_values(by='Double'))
    print("Foi gerado Double.csv")

def Menu():
    print('+========+')
    print('|1-crash |')
    print('|2-Double|')
    print('|========|')
    print('|0-Sair  |')
    print('+========+')
    line=input(">>>>>>>>>>>>>>>>>>>>> :")
    if line=='1':
        bdados("https://blaze.com/pt/games/crash?modal=crash_history_index","history")
        Crash()
    elif line == '2':    
        bdados("https://blaze.com/pt/games/double?modal=double_history_index","history__double")
        Double()
    elif line == '0':
        exit()    
Menu()

