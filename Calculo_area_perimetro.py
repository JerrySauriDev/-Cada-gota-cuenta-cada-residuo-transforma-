import pandas as pd
import numpy as np

# Carga de datos
df_mm_anual =pd.read_csv('Datos_Dia_mm_validados.csv') # Lluvia maxima 
df_Co = pd.read_csv('Coeficiente.csv') # Coeficiente de escorrentia de acuerdo al material del techo
df_medidas = pd.read_csv('Medidas_unidad_academica.csv') # Medidas de la unidad academica

# Procedimiento para el calculo de area y perimetro
medidas = dict(zip(df_medidas['Medidas'], df_medidas['Metros'])) # Convertimos a diccionario para fácil acceso
enfrente, atras = medidas['Enfrente'], medidas['Atras'] # Se definen coordenadas basadas en las medidas
lat_der, lat_izq = medidas['Lateral derecho'], medidas['Lateral izquierda'] # Se definen coordenadas basadas en las medidas

# Cálculo de área (Polígono)
vertices = [(0, 0), (enfrente, 0), (atras, lat_der), (0, lat_izq)] # Proyectamos los puntos
x = [v[0] for v in vertices]
y = [v[1] for v in vertices]
area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) # Fórmula del área del polígono
perimetro = enfrente + lat_der + atras + lat_izq # Cálculo del perímetro

# Extracción del coeficiente de escorrentia
material_interes = "Techos impermeabilizados o cubiertos con materiales duros (p. ej. Tejas)"
Co = df_Co.loc[df_Co['Material o tipo de construcción'] == material_interes, 'Kc'].item()

# Extracción de mm máxima
columna_a_extraer = 'PROMEDIO'
try:
    mm_maxima_seleccionado = df_mm_anual.loc[df_mm_anual['AÑO'] == 'MÁXIMA', columna_a_extraer].item()
except KeyError:
    print(f"Error: La columna '{columna_a_extraer}' no existe en el archivo.")
    mm_maxima_seleccionado = 0

# Convertimos la columna AÑO a string por seguridad y quitamos espacios en blanco
df_mm_anual['AÑO'] = df_mm_anual['AÑO'].astype(str).str.strip()
fila_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].copy()
reporte = fila_maxima.set_index('AÑO').rename_axis('', axis=0).T # .rename_axis('Datos', axis=1) cambia el nombre que aparece sobre las columnas

# Cálculo de Volumen
mm_maxima = mm_maxima_seleccionado / 1000 # Convertir mm a m3
volumen_captable = area * mm_maxima * Co # m3 volumen utilizable de agua pluvial sin descarte

# Descarte de seguridad (5mm)
volumen_descarte = (5 / 1000) * area * Co
volumen_neto = max(0, volumen_captable - volumen_descarte)

# Reporte final
print(reporte)
print("-" * 30)
print(f"Perimetro: {perimetro:.2f} m \nÁrea: {area:.3f} m²")
print(f"Volumen captable: {volumen_captable:.2f} m³\nVolumen final con descarte: {volumen_neto:.2f} m³")

# Guardar reporte
guardar_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].squeeze() # Usamos squeeze() para convertir el DataFrame de 1 fila en una Serie
guardar_maxima.to_csv('Datos_maxima_nuevo.csv', header=False) # Guardar como nueva tabla
