from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
from Procesos_Generales.Config_rutas import CARPETA_RESULTADOS, CARPETA_GRAFICAS, CARPETA_IMAGENES
import os

def generar_informe_completo(datos_scall):
    nombre_pdf = os.path.join(CARPETA_RESULTADOS, "Informe_Final_SCALL.pdf")

    doc = SimpleDocTemplate(nombre_pdf, pagesize=letter)
    estilos = getSampleStyleSheet()
    
    # Estilos de fuentes
    estilos.add(ParagraphStyle(name="Titulo", parent=estilos["Title"], fontSize=22, fontName='Times-Bold', alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Justificado", parent=estilos["Normal"], fontSize=12, fontName='Times-Roman', alignment=TA_JUSTIFY))
    estilos.add(ParagraphStyle(name="Center", parent=estilos["Heading2"], fontSize=18, fontName='Times-Bold', alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Tema1", parent=estilos["Heading2"], fontSize=12, fontName='Times-Bold', alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Tema2", parent=estilos["Heading2"], fontSize=11.5, fontName='Times-Bold'))

    story = []

    # Portada
    story.append(Spacer(1, 0.1*cm)) 
    story.append(Paragraph('Captación de agua pluvial y gestión de residuos.<br/>"Cada gota cuenta cada residuo transforma"', estilos["Titulo"]))
    story.append(Spacer(1, 0.2))
    story.append(Paragraph('Universidad Nacional Rosario Castellanos', estilos["Center"]))
    story.append(Spacer(1, 0.2*cm))
    
    # Resultados de la ejecución de SCALL
    story.append(Paragraph("Resultados de la Ejecución del Sistema", estilos["Tema2"]))
    story.append(Spacer(1, 0.2*cm))
    
    # Aquí volcamos los datos del diccionario 'datos_scall'
    for clave, valor in datos_scall.items():
        linea = f"<b>{clave}:</b> {valor}"
        story.append(Paragraph(linea, estilos["Normal"]))
        story.append(Spacer(1, 0.2*cm))

    # Resumen
    story.append(Paragraph("Resumen del Sistema de Captación de Agua Pluvial", estilos["Tema2"]))
    story.append(Spacer(1, 0.1*cm))

    resumen_texto = """ 
El sistema SCALL integra un motor de cálculo automatizado que permite estimar el potencial de captación pluvial de la unidad académica. A partir de las coordenadas del perímetro del edificio, se calcula el área efectiva de captación mediante el método geométrico del polígono irregular. Esta área constituye la base para estimar el volumen máximo de agua de lluvia que puede recolectarse.
Posteriormente, el sistema permite seleccionar un porcentaje del área total a utilizar, simulando diferentes escenarios de implementación progresiva del sistema. Con base en este valor, se determina el volumen de agua potencialmente captado durante eventos de precipitación.
Para el almacenamiento, el sistema dimensiona la capacidad del conducto construido con botellas PET interconectadas, considerando el tipo de botella y la cantidad disponible. De esta manera, se obtiene la capacidad real de almacenamiento en litros y metros cúbicos.
Finalmente, el sistema contempla un descarte inicial de agua de lluvia para limpieza de superficies, ajustando el volumen útil final disponible para aprovechamiento.
Todo el proceso se encuentra automatizado y genera reportes digitales que documentan los resultados obtenidos.
"""
    story.append(Paragraph(resumen_texto, estilos["Justificado"]))
    story.append(Spacer(1, 0.5*cm))
    
    # Imagen de Portada
    ruta_img = os.path.join(CARPETA_IMAGENES, "Portada.png")
    if os.path.exists(ruta_img):
        img = Image(ruta_img, width=16*cm, height=6*cm)
        story.append(img)
    else:
        story.append(Paragraph(f"Imagen no encontrada.", estilos["Normal"]))
    
    story.append(PageBreak())

    # Análisis
    story.append(Paragraph("Análisis de Perímetro y Área", estilos["Tema2"]))
    story.append(Spacer(1, 0.2*cm))

    explicacion_gauss = """
El desafío era medir con precisión el área del techo del edificio, pues no es un rectángulo simple, sino un polígono irregular con lados de diferentes 
y para calcular su área procedemos a utilizar el método poligonal “shoelace” o fórmula del área de Gauss, del matemático 
alemán Carl Friedrich Gauss y coordenadas usadas en el plano cartesiano con un requisito importante que deben estar listados en
 orden, ya sea en sentido horario o antihorario.
    """
    story.append(Paragraph(explicacion_gauss, estilos["Justificado"]))
    story.append(Spacer(1, 0.8*cm))
    
    # Gráfica de Perímetro
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Perimetro_area.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=12*cm, height=16*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))
    story.append(PageBreak())

    # ---- 5. ANÁLISIS DE PRECIPITACIÓN (TUS TEXTOS Y GRÁFICAS) ----
    story.append(Paragraph("Análisis de las Gráficas de Precipitación", estilos["Tema2"]))
    analisis_mm="""
Las gráficas de precipitación permiten visualizar el comportamiento histórico de las lluvias en la zona de estudio, identificando patrones temporales, variabilidad climática y periodos de mayor y menor disponibilidad hídrica.
"""
    story.append(Paragraph(analisis_mm, estilos["Justificado"]))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("Precipitación Histórica Anual (1961 - 2025)", estilos["Tema1"]))
    
    analisis_anual= """
La precipitación histórica anual muestra la evolución del volumen total de lluvia a lo largo del tiempo, lo que permite detectar tendencias de incremento, estabilidad o disminución en los niveles de captación potencial. Este análisis es clave para evaluar la viabilidad a largo plazo del sistema de recolección pluvial y anticipar escenarios futuros de abastecimiento.
"""
    story.append(Paragraph(analisis_anual, estilos["Justificado"]))
    story.append(Spacer(1, 0.8*cm))
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_mm_anual_historica.png")
    if os.path.exists(ruta_img):
        img = Image(ruta_img)
        img.drawWidth = 16 * cm
        img.drawHeight = 9 * cm
        story.append(img)
    else:
        story.append(Paragraph(f"Imagen no encontrada.", estilos["Normal"]))

    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph("Precipitación Histórica [Mes]", estilos["Tema1"]))
    story.append(Spacer(1, 0.1*cm))
    analisis_mes= """
La precipitación mensual evidencia la estacionalidad del régimen de lluvias. Se observan meses con alta concentración de precipitaciones, los cuales representan ventanas óptimas de captación y almacenamiento, frente a periodos secos donde el sistema depende del volumen previamente acumulado. Esta distribución mensual orienta el dimensionamiento estratégico del almacenamiento.
"""
    story.append(Paragraph(analisis_mes, estilos["Justificado"]))
    story.append(Spacer(1, 0.2*cm))
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_estadisticas_lluvia_mensual.png")
    if os.path.exists(ruta_img):
        img = Image(ruta_img)
        img.drawWidth = 16 * cm
        img.drawHeight = 9 * cm
        story.append(img)
    else:
        story.append(Paragraph(f"Imagen no encontrada.", estilos["Normal"]))


    story.append(Paragraph("Precipitación Histórica Diaria - [Mes]", estilos["Tema1"]))
    story.append(Spacer(1, 0.1*cm))
    analisis_dia= """
La precipitación diaria permite identificar eventos de lluvia intensos y su frecuencia. Estos picos representan oportunidades críticas de recolección, pero también ponen a prueba la capacidad hidráulica del sistema de conducción. Analizar esta variabilidad diaria ayuda a asegurar que la infraestructura pueda manejar tanto lluvias ligeras como precipitaciones abruptas sin pérdidas significativas.
"""
    story.append(Paragraph(analisis_dia, estilos["Justificado"]))
    story.append(Spacer(1, 0.8*cm))
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_estadisticas_lluvia_24h.png")
    if os.path.exists(ruta_img):
        img = Image(ruta_img)
        img.drawWidth = 16 * cm
        img.drawHeight = 9 * cm
        story.append(img)
    else:
        story.append(Paragraph(f"Imagen no encontrada.", estilos["Normal"]))

    story.append(PageBreak())

    story.append(Paragraph("Distribución Espacial de Puntos de Recolección: PET y HDPE.", estilos["Tema2"]))
    story.append(Spacer(1, 0.2*cm))
    analisis_pet ="""
La disposición actual favorece una recolección eficiente, minimizando la interferencia con las áreas de estudio y maximizando la visibilidad de los contenedores para el personal y alumnado.
"""
    story.append(Paragraph(analisis_pet, estilos["Justificado"]))
    story.append(Spacer(1, 1*cm))

    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Puntos_PET.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=12*cm, height=16*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))

    story.append(PageBreak())

    # ---- 6. CONCLUSIÓN (TU TEXTO ORIGINAL) ----
    story.append(Paragraph("Conclusión General", estilos["Tema2"]))
    
    conclusion_texto = """
El sistema SCALL no solo permite estimar el potencial de captación pluvial, sino que integra una propuesta de reutilización de residuos PET como estructura de conducción, consolidando una solución de bajo costo, replicable y ambientalmente sostenible. La automatización de cálculos y la generación de reportes garantizan resultados consistentes, trazables y fácilmente actualizables ante cambios en los parámetros de diseño.
Por otra parte, el análisis de las gráficas de precipitación evidencia que el comportamiento de la lluvia no es constante ni uniforme, sino dinámico y estacional. Comprender esta variabilidad transforma los datos climáticos en información operativa, permitiendo diseñar un sistema de captación más eficiente, resiliente y alineado con las condiciones reales del entorno.
En síntesis, SCALL convierte el análisis de datos ambientales en una herramienta de toma de decisiones, donde cada gota de lluvia y cada residuo reutilizado se convierten en una estrategia sostenible con impacto técnico y social.
    """
    story.append(Paragraph(conclusion_texto, estilos["Justificado"]))

    # Finalización
    doc.build(story)
    print(f"\n📄 Informe académico generado con datos actuales.")