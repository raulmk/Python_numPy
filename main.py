import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
import random as rd
import statistics as stats

def importar_archivos_nparray(archivo):
    dades = []

    with open(archivo, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for fila in csv_reader:
            dades.append(fila)

    dades_np = np.array(dades)
    return dades_np

def filtrar(filtrado, dades_np):
    filas_tm = np.array(dades_np[dades_np[:, 3] == filtrado])
    resultado = []
    for i in filas_tm:
        if '2022-02' in i[0]:
            resultado.append(i)
    resultado = np.array(resultado)
    
    return resultado

def crear_grafico_tm(dades_np):
    resultado = filtrar('TM', dades_np)
    dates= []
    D5 = []
    X2 = []
    X4 = []
    X8 = []
    for i in resultado:
        if (i[0] not in dates):
            dates.append(i[0])
        match i[2]:
            case'D5' :
                D5.append(float(i[4]))
            case'X2' :
                X2.append(float(i[4]))
            case'X4' :
                X4.append(float(i[4]))
            case'X8' :
                X8.append(float(i[4]))

    #Dades en un sol gráfic

    plt.plot(dates, D5, label="D5", color= "r")
    plt.plot(dates, X2, label="X2", color= "y")
    plt.plot(dates, X4, label="X4", color= "b")
    plt.plot(dates, X8, label="X8", color= "g")

    plt.xlabel('Fechas')
    plt.ylabel('Temperatura Media (°C)')
    plt.title('Comparativa de Temperatura Media Diaria - Febrero 2022')
    plt.legend()

    plt.xticks(rotation=60)
    plt.grid(True)

    plt.show()
    plt.close()

    #Dades en 4 gráfics amb subplot.

    plt.subplot(1,4,1)
    plt.plot(dates, D5, label="D5", color= "r")
    plt.xticks(rotation=90)
    plt.subplot(1,4,2)
    plt.plot(dates, X2, label="X2", color= "y")
    plt.xticks(rotation=90)
    plt.subplot(1,4,3)
    plt.plot(dates, X4, label="X4", color= "b")
    plt.xticks(rotation=90)
    plt.subplot(1,4,4)
    plt.plot(dates, X8, label="X8", color= "g")

    plt.xlabel('Fechas')
    plt.ylabel('Temperatura Media (°C)')
    plt.title('Comparativa de Temperatura Media Diaria en diferentes gráficos- Febrero 2022')
    plt.legend()

    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()
    plt.close()

    return [D5, X2, X4, X8, dates]

def calcula_temp_2023(temps_2022):

    #Calculem temperatures mitjanes amb les dades anteriors i fem l'histograma
    Temps = [temps_2022[0],
             temps_2022[1],
             temps_2022[2],
             temps_2022[3]]
    dfTemps= pd.DataFrame(Temps, index = ["D5", "X2", "X4", "X8"], columns= temps_2022[4])
    mitj=[]
    for i in dfTemps.columns:
        mitj.append(dfTemps[i].mean())
    dfMitj= pd.DataFrame(mitj)
    print(dfMitj)
    dfMitj.plot(kind="hist")
    plt.ylabel('Numero de dias')
    plt.xlabel('Temperatura Media (°C)')
    plt.title('Distribución de valores de temperatura media Febrero 2022')
    plt.xlim(0,20)
    plt.show()
    

    #Calculem les temperatures de 2023
    temps_2023=[]
    for i in range(1,28):
        temps_2023.append(rd.choice(mitj))
    temps_2023_mitj= pd.DataFrame(temps_2023)
    temps_2023_mitj.plot(kind="hist")
    plt.ylabel('Numero de dias')
    plt.xlabel('Temperatura Media (°C)')
    plt.title('Distribución de valores de temperatura media Febrero 2023')
    plt.xlim(0,20)
    plt.show()   

def calcul_precipitacions_2023(dades_np):
    resultado = filtrar('PPT', dades_np)
    lista_dias = []
    contador = 0
    lista = []
    for i in resultado:
        if contador < 3:
            lista.append(i)
        else:
            lista_dias.append(lista)
            lista = []
            contador = 0
            lista.append(i)

        contador = contador +1

    lista_ayuda = []
    lista_resultado = []
    contador_dias_llueve = 0
    for i in lista_dias:
        for j in i:
            if j[4] != '0':
                lista_ayuda.append(1)
                
            else:
                lista_ayuda.append(0)
        print(lista_ayuda)
        print(stats.mode(lista_ayuda) )
        if stats.mode(lista_ayuda) == 1:
            lista_resultado.append([i[0][0], True])
            contador_dias_llueve = contador_dias_llueve +1
        else:
            lista_resultado.append([i[0][0], False])
        lista_ayuda = []
    
    porcentaje_llueve = contador_dias_llueve / 28 * 100
    porcentaje_no_llueve = (28- contador_dias_llueve) / 28 * 100
    porcentajes = [porcentaje_llueve, porcentaje_no_llueve]
    etiquetas = ["Plou", "No plou"]

    #QUESITOS
    fig, ax = plt.subplots()
    ax.pie(porcentajes, labels = etiquetas, autopct="%0.1f %%")
    plt.show()

    fig, ax = plt.subplots()
    ax.barh(etiquetas, width = porcentajes)
    plt.xlim(0,100)
    plt.show()
    


def main():
    estacions = importar_archivos_nparray("2020_MeteoCat_Estacions.csv")
    detall_estacions = importar_archivos_nparray("2022_MeteoCat_Detall_Estacions.csv")
    metadades = importar_archivos_nparray("MeteoCat_Metadades.csv")
    temp_mitj_2022_estacions = crear_grafico_tm(detall_estacions)
    calcula_temp_2023(temp_mitj_2022_estacions)
    calcul_precipitacions_2023(detall_estacions)
main()
