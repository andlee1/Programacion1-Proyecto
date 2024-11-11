import validaciones
import json
from crudCliente import crear_dicc

def crear_matriz(archivo):
    try:
        with open(archivo, 'r') as arch:
            matriz = [linea.strip().split(';') for linea in arch]
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    return matriz

def cargar_datos(archivo,matriz):
    try:
        with open(archivo, 'w') as arch:
            for i in matriz:
                linea = ';'.join(i) + '\n'
                arch.write(linea)

    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")

def append_datos(archivo,lista):
    try:
        with open(archivo, 'a') as arch:
            for i in lista:
                linea = ';'.join(i) + '\n'
                arch.write(linea)

    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")

def comprar_producto(archivo_stock, archivo_clientes,archivo_ventas):
    '''
    pre: recibe diccionario, matriz y matriz vacia. pide mas datos
    pos: agrega listas a la matriz vacia y retorna multiples parametros
    '''
    #Creo matriz electro
    matriz_e = crear_matriz(archivo_stock)

    #Creo diccionario
    diccionario = crear_dicc(archivo_clientes)  

    #Crear matriz ventas
    lista_v = []

    #Datos y validaciones
    producto = validaciones.validar_id()
    lista_id = [int(i[0]) for i in matriz_e]
    while producto not in lista_id:
        print("No se encontro el ID")
        producto = validaciones.validar_id()

    cantidad = validaciones.validar_cantidad()

    conjunto_clientes = set(diccionario.keys())
    dni = input("DNI (XXXXXXXX): ")
    while not validaciones.validar_dni(dni) or dni not in conjunto_clientes:
        if dni not in conjunto_clientes:
            dni = input("Ingrese un dni existente: ")
        else:
            dni = input("Ingrese el formato correcto(XXXXXXXX): ")

    #Buscar la fila del producto por id
    for fila in matriz_e:
        if fila[0] == str(producto):			
            #Controlar stock
            if cantidad > int(fila[3]):
                print(f'No hay sufieciente stock solo quedan {fila[3]} unidades')
            else:
                fila[3] = int(fila[3]) - cantidad #Restar stock
                precio_total = int(fila[2]) * cantidad

                lista_v.append([
                    diccionario[dni]['nombre'][:15],
                    dni,
                    fila[1][:8], #producto
                    str(cantidad),
                    str(precio_total)])
                
    append_datos(archivo_ventas,lista_v)                 
    matriz_str = [[str(j) for j in i] for i in matriz_e] #pasar todo a str para escribir el archivo
    cargar_datos(archivo_stock, matriz_str)


def devolver_producto(archivo_stock, archivo_ventas):
    '''
    pre: recibe archivo de stock y archivo de ventas.
    pos: devolver un producto, actualiza el stock y elimina o actualiza la venta.
    '''
    # Cargar los datos de ventas y stock
    matriz_ventas = crear_matriz(archivo_ventas)
    matriz_stock = crear_matriz(archivo_stock)

    dni = input("Ingrese su DNI para buscar compras: ")
    while not validaciones.validar_dni(dni):
        dni = input("Ingrese un DNI válido (XXXXXXXX): ")

    # Comprar del cliente, no se puede usar mostrar_compras_cliente() porque trabaja con archivos
    compras_cliente = [lista for lista in matriz_ventas if lista[1] == dni]

    print(f'{"Nombre":^15} {"DNI":^9} {"Producto":^10} {"Cantidad":^10} {"Precio":^8}')
    for nombre, dni, producto, cantidad, precio_total in compras_cliente: 
        print(f'{nombre:^15} {dni:^9} {producto:^10} {cantidad:^10} {precio_total:^8}')

    # Seleccionar compra a devolver
    num_compra = validaciones.validar_id()
    while num_compra not in range(1, len(compras_cliente) + 1):
        print("No se encontro la compra")
        num_compra = validaciones.validar_id()

    compra_seleccionada = compras_cliente[int(num_compra) - 1]

    # Actualizar stock
    for fila in matriz_stock:
        if fila[1] == compra_seleccionada[2]:  # Comparar por nombre de producto
            fila[3] = str(int(fila[3]) + int(compra_seleccionada[3]))  # Actualizar cantidad de stock

    # Remover la compra de la lista de ventas
    matriz_ventas.remove(compra_seleccionada)

    # Guardar cambios en los archivos
    cargar_datos(archivo_ventas, matriz_ventas)
    cargar_datos(archivo_stock, matriz_stock)

    print("Producto devuelto")


def mostar_compras_cliente(archivo_ventas):
    '''
    pre: recibe matriz de ventas y pide clave dni
    pos: retorna matriz recortada cuando coincide la clave con elemento de la fila 
    '''
    matriz = crear_matriz(archivo_ventas)
    dni = input("Ingrse su DNI: ")
    while not validaciones.validar_dni(dni):
        dni = input("Ingese un dni valido (XXXXXXXX): ")

    matriz_recortada = [] 
    for fila in matriz:
        if dni == fila[1]:
            matriz_recortada.append(fila)
    return matriz_recortada

def mostrar_ventas(archivo):
    '''
    pre: recibe una matriz
    pos: imprime de manera ordenada
    '''
    print(f'{"Nombre":^15} {"DNI":^9} {"Producto":^10} {"Cantidad":^10} {"Precio":^8}')
    try:
        with open(archivo, 'r') as arch:
            for linea in arch:
                nombre, dni, producto, cantidad, precio_total = linea.strip().split(';') 
                print(f'{nombre:^15} {dni:^9} {producto:^10} {cantidad:^10} {precio_total:^8}')
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")