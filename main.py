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
    for i in resultado:
        if (i[0] not in dates):
            dates.append(i[0])
        if i[2] == 'D5' :
            D5.append(i)

    dates = np.array(dates)
    D5np= D5
    
 


    lista_estaciones = []
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'D5'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X2'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X4'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X8'])
    
    plt.plot(dates, D5, label='Temperatura Media (TM)', color= "w")


    # Personaliza la gráfica
    plt.xlabel('Fechas')
    plt.ylabel('Temperatura Media (°C)')
    plt.title('Comparativa de Temperatura Media Diaria - Febrero 2022')
    plt.legend()

    plt.xticks(rotation=45)
    plt.grid(True)

    # Muestra la gráfica
    plt.show()


def main():
    estacions = importar_archivos_nparray("2020_MeteoCat_Estacions.csv")
    detall_estacions = importar_archivos_nparray("2022_MeteoCat_Detall_Estacions.csv")
    metadades = importar_archivos_nparray("MeteoCat_Metadades.csv")

    crear_grafico_tm(detall_estacions)


main()
