import os
os.system("cls")
# Función para grabar una encomienda


def grabar_encomienda():
    tipo = input("Ingrese el tipo de encomienda (sobre o paquete): ").lower()
    while tipo != "sobre" and tipo != "paquete":
        tipo = input("Tipo inválido. Ingrese el tipo de encomienda nuevamente (sobre o paquete): ").lower()
    
    nombre_destinatario = input("Ingrese el nombre del destinatario (entre 2 y 30 caracteres): ").upper()
    while len(nombre_destinatario) < 2 or len(nombre_destinatario) > 30:
        nombre_destinatario = input("Nombre inválido. Ingrese el nombre del destinatario nuevamente (entre 2 y 30 caracteres): ").upper()
    
    rut_destinatario = input("Ingrese el RUT del destinatario (con guión como penúltimo carácter): ").upper()
    while len(rut_destinatario) < 3 or rut_destinatario[-2] != "-":
        rut_destinatario = input("RUT inválido. Ingrese el RUT del destinatario nuevamente (con guión como penúltimo carácter): ").upper()
    
    peso = float(input("Ingrese el peso en kg de la encomienda (mínimo 0.1): "))
    while peso < 0.1:
        peso = float(input("Peso inválido. Ingrese el peso en kg de la encomienda nuevamente (mínimo 0.1): "))
    
    precio = int(input("Ingrese el precio de la encomienda (mínimo 2000): "))
    while precio < 2000:
        precio = int(input("Precio inválido. Ingrese el precio de la encomienda nuevamente (mínimo 2000): "))
    
    ciudad_destino = input("Ingrese la ciudad de destino (mínimo 3 caracteres): ").upper()
    while len(ciudad_destino) < 3:
        ciudad_destino = input("Ciudad inválida. Ingrese la ciudad de destino nuevamente (mínimo 3 caracteres): ").upper()
    
def buscar_encomienda(rut):
    rut = [] 

def listar_encomiendas(encomiendas):
    sobres = 0
    paquetes = 0
    
    print("Encomiendas registradas:")
    print("{:<10s} {:<20s} {:<15s} {:<10s} {:<10s} {:<15s}".format("Tipo", "Destinatario", "RUT", "Peso (kg)", "Precio", "Ciudad"))
    
    for encomienda in encomiendas:
        tipo = encomienda["tipo"]
        nombre_destinatario = encomienda["nombre"]
        nombre_destinatario = encomienda["nombre_destinatario"]
        rut_destinatario = encomienda["rut_destinatario"]
        peso = encomienda["peso"]
        precio = encomienda["precio"]
        ciudad_destino = encomienda["ciudad_destino"]
        
        print("{:<10s} {:<20s} {:<15s} {:<10.2f} {:<10d} {:<15s}".format(tipo, nombre_destinatario, rut_destinatario, peso, precio, ciudad_destino))
        
        if tipo == "sobre":
            sobres += 1
        else:
            paquetes += 1
    
    print("\nTotal de sobres: {}".format(sobres))
    print("Total de paquetes: {}".format(paquetes))
    
def menu():
    encomiendas = []  
    
    while True:
        print("\n--- Caracol Express ---")
        print("1. Grabar encomienda")
        print("2. Buscar encomienda por RUT")
        print("3. Listar encomiendas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            grabar_encomienda()
        elif opcion == "2":
            rut = input("Ingrese el RUT del destinatario para buscar: ")
            buscar_encomienda(rut)
        elif opcion == "3":
            listar_encomiendas(encomiendas)
        elif opcion == "4":
            print("¡Gracias por usar Caracol Express!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú principal 
menu()
def grabar_encomienda():
    tipo = input("Ingrese el tipo de encomienda (sobre o paquete): ").lower()
    while tipo != "sobre" and tipo != "paquete":
        tipo = input("Tipo inválido. Ingrese el tipo de encomienda nuevamente (sobre o paquete): ").lower()
    
    nombre_destinatario = input("Ingrese el nombre del destinatario (entre 2 y 30 caracteres): ").upper()
    while len(nombre_destinatario) < 2 or len(nombre_destinatario) > 30:
        nombre_destinatario = input("Nombre inválido. Ingrese el nombre del destinatario nuevamente (entre 2 y 30 caracteres): ").upper()
    
    rut_destinatario = input("Ingrese el RUT del destinatario (con guión como penúltimo carácter): ").upper()
    while len(rut_destinatario) < 3 or rut_destinatario[-2] != "-":
        rut_destinatario = input("RUT inválido. Ingrese el RUT del destinatario nuevamente (con guión como penúltimo carácter): ").upper()
    
    peso = float(input("Ingrese el peso en kg de la encomienda (mínimo 0.1): "))
    while peso < 0.1:
        peso = float(input("Peso inválido. Ingrese el peso en kg de la encomienda nuevamente (mínimo 0.1): "))
    
    precio = int(input("Ingrese el precio de la encomienda (mínimo 2000): "))
    while precio < 2000:
        precio = int(input("Precio inválido. Ingrese el precio de la encomienda nuevamente (mínimo 2000): "))
    
    ciudad_destino = input("Ingrese la ciudad de destino (mínimo 3 caracteres): ").upper()
    while len(ciudad_destino) < 3:
        ciudad_destino = input("Ciudad inválida. Ingrese la ciudad de destino nuevamente (mínimo 3 caracteres): ").upper()
    
    encomienda = {
        "tipo": tipo,
        "nombre_destinatario": nombre_destinatario,
        "rut_destinatario": rut_destinatario,
        "peso": peso,
        "precio": precio,
        "ciudad_destino": ciudad_destino
    }
    
    encomienda.append(encomienda)
    print("Encomienda registrada exitosamente.")

def buscar_encomienda(rut):
    encontradas = []
    
    for encomienda in encomienda:
        if encomienda["rut_destinatario"] == rut:
            encontradas.append(encomienda)
    
    if len(encontradas) == 0:
        print("No se encontraron encomiendas para el RUT especificado.")
    else:
        print("Encomiendas encontradas para el RUT {}:".format(rut))
        print("{:<10s} {:<20s} {:<15s} {:<10s} {:<10s} {:<15s}".format("Tipo", "Destinatario", "RUT", "Peso (kg)", "Precio", "Ciudad"))
        for encomienda in encontradas:
            tipo = encomienda["tipo"]
            nombre_destinatario = encomienda[nombre_destinatario]
            rut_destinatario = encomienda["rut_destinatario"]
            peso = encomienda["peso"]
            precio = encomienda["precio"]
            ciudad_destino = encomienda["ciudad_destino"]
            
            print("{:<10s} {:<20s} {:<15s} {:<10.2f} {:<10d} {:<15s}".format(tipo, nombre_destinatario, rut_destinatario, peso, precio, ciudad_destino))
    
def menu():
    encomiendas = [] 
    
    while True:
        print("\n--- Caracol Express ---")
        print("1. Grabar encomienda")
        print("2. Buscar encomienda por RUT")
        print("3. Listar encomiendas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            grabar_encomienda()
        elif opcion == "2":
            rut = input("Ingrese el RUT del destinatario para buscar: ")
            buscar_encomienda(rut)
        elif opcion == "3":
            listar_encomiendas(encomiendas)
        elif opcion == "4":
            print("¡Gracias por usar Caracol Express!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
menu()


# endwhile