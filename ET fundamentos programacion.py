
import csv #para poder manejar archivos de csv.
import functools #para faciliar el manejo de la lista de sueldos y no me de error porque sea una tupla/lista/string.
import random #para crear el numero de forma aleatoria.
from statistics import geometric_mean #esto el profe dijo que lo agregaramos durante la prueba.
#lista de trabajadores:
trabajadores = [
    "Juan Pérez" , "María García", "Carlos López", "Ana Martínez", 
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

def generar_sueldos():
    #se usa un return en el cual producimos 10 sueldos aleatorios, dentro del rango informado.
    return[random.randint(300000,2500000) for _ in range(10)]
    
def clasificar_sueldos(sueldos):
    #se crean 3 listas en las que se guardaran los sueldos, dependiendo de la categoria.
    bajos = []
    medios = []
    altos = []
    
    for i, sueldo in enumerate(sueldos):
        sueldo = int(sueldo)
        if sueldo < 800000:
            bajos.append([trabajadores[1],sueldo])
        elif sueldo >= 800000 and sueldo <2000000:
            medios.append([trabajadores[1],sueldo])
        else:
            altos.append([trabajadores[1],sueldo])
        #por cada sueldo, lo agregamos a una categoria de sueldo, y despues este se asigna a un trabajador.
    return bajos,medios,altos
#un return para devolver cada categoria de sueldo con los sueldos y informacion ya adentro.


def calcular_estadisticas(sueldos):
    #se crea una funcion con cada informacion a dar
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio= sum(sueldos) / len(sueldos)
    media_geometrica= round(geometric_mean(sueldos),1)
    return sueldo_max,sueldo_min,sueldo_promedio,media_geometrica
#return de cada informacion a dar por separado, para despues mostrar correspondientemente.

def generar_reporte_sueldos(sueldos):
    with open("reporte sueldos.csv", "w",newline="") as csvfile: #abrimos/creamos el archivo csv.
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre empleado", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo Liquido"])#hacemos esa primera linea que mostrara las categorias.
        for i, sueldo in enumerate(sueldos):
            salud = sueldo * 0.7
            afp = sueldo * 0.12
            sueldo_liquido = sueldo - salud - afp
            writer.writerow([trabajadores[i], sueldo, afp, sueldo_liquido])
            #se calcula individualmente cada uno de los descuentos de salud, afp, y el sueldo liquido, siendo almacenado en el archivo correspondiente.

def main():
    #nuestro codigo principal
    sueldos = generar_sueldos()
    #generamos los sueldos antes que nada
    while True:
        print("\nMenú:")
        print("1.- Asignar sueldos aleatorios")
        print("2.- Clasificar sueldos")
        print("3.- Ver estadísticas")
        print("4.- Reporte de sueldos")
        print("5.- Salir del programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("sueldos fueron generados aleatoriamene") #sueldos ya generados ;)
        elif opcion == "2":
            #escribimos la informacion de forma ordenada, por sueldos bajos, medios y altos.
            bajos, medios, altos = clasificar_sueldos(sueldos)
            print("\nSueldos bajos:")
            for nombre,sueldo in bajos:
                print(f"{nombre}: ${sueldo}")
            print("\nSueldos medios:")
            for nombre,sueldo in medios:
                print(f"{nombre}: ${sueldo}")
            print("\nSueldos altos:")
            for nombre,sueldo in altos:
                print(f"{nombre}: ${sueldos}")
        elif opcion == "3":
            #escribimos la informacion de forma ordenada, imprimiendo los datos a mostrar.
            sueldo_max,sueldo_min,sueldo_promedio,media_geometrica = calcular_estadisticas(sueldos)
            print(f"Sueldo mas alto: ${sueldo_max}")
            print(f"Fueldo mas bajo: ${sueldo_min}")
            print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
            print(f"Media geometrica: {media_geometrica:.2f}")
        elif opcion == "4":
            #se crea el archivo y se avisa que se imprimieron
            generar_reporte_sueldos(sueldos)
            print("reporte de sueldos generado en reporte_sueldos.csv")
            
        elif opcion == "5":
            print("Finalizando programa....")
            print("Desarrollado por Eric Saavedra Maldonado")
            print("RUT 21.737.347-6")
            break
        else:
            print ("Opción inválida. Intente nuevamente.")

if __name__ == "__main__": #ocupamos esta ultima escritura sagrada para hacer que el menu corra sin parar!.
    main()

