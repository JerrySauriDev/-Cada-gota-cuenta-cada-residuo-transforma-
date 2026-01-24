from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
import os
from Config_rutas import CARPETA_RESULTADOS, CARPETA_GRAFICAS
import Simulacion_SCALL_v2 as Scall
import Motor_SCALL_v1 as MtSll

def generar_informe():
    nombre_pdf = os.path.join(CARPETA_RESULTADOS, "Informe_Final_SCALL.pdf")

    doc = SimpleDocTemplate(nombre_pdf, pagesize=letter)
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name="Titulo", parent=estilos["Title"], fontName='Times-Bold', alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Justificado", parent=estilos["Normal"], fontSize=11, fontName='Times-Roman', alignment=TA_JUSTIFY))
    estilos.add(ParagraphStyle(name="Center", parent=estilos["Heading2"], fontName='Times-Bold', alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Tema", parent=estilos["Heading2"], fontSize=11, fontName='Times-Bold'))

    story = []

    # ---- PORTADA ----
    story.append(Spacer(1, 20))
    story.append(Paragraph('Captación de agua pluvial y gestión de residuos.\n"Cada gota cuenta cada residuo transforma"', estilos["Titulo"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph('Universidad Nacional Rosario Castellanos', estilos["Center"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph("Resumen del Sistema de Captación de Agua Pluvial", estilos["Tema"]))

    # ---------- RESUMEN ----------
    story.append(Spacer(1, 0.2*cm))

    resumen_texto = """
El sistema SCALL integra un motor de cálculo automatizado que permite estimar el potencial de captación pluvial de la unidad académica. A partir de las coordenadas del perímetro del edificio, se calcula el área efectiva de captación mediante el método geométrico del polígono irregular. Esta área constituye la base para estimar el volumen máximo de agua de lluvia que puede recolectarse.
Posteriormente, el sistema permite seleccionar un porcentaje del área total a utilizar, simulando diferentes escenarios de implementación progresiva del sistema. Con base en este valor, se determina el volumen de agua potencialmente captado durante eventos de precipitación.
Para el almacenamiento, el sistema dimensiona la capacidad del conducto construido con botellas PET interconectadas, considerando el tipo de botella y la cantidad disponible. De esta manera, se obtiene la capacidad real de almacenamiento en litros y metros cúbicos.
Finalmente, el sistema contempla un descarte inicial de agua de lluvia para limpieza de superficies, ajustando el volumen útil final disponible para aprovechamiento.
Todo el proceso se encuentra automatizado y genera reportes digitales que documentan los resultados obtenidos.
"""
    story.append(Paragraph(resumen_texto, estilos["Justificado"]))
    story.append(PageBreak())

    # Insertar gráfica con diferente altura
    story.append(Paragraph("Análisis de Perímetro y Área", estilos["Tema"]))
    story.append(Spacer(1, 0.2*cm))

    Explicacion_1 = """
El desafío era medir con precisión el área del techo del edificio, pues no es un rectángulo simple, sino un polígono irregular con lados de diferentes 
y para calcular su área procedemos a utilizar el método poligonal “shoelace” o fórmula del área de Gauss, del matemático 
alemán Carl Friedrich Gauss y coordenadas usadas en el plano cartesiano con un requisito importante que deben estar listados en
 orden, ya sea en sentido horario o antihorario.
"""
    story.append(Paragraph(Explicacion_1, estilos["Justificado"]))
    story.append(Spacer(1, 1*cm))
    
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Perimetro_Area.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=12*cm, height=16*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))
    story.append(PageBreak())

    # ---- LISTA DE GRÁFICAS ----
    graficas = [
        ("Precipitación Histórica [Año]", "Grafica_mm_anual_historica.png"),
        ("Precipitación Histórica [Mes]", "Grafica_estadisticas_lluvia_mensual.png"),
        ("Precipitación Histórica Diaria - [Mes]", "Grafica_estadisticas_lluvia_24h.png"),
    ]

    for titulo, archivo in graficas:
        story.append(Paragraph(titulo, estilos["Tema"]))
        story.append(Spacer(1, 0.3*cm))

        ruta_img = os.path.join(CARPETA_GRAFICAS, archivo)

        if os.path.exists(ruta_img):
            img = Image(ruta_img)
            img.drawWidth = 16 * cm
            img.drawHeight = 9.5 * cm
            story.append(img)

        else:
            story.append(Paragraph(f"Imagen no encontrada: {archivo}", estilos["Normal"]))

    story.append(PageBreak())
    story.append(Paragraph("Distribución Espacial de Puntos de Recolección: PET y HDPE.", estilos["Tema"]))
    story.append(Spacer(1, 0.2*cm))

    Explicacion_4 ="""
La disposición actual favorece una recolección eficiente, minimizando la interferencia con las áreas de estudio y maximizando la visibilidad de los contenedores para el personal y alumnado.
"""
    story.append(Paragraph(Explicacion_4, estilos["Justificado"]))
    story.append(Spacer(1, 1*cm))

    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Puntos_PET.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=12*cm, height=16*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))

    story.append(PageBreak())

    # ---------- CONCLUSIÓN ----------
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("Conclusión General", estilos["Tema"]))
    story.append(Spacer(1, 0.4*cm))

    conclusion_texto = """
El sistema SCALL no solo permite estimar el potencial de captación pluvial, sino que 
también integra una propuesta de reutilización de residuos PET como estructura de conducción, 
fomentando una solución de bajo costo, replicable y ambientalmente sostenible.
La automatización del cálculo y la generación de reportes garantizan resultados consistentes, 
trazables y fácilmente actualizables ante cambios en los parámetros de diseño. Esto convierte al 
sistema SCALL en una herramienta práctica para evaluar proyectos de captación pluvial en entornos 
educativos y comunitarios.
"""
    story.append(Paragraph(conclusion_texto, estilos["Justificado"]))
    datos = Scall.main()
    datos_reporte = {
    "Área total UNRC (m²)": f"{MtSll.area:.2f}",
    "Área seleccionada (m²)": f"{Scall.main().area_c:.2f}",
    "Volumen captable (m³)": f"{Scall.vol_c:.2f}",
    "Capacidad de almacenamiento (m³)": f"{Scall.m3_almacen:.2f}",
    "Volumen útil final (m³)": f"{Scall.util:.2f}",
    "Porcentaje de aprovechamiento (%)": f"{Scall.porcentaje_sistema:.2f}"
    }

    doc.build(story)

if __name__ == "__main__":
    generar_informe()
