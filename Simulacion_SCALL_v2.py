import os
import Motor_SCALL_v1 as MtSll
from Procesos_Generales.Generador_PDF import generar_informe_completo # El archivo que crearemos para el PDF

class InterfazSCALL:
    def __init__(self):
        self.CONFIG_UI = {
            "nombre_proyecto": 'Captación de agua pluvial y gestión de residuos.\n"Cada gota cuenta cada residuo transforma"',
            "institucion": "Universidad Nacional Rosario Castellanos",
            "autor": 'Equipo 3',
        }
        self.CARPETA_RESULTADOS = "SCALL_Resultados"
        self.datos_finales = {} # Aquí "atrapamos" las variables para el PDF
        
        if not os.path.exists(self.CARPETA_RESULTADOS):
            os.makedirs(self.CARPETA_RESULTADOS)

    def bienvenida(self):
        print("\n" + "="*60)
        print("Bienvenid@ al sistema SCALL — Captación de Agua Pluvial UNRC")
        print("Este sistema transforma reciclaje PET en solución sustentable.")
        print("="*60)
        # Accedemos al texto que vive en tu motor
        print(MtSll.texto_materiales)
        print("\nVerificando materiales disponibles...\n")

    def preguntar_si_no(self, mensaje):
        while True:
            resp = input(mensaje).strip().lower()
            if resp in ("si", "no"):
                return resp
            print("Respuesta inválida. Solo 'si' o 'no'.")

    def ejecutar_flujo_completo(self):
        """Mantiene tu flujo original paso a paso"""
        self.bienvenida()

        # --- Verificación ---
        if self.preguntar_si_no("¿Cuentas con todos los materiales? (Si/No): ") == "no":
            print("Sin materiales no hay sistema SCALL.")
            return False

        print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
        print(MtSll.texto_pasos)

        if self.preguntar_si_no("\n¿Sistema SCALL construido exitosamente? (Si/No): ") == "no":
            print("Sistema no construido. Sin infraestructura no hay sistema de captacion pluvial.\nProceso finalizado.")
            return False

        # --- Cálculos y Inputs ---
        print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvial listo para operar!")
        print("Ahora veremos el area y volumen de agua pluvial que se puede captar en la UNRC.")
        print(f"\nÁrea total UNRC: {MtSll.area:.2f} m²")
        print(f"Volumen máximo captable: {MtSll.volumen_captable:.2f} m³\n")

        # Estas funciones las puedes dejar fuera o dentro de la clase
        porcentaje = self._seleccionar_porcentaje()
        area_c, vol_c = MtSll.calcular_volumen_captable(porcentaje)

        print(f"\nÁrea seleccionada: {area_c:.2f} m²")
        print(f"Volumen captable: {vol_c:.2f} m³\n")

        tipo, cant = self._seleccionar_botellas()
        litros, m3_almacen = MtSll.calcular_capacidad_almacenamiento(tipo, cant)

        print(f"\nCapacidad de almacenamiento: {litros:.0f} litros ({m3_almacen:.2f} m³)")

        util = vol_c
        if self.preguntar_si_no("¿Aplicar descarte inicial de 5 mm para limpieza? (Si/No): ") == "si":
            util = MtSll.calcular_descarte(area_c, vol_c)
            print(f"Volumen útil post-descarte: {util:.2f} m³")

        porcentaje_sistema = (m3_almacen / util * 100) if util > 0 else 0
        print(f"Capacidad del sistema respecto al volumen captable: {porcentaje_sistema:.2f}%\n")

        if self.preguntar_si_no("¿Está lloviendo en la UNRC? (Si/No): ") == "si":
            print("\nSistema activado:\n")
            print(MtSll.activado)
        else:
            print("\nEsperando lluvia para iniciar monitoreo...")
        
        # --- PREPARACIÓN DE DATOS PARA EL PDF ---
        
        # Aquí es donde "guardamos" las variables locales en el objeto
        self.datos_finales = {
            "Área total UNRC": f"{MtSll.area:.2f} m²",
            "Área seleccionada": f"{area_c:.2f} m²",
            "Volumen captable": f"{vol_c:.2f} m³",
            "Capacidad de almacenamiento": f"{m3_almacen:.2f} m³",
            "Volumen útil final": f"{util:.2f} m³",
            "Porcentaje de aprovechamiento": f"{porcentaje_sistema:.2f} %"
        }

        if self.preguntar_si_no("\n¿Desea generar gráficas e informe final? (si/no): ") == "si":
            print("----------------------------------------------")
            print("    Generación de Gráficas e Infome Final")
            generar_informe_completo(self.datos_finales) # Llamamos al PDF pasando los datos
            print("                Finalizado")
            print("----------------------------------------------")
            print('\n"Adiós, vuelve pronto y recuerda:\n💧 Cada Gota Cuenta, Cada Residuo Transforma ♻️"')
        else:
            print('\n"Adiós, vuelve pronto y recuerda:\n💧 Cada Gota Cuenta, Cada Residuo Transforma ♻️"')

    # Métodos privados para limpiar el flujo principal
    def _seleccionar_porcentaje(self):
        while True:
            try:
                p = float(input("Ingrese porcentaje de área a captar (0-100): "))
                if 0 < p <= 100: return p
            except: pass
            print("Valor inválido.")

    def _seleccionar_botellas(self):
        while True:
            t = input("Seleccione tipo de botella (1 = 2.5L | 2 = 3L): ")
            if t in ("1", "2"):
                try:
                    c = int(input("Cantidad de botellas interconectadas: "))
                    if c > 0: return t, c
                except: pass
            print("Datos inválidos.")

if __name__ == "__main__":
    app = InterfazSCALL()
    app.ejecutar_flujo_completo()
