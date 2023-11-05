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
    resultado = filas_tm[filas_tm[:, 0].__contains__("2022-02")]
    for i in resultado:
        print(i)


    lista_estaciones = []
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'D5'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X2'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X4'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'X8'])
    lista_estaciones.append(filas_tm[filas_tm[:, 2] == 'D6'])
    
    for i in range(0, 4):
        colores = ["b" , "r", "w", "g"]
        # Obtiene las fechas y valores de temperatura media
        fechas = np.array([np.datetime64(fecha) for fecha in lista_estaciones[i][:, 0]])
        temperatura_media = lista_estaciones[i][:, 4].astype(float)

        # Crea el gráfico
        plt.figure(figsize=(12, 6))

        # Plotea los datos de temperatura media
        plt.plot(fechas, temperatura_media, label='Temperatura Media (TM)', color=colores[i])


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
