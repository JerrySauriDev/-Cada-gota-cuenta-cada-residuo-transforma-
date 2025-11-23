#Inicio
# Bienvenida al programa
print(f"\nBienvenid@, nuestro sistema busca transformar el reciclaje de PET y HDPE como una propuesta sustentable y\n"
    f"sostenible para captar y reutilizar el agua de la lluvia dentro de la Universidad Nacional Rosario Castellanos.\n")
print(f"Pasos para la captación de agua pluvial.")
print(f"Requerimos recoleccion de plasticos que seran reutilizados para armados de modulos de almacenamiento"
    f"y contruir el sistema de captación con demas materiales necesarios.\n")

# Declaracion de variables y funciones
print("Materiales requeridos\n")
material =(f"1.-PET suficiente\n"
    f"2.-Canaletas\n"
    f"3.-Filtro primario (malla o tela)\n"
    f"4.-Tubo de bajada\n"
    f"5.-Filtro secundario (arena, grava, carbón)\n"
    f"6.-Depósito para almacenamiento\n"
    f"7.-Llave de salida\n"
    f"8.-Tornillos, alambre, cinta\n"
    f"9.-Manguera\n")
print(material) # Se llama la variable material con uso de print

creacion =(f"1.-Colocar una canaleta en el borde del techo para recolectar el agua de la lluvia\n"
    f"2.-Conectar la canaleta a un tubo o embudo inicial que dirija el agua hacia la pared\n"
    f"3.-Fijar botellas PET cortadas (en forma de canal o media caña) a lo largo de la pared, formando una bajada continua\n"
    f"4.-Unir las botellas con cinta resistente, tornillos o alambre, sobre una estructura de soporte (rejilla, madera reciclada\n"
    f"5.-Al final del canal, instalar un filtro casero con capas de grava, arena y carbón activado dentro de una botella cortada\n"
    f"6.-El agua filtrada cae directamente en un tinaco o depósito reciclado con tapa y válvula de salida.\n")

# Función para la verificación de material reunido para contruir el sistema de captación
print("Verificar si contamos con los materiales para captación de agua pluvial...")
def verificar_material():
    while True:
        material_respuesta = input(f"¿Tienes todos los materiales? (Si/No)\n")
        if material_respuesta == 'si' or material_respuesta == 'si':
            print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
            print("Como siguiente paso es crear el sistema de captación de agua pluvial con los materiales reunidos.")
            print("Pasos a seguir:\n")
            print(creacion) # Se llama la variable creacion con uso de print
            pasos_completados() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif material_respuesta == 'no':
            print(f"\n¡Revisa que materiales requeridos te hacen falta para crear el sistema!\n")
            print(f'"Sin materiales no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual 

# Función para la verificacion de contrucción del sistema de captación de agua conforme a los pasos dados
def pasos_completados():
    while True:
        pasos_completados = input(f"¿Se completo con exito la pasos para creación del sistema de captación de agua pluvial? (Si/No)\n")
        if pasos_completados == 'si' or pasos_completados == 'si':
            print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvia listo para funcionar!\n")
            calcular_capacidad() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif pasos_completados == 'no':
            print(f"\nSistema de captacion de agua pluvial no contruido.")
            print(f'"Sin infraestructura no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual

# Funcion para el calculo aproximado de almacenamiento de agua pluvial
def calcular_capacidad():
    print("\nCálculo de Capacidad.")
    print("Ahora veremos cuantos litros de capacidad obtendremos de acuerdo al tamaño de botella utilizado, ingrese los datos.")   
    print("\nOpciones de módulos para almacenamiento con PET:\n")
    print("1. Botellas de 2.5 Litros.")
    print("2. Botellas de 3 Litros.")   
    while True:            
        tamaño_botella = input("Seleccione el tipo de botella usado (1 o 2): ")
        num_modulos = int(input("Ingrese el número total de botellas interconectados: "))
        if tamaño_botella == '1' or tamaño_botella =='1':  # Botellas de 2.75 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = num_modulos * 2.75
        elif tamaño_botella == '2':  # Botellas de 3 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = num_modulos * 3
        else:
            print("\nOpción inválida.\nSolo ingresa 1 o 2.")
            continue # Vuelve a iniciar el ciclo actual      
        capacidad_final = capacidad_litros        
        print(f"\nDatos de Capacidad del Sistema de captación de agua pluvial:")
        print(f"   Botellas utilizados: {num_modulos}")
        print(f"   Capacidad total estimado: {capacidad_final} litros.")
        print(f"\n¡Genial! ¡Tienes un sistema con una capacidad de {capacidad_final} litros para almacenamiento de agua pluvial!\n")
        llueve() # Función activada e inicio de esta
        break

# Funcion para la verificación de si llueve o no y funcione la recolección de agua pluvial
def llueve():
    while True:
        print("Ahora para que funcione el sistema se debe confirmar si llueve.")
        lluvia = input(f"¿Esta lloviendo en la UNRC? (Si/No)\n")
        if lluvia == 'si' or lluvia == 'si':
            print(f"\nEl sistema se activa...\n\n"
            f"El agua llega a traves a traves de los canales construidos\n"
            f"¡Genial! ¡El agua se almacena en el deposito!\n\n"
            f"El agua recolectada se podria usar para:\n"
            f"Riego de plantas, Limpeza de salones y patio, Uso sanitario\n\n"
            f"Se debe dar mantenimiento al sistema; monitorearlo, limpiarlo, cambiar filtros, etc\n"
            f'"Condicion sana, buena eficiencia"')                        
            break #Termina el bucle actual
        elif lluvia == 'no':
            print(f"\nEsperar a que llueva y poder monitorear.\n")
            print(f'"Sin lluvia no hay recolección y monitoreo"')
            break #Termina el bucle actual          
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual
verificar_material() # Función activada e inicio de esta
# Fin