import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mm_verificados_nuevo.csv') # Cargar los datos limpios y verificados desde el archivo

# Preparar los datos para la gráfica de máximas, medias y mínimas mensuales
meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
         'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'] 

# Usamos .set_index('AÑO') para que sea más fácil localizar las filas por nombre
df_stats = df.set_index('AÑO')

# Extraemos los valores de las filas de estadísticas
Maxima = df_stats.loc['MÁXIMA', meses]
Minima = df_stats.loc['MÍNIMA', meses]
Media = df_stats.loc['MEDIA', meses]

# Se crea la gráfica de líneas para Máxima, Media y Mínima
plt.figure(figsize=(12, 6)) # Tamaño de la figura
plt.rcParams['axes.facecolor'] = "#f9f9f9e6" # Fondo ligeramente gris para resaltar líneas

# Dibujamos las líneas con estilos personalizados
plt.plot(meses, Maxima, label='Máxima', marker='o', color= "#AC0A0A", linewidth=2, zorder=2)
plt.plot(meses, Media, label='Media', marker='s', color= "#0D995F", linestyle='--', linewidth=2.5, zorder=2)
plt.plot(meses, Minima, label='Mínima', marker='v', color="#005F85", linewidth=2, zorder=3)

# Función para evitar que los números se encimen
for i in range(len(meses)): # Iterar sobre cada mes
    # Valor de Máxima (arriba del punto) 
    plt.text(i, Maxima[i] + (Maxima.max()*0.07), f'{Maxima[i]:.1f}',
             ha='center', va='bottom', color='#AC0A0A', fontweight='bold', fontsize=9)
    # Valor de Media (arriba del punto)
    plt.text(i, Media[i] + (Maxima.max()*0.02), f'{Media[i]:.1f}', 
             ha='center', va='bottom', color='#0D995F', fontweight='bold', fontsize=9)
    # Valor de Mínima (Solo si es > 0)
    if Minima[i] > 0.01:
        plt.text(i, Minima[i] - (Maxima.max()*0.03), f'{Minima[i]:.1f}', 
                 ha='center', va='top', color='#005F85', fontweight='bold', fontsize=9)
    
# Configuración visual de la gráfica
plt.title('Lluvia 24h Chalco 1961-2025', fontsize=18, fontweight='bold', pad=20) # Título de la gráfica
plt.ylabel('Precipitación (mm)', fontsize=13, labelpad=10) # Etiqueta del eje Y
plt.xlabel('Meses', fontsize=13, labelpad=10) # Etiqueta del eje X
plt.xticks(rotation=30, fontsize=11) # Rotación de las etiquetas del eje X
plt.yticks(fontsize=11) # Tamaño de las etiquetas del eje Y
plt.grid(True, linestyle='--', alpha=0.5, zorder=0) # Cuadrícula de fondo
plt.legend(loc='upper right', frameon=True, shadow=True, fontsize=12) # Leyenda de la gráfica

# Ajustar el límite de Y para que los textos no se corten
plt.ylim(Minima.min() - 10, Maxima.max() + (Maxima.max()*0.15)) # Margen superior e inferior

# Mostrar y guardar la imagen
plt.tight_layout()
plt.savefig('grafica_estadisticas_lluvia.png')
plt.show()