import validaciones
import json

def crear_dicc(archivo):
    try:
        arch = open(archivo, "r")
    except:
        print("No se pudo abrir el archivo")
    else:
        diccionario = json.load(arch)
    finally:
        arch.close()
    return diccionario

def cargar_datos(archivo, diccionario):
    try:
        arch = open(archivo, "w")
    except:
        print("No se pudo abrir el archivo")
    else:
        json.dump(diccionario,arch)
    finally:
        arch.close()

def crear(archivo):
    '''
    pre: recibe diccionario por parametro pide 4 datos y los valida
    pos: devuelve diccionario con nuevo cliente agregado
    '''
    diccionario = crear_dicc(archivo)

    conjunto_clientes = set(diccionario.keys())
    dni = input("DNI (XXXXXXXX): ")
    while not validaciones.validar_dni(dni) or dni in conjunto_clientes:
        if dni in conjunto_clientes:
            dni = input("DNI ya existente, ingrese un DNI distinto: ")
        else:
            dni = input("Ingrese el formato correcto(XXXXXXXX): ")

    nombre = input("Nombre: ")
    email = input("Email: ")
    while not validaciones.validar_email(email):
        email = input("Ingrese un email valido: ")

    telefono = input("Teléfono (XXXX-XXXXXX): ")
    while not validaciones.validar_telefono(telefono):
        telefono = input("Ingrese un telefono valido (XXXX-XXXXXX): ")

    diccionario[dni] = {"nombre": nombre, "email": email, "telefono": telefono}
    
    cargar_datos(archivo, diccionario)

def leer(archivo):
    '''
    pre: recibe diccionario por parametro, itera sobre los pares del diccionario con clave,valor
    pos: imprime el diccionario de manera centrada
    '''
    diccionario = crear_dicc(archivo)
    print(f'{"DNI":^12} {"Nombre":^20} {"Email":^25} {"Teléfono":^15}')
    for dni, valor in diccionario.items():
        print(f'{dni:^12} {valor["nombre"]:^20} {valor["email"]:^25} {valor["telefono"]:^15}')

def actualizar_cliente(archivo):
    '''
    pre: pide clave DNI, si la encuentra pide otros datos
    pos: devuelve diccionario con datos actualizados
    '''
    diccionario = crear_dicc(archivo)
    dni = input("DNI: ")
    if dni in diccionario:
        email = input("Nuevo Email: ")
        while not validaciones.validar_email(email):
            email = input("Ingrese un email valido: ")

        telefono = input("Nuevo Teléfono: ")
        while not validaciones.validar_telefono(telefono):
            telefono = input("Ingrese un telefono valido: ")

        diccionario[dni]["email"] = email
        diccionario[dni]["telefono"] = telefono
    else:
        print("No se encontro el cliente")
    
    cargar_datos(archivo, diccionario)

def eliminar(archivo):
    '''
    pre: pide clave DNI, si la encuentra borra la linea clave-valor
    pos: devuelve diccionario actualizado
    '''
    diccionario = crear_dicc(archivo)
    dni = input("DNI: ")
    if dni in diccionario:
        del diccionario[dni]
        print("Cliente eliminado")
    else:
        print("No se encontro el cliente")
    
    cargar_datos(archivo, diccionario)
