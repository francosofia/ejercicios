import pandas as pd
import numpy as np

contendio = pd.read_csv("usu_hogar_T324.txt", sep=";")

print("Cantidad de columnas:",contendio.shape[1])

print("Cantidad de filas:", contendio.shape[0])

print("Tipos de columnas:", contendio.dtypes)

print(contendio.index)