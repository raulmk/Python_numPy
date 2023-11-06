import numpy as np
import csv
import matplotlib.pyplot as plt

def importar_archivos_nparray(archivo):
    dades = []

    with open(archivo, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for fila in csv_reader:
            dades.append(fila)

    dades_np = np.array(dades)
    return dades_np


def crear_grafico_tm(dades_np):
    filas_tm = np.array(dades_np[dades_np[:, 3] == 'TM'])
    resultado = []
    for i in filas_tm:
        if '2022-02' in i[0]:
            resultado.append(i)
    resultado = np.array(resultado)
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
                D5.append(i[4])
            case'X2' :
                X2.append(i[4])
            case'X4' :
                X4.append(i[4])
            case'X8' :
                X8.append(i[4])

  
  
    
    # plt.plot(dates, D5, label="D5", color= "r")
    # plt.plot(dates, X2, label="X2", color= "y")
    # plt.plot(dates, X4, label="X4", color= "b")
    # plt.plot(dates, X8, label="X8", color= "g")

    # plt.xlabel('Fechas')
    # plt.ylabel('Temperatura Media (°C)')
    # plt.title('Comparativa de Temperatura Media Diaria - Febrero 2022')
    # plt.legend()

    # plt.xticks(rotation=60)
    # plt.grid(True)

    # plt.show()

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
    plt.xticks(rotation=90)
    plt.show()

    return [D5, X2, X4, X8]

def calcula_temp_2023(temps_2022):
    D5 = temps_2022[0]
    X2 = temps_2022[1]
    X4 = temps_2022[2]
    X8 = temps_2022[3]


def main():
    estacions = importar_archivos_nparray("2020_MeteoCat_Estacions.csv")
    detall_estacions = importar_archivos_nparray("2022_MeteoCat_Detall_Estacions.csv")
    metadades = importar_archivos_nparray("MeteoCat_Metadades.csv")
    temp_mitj_2022_estacions = crear_grafico_tm(detall_estacions)
    calcula_temp_2023(temp_mitj_2022_estacions)

main()
